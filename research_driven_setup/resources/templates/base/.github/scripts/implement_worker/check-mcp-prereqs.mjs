import { access, readFile } from 'node:fs/promises';
import path from 'node:path';
import { parseArgs } from 'node:util';
import { spawnSync } from 'node:child_process';

const REQUIRED_SERVERS = ['github', 'sequential-thinking', 'filesystem', 'open-websearch', 'context7'];
const LOCAL_BINARIES = {
  'sequential-thinking': ['npx', ['--no-install', 'mcp-server-sequential-thinking', '--help']],
  filesystem: ['node', ['-e', "require.resolve('@modelcontextprotocol/server-filesystem/package.json'); console.log('filesystem-ok');"]],
  'open-websearch': ['npx', ['--no-install', 'open-websearch', '--help']],
};

async function fileExists(target) {
  try {
    await access(target);
    return true;
  } catch {
    return false;
  }
}

function runCommand(command, args, cwd) {
  return spawnSync(command, args, {
    cwd,
    encoding: 'utf8',
    stdio: 'pipe',
  });
}

export async function inspectWorkspace({ workspace, smokeLocal = false, install = false }) {
  const mcpPath = path.join(workspace, '.vscode', 'mcp.json');
  const result = {
    ok: true,
    configPath: mcpPath,
    missingServers: [],
    localChecks: {},
    github: {},
  };

  const raw = await readFile(mcpPath, 'utf8');
  const config = JSON.parse(raw);
  const servers = config.servers ?? {};

  for (const name of REQUIRED_SERVERS) {
    if (!servers[name]) {
      result.missingServers.push(name);
      result.ok = false;
    }
  }

  if (servers.github) {
    result.github = {
      type: servers.github.type,
      url: servers.github.url,
      headers: servers.github.headers ?? {},
      valid:
        servers.github.type === 'http' &&
        servers.github.url === 'https://api.githubcopilot.com/mcp/' &&
        typeof (servers.github.headers ?? {})['X-MCP-Toolsets'] === 'string',
    };
    if (!result.github.valid) {
      result.ok = false;
    }
  }

  if (install) {
    const npmInstall = runCommand('npm', ['install'], workspace);
    result.install = {
      status: npmInstall.status,
      stdout: npmInstall.stdout.trim(),
      stderr: npmInstall.stderr.trim(),
    };
    if (npmInstall.status !== 0) {
      result.ok = false;
    }
  }

  const context7Script = path.join(workspace, '.github', 'scripts', 'start-context7-mcp.sh');
  result.localChecks.context7Script = {
    exists: await fileExists(context7Script),
  };
  if (!result.localChecks.context7Script.exists) {
    result.ok = false;
  }

  for (const [name, tuple] of Object.entries(LOCAL_BINARIES)) {
    const [command, args] = tuple;
    const check = { configured: Boolean(servers[name]) };
    if (smokeLocal && check.configured) {
      const run = runCommand(command, args, workspace);
      check.status = run.status;
      check.stdout = run.stdout.trim();
      check.stderr = run.stderr.trim();
      check.smokeOk = run.status === 0;
      if (!check.smokeOk) {
        result.ok = false;
      }
    }
    result.localChecks[name] = check;
  }

  return result;
}

async function main() {
  const { values } = parseArgs({
    options: {
      workspace: { type: 'string', default: process.cwd() },
      'smoke-local': { type: 'boolean', default: false },
      install: { type: 'boolean', default: false },
    },
  });

  const report = await inspectWorkspace({
    workspace: path.resolve(values.workspace),
    smokeLocal: values['smoke-local'],
    install: values.install,
  });

  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
  if (!report.ok) {
    process.exitCode = 1;
  }
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : String(error));
    process.exit(1);
  });
}