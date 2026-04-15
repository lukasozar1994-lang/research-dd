import fs from "node:fs/promises";
import path from "node:path";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const workspaceRoot = process.cwd();
const defaultLimit = 3;
const defaultMaxChars = 120000;
const defaultEngines = ["duckduckgo"];
const defaultArtifactsDirName = "zrodla_i_analiza";

function getTextContent(result) {
  if (!result || !Array.isArray(result.content)) {
    throw new Error("Tool result has no MCP text content");
  }

  const text = result.content
    .filter((part) => part && part.type === "text" && typeof part.text === "string")
    .map((part) => part.text)
    .join("\n")
    .trim();

  if (!text) {
    throw new Error("Tool result returned empty text content");
  }

  return text;
}

function slugify(value) {
  return value
    .toLowerCase()
    .normalize("NFKD")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80) || "source";
}

function cleanFetchedContent(content) {
  return content
    .replace(/\r\n/g, "\n")
    .replace(//g, "")
    .replace(/^[ \t]+/gm, "")
    .replace(/[ \t]+$/gm, "")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
}

function parseList(value) {
  return value
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function normalizeOutputDir(value) {
  const normalized = value.replace(/\\+/g, "/").replace(/\/$/, "");
  if (!normalized) {
    return normalized;
  }

  if (path.posix.basename(normalized) === defaultArtifactsDirName) {
    return normalized;
  }

  return path.posix.join(normalized, defaultArtifactsDirName);
}

async function loadQueriesFromFile(filePath) {
  const fullPath = path.resolve(workspaceRoot, filePath);
  const raw = await fs.readFile(fullPath, "utf8");
  if (fullPath.endsWith(".json")) {
    const parsed = JSON.parse(raw);
    if (!Array.isArray(parsed)) {
      throw new Error("queries-file JSON must contain an array of strings");
    }
    return parsed.map((item) => String(item).trim()).filter(Boolean);
  }

  return raw
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
}

async function parseArgs(argv) {
  const options = {
    queries: [],
    limit: defaultLimit,
    maxChars: defaultMaxChars,
    engines: [...defaultEngines],
    outputDir: ""
  };

  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    const next = argv[index + 1];

    if (arg === "--query") {
      if (!next) {
        throw new Error("Missing value for --query");
      }
      options.queries.push(next.trim());
      index += 1;
      continue;
    }

    if (arg === "--queries-file") {
      if (!next) {
        throw new Error("Missing value for --queries-file");
      }
      options.queries.push(...await loadQueriesFromFile(next));
      index += 1;
      continue;
    }

    if (arg === "--limit") {
      options.limit = Number.parseInt(next, 10);
      index += 1;
      continue;
    }

    if (arg === "--max-chars") {
      options.maxChars = Number.parseInt(next, 10);
      index += 1;
      continue;
    }

    if (arg === "--engines") {
      options.engines = parseList(next);
      index += 1;
      continue;
    }

    if (arg === "--output-dir") {
      options.outputDir = next;
      index += 1;
      continue;
    }

    throw new Error(`Unknown argument: ${arg}`);
  }

  options.queries = options.queries.map((query) => query.trim()).filter(Boolean);

  if (options.queries.length === 0) {
    throw new Error("Provide at least one --query or --queries-file");
  }

  if (!Number.isInteger(options.limit) || options.limit < 1) {
    throw new Error("--limit must be a positive integer");
  }

  if (!Number.isInteger(options.maxChars) || options.maxChars < 1000) {
    throw new Error("--max-chars must be an integer >= 1000");
  }

  if (!options.outputDir) {
    options.outputDir = path.join("research_data", slugify(options.queries[0]), defaultArtifactsDirName);
  } else {
    options.outputDir = normalizeOutputDir(options.outputDir);
  }

  return options;
}

function buildMarkdown(fetchPayload, queryLabels) {
  const title = fetchPayload.title?.trim() || "Fetched Web Content";
  const cleanedContent = cleanFetchedContent(fetchPayload.content);
  const lines = [
    `# ${title}`,
    "",
    `- Source URL: ${fetchPayload.url}`,
    `- Final URL: ${fetchPayload.finalUrl}`,
    `- Content-Type: ${fetchPayload.contentType}`,
    `- Retrieval method: ${fetchPayload.retrievalMethod}`,
    `- Truncated: ${fetchPayload.truncated ? "yes" : "no"}`,
    `- Matched queries: ${queryLabels.join(" | ")}`,
    `- Fetched at: ${new Date().toISOString()}`,
    "",
    "---",
    "",
    cleanedContent,
    ""
  ];

  return lines.join("\n");
}

function buildIndexMarkdown(summary) {
  const lines = [
    "# Source Index",
    "",
    `- Generated at: ${summary.generatedAt}`,
    `- Output directory: ${summary.outputDir}`,
    `- Queries: ${summary.queries.join(" | ")}`,
    `- Requested search result limit: ${summary.limit}`,
    `- Successful fetches: ${summary.saved.length}`,
    `- Failed fetches: ${summary.failed.length}`,
    "",
    "## Saved Sources",
    ""
  ];

  if (summary.saved.length === 0) {
    lines.push("No sources were saved.", "");
  } else {
    for (const item of summary.saved) {
      lines.push(`- File: ${item.fileName}`);
      lines.push(`  URL: ${item.url}`);
      lines.push(`  Title: ${item.title || "(no title)"}`);
      lines.push(`  Queries: ${item.queries.join(" | ")}`);
      lines.push("");
    }
  }

  lines.push("## Failed Sources", "");

  if (summary.failed.length === 0) {
    lines.push("No fetch failures recorded.", "");
  } else {
    for (const item of summary.failed) {
      lines.push(`- URL: ${item.url}`);
      lines.push(`  Queries: ${item.queries.join(" | ")}`);
      lines.push(`  Error: ${item.error}`);
      lines.push("");
    }
  }

  return lines.join("\n");
}

async function createClient(name, transport) {
  const client = new Client({ name, version: "1.0.0" }, { capabilities: {} });
  await client.connect(transport);
  return client;
}

async function callToolJson(client, name, args) {
  const result = await client.callTool({ name, arguments: args });
  if (result.isError) {
    throw new Error(getTextContent(result));
  }
  return JSON.parse(getTextContent(result));
}

async function main() {
  const options = await parseArgs(process.argv.slice(2));
  const outputDir = path.resolve(workspaceRoot, options.outputDir);

  const webTransport = new StdioClientTransport({
    command: "npx",
    args: ["open-websearch"],
    cwd: workspaceRoot,
    env: {
      ...process.env,
      MODE: "stdio",
      DEFAULT_SEARCH_ENGINE: options.engines[0] || defaultEngines[0]
    },
    stderr: "pipe"
  });

  const filesystemTransport = new StdioClientTransport({
    command: "npx",
    args: ["mcp-server-filesystem", workspaceRoot],
    cwd: workspaceRoot,
    env: process.env,
    stderr: "pipe"
  });

  const webClient = await createClient("open-websearch-collector", webTransport);
  const filesystemClient = await createClient("filesystem-collector", filesystemTransport);

  try {
    await filesystemClient.callTool({
      name: "create_directory",
      arguments: { path: outputDir }
    });

    const discovered = new Map();

    for (const query of options.queries) {
      const searchPayload = await callToolJson(webClient, "search", {
        query,
        limit: options.limit,
        engines: options.engines
      });

      for (const result of searchPayload.results || []) {
        if (!result?.url) {
          continue;
        }

        const existing = discovered.get(result.url);
        if (existing) {
          existing.queries.add(query);
          continue;
        }

        discovered.set(result.url, {
          url: result.url,
          title: result.title || "",
          description: result.description || "",
          queries: new Set([query])
        });
      }
    }

    const saved = [];
    const failed = [];
    let counter = 1;

    for (const item of discovered.values()) {
      try {
        const fetchPayload = await callToolJson(webClient, "fetchWebContent", {
          url: item.url,
          maxChars: options.maxChars
        });

        const fileName = `${String(counter).padStart(2, "0")}-${slugify(fetchPayload.title || item.title || item.url)}.md`;
        const filePath = path.join(outputDir, fileName);
        const queryLabels = [...item.queries];
        const markdown = buildMarkdown(fetchPayload, queryLabels);

        const writeResult = await filesystemClient.callTool({
          name: "write_file",
          arguments: {
            path: filePath,
            content: markdown
          }
        });

        if (writeResult.isError) {
          throw new Error(getTextContent(writeResult));
        }

        saved.push({
          fileName,
          path: filePath,
          url: fetchPayload.url,
          title: fetchPayload.title || item.title || "",
          queries: queryLabels,
          truncated: Boolean(fetchPayload.truncated)
        });
        counter += 1;
      } catch (error) {
        failed.push({
          url: item.url,
          title: item.title,
          queries: [...item.queries],
          error: error instanceof Error ? error.message : String(error)
        });
      }
    }

    const summary = {
      generatedAt: new Date().toISOString(),
      outputDir,
      queries: options.queries,
      limit: options.limit,
      engines: options.engines,
      saved,
      failed
    };

    const indexMarkdown = buildIndexMarkdown(summary);

    await filesystemClient.callTool({
      name: "write_file",
      arguments: {
        path: path.join(outputDir, "source-index.md"),
        content: indexMarkdown
      }
    });

    await filesystemClient.callTool({
      name: "write_file",
      arguments: {
        path: path.join(outputDir, "source-index.json"),
        content: `${JSON.stringify(summary, null, 2)}\n`
      }
    });

    console.log(JSON.stringify({
      ok: true,
      outputDir,
      queries: options.queries,
      savedCount: saved.length,
      failedCount: failed.length,
      savedFiles: saved.map((item) => item.fileName)
    }, null, 2));
  } finally {
    await Promise.allSettled([
      webTransport.close(),
      filesystemTransport.close()
    ]);
  }
}

main().catch((error) => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exit(1);
});