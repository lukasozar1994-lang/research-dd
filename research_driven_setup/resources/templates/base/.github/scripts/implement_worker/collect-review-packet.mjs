import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { parseArgs } from 'node:util';

function parseAcceptanceCriteria(markdown) {
  return markdown
    .split('\n')
    .map((line) => line.trim())
    .filter((line) => /^-\s+AC-|^\|\s*AC-/.test(line));
}

export async function buildReviewPacket({ taskId, acceptanceFile, validationFile, changedFiles = [], decision, reason }) {
  const acceptanceMarkdown = await readFile(acceptanceFile, 'utf8');
  const validation = JSON.parse(await readFile(validationFile, 'utf8'));
  const acceptanceCriteria = parseAcceptanceCriteria(acceptanceMarkdown).slice(0, 5);
  const defaultDecision = validation.status === 'pass' ? 'accept' : 'retry';

  return {
    task_id: taskId,
    changed_files: changedFiles,
    acceptance_mapping: acceptanceCriteria.map((criterion) => ({
      criterion,
      status: changedFiles.length > 0 ? 'covered' : 'unmapped',
    })),
    risk_findings: validation.status === 'pass' ? [] : ['Validation did not pass; review cannot accept this scope yet.'],
    decision: decision ?? defaultDecision,
    decision_reason: reason ?? (validation.status === 'pass' ? 'Validation passed and the task is ready for handoff.' : 'Validation failed or remained incomplete.'),
    created_at: new Date().toISOString(),
  };
}

async function main() {
  const { values } = parseArgs({
    options: {
      'task-id': { type: 'string' },
      'acceptance-file': { type: 'string' },
      'validation-file': { type: 'string' },
      'changed-files': { type: 'string', default: '' },
      decision: { type: 'string' },
      reason: { type: 'string' },
      output: { type: 'string' },
    },
    strict: true,
  });

  if (!values['task-id'] || !values['acceptance-file'] || !values['validation-file']) {
    throw new Error('--task-id, --acceptance-file and --validation-file are required');
  }

  const packet = await buildReviewPacket({
    taskId: values['task-id'],
    acceptanceFile: path.resolve(values['acceptance-file']),
    validationFile: path.resolve(values['validation-file']),
    changedFiles: values['changed-files'].split(',').map((item) => item.trim()).filter(Boolean),
    decision: values.decision,
    reason: values.reason,
  });

  if (values.output) {
    const resolvedOutput = path.resolve(values.output);
    await mkdir(path.dirname(resolvedOutput), { recursive: true });
    await writeFile(resolvedOutput, `${JSON.stringify(packet, null, 2)}\n`, 'utf8');
  }

  process.stdout.write(`${JSON.stringify(packet, null, 2)}\n`);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : String(error));
    process.exit(1);
  });
}