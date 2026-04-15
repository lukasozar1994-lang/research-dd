import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { parseArgs } from 'node:util';

export async function buildExecutionReport({ reviewPath, validationPath, commitPath }) {
  const review = JSON.parse(await readFile(reviewPath, 'utf8'));
  const validation = JSON.parse(await readFile(validationPath, 'utf8'));
  const commit = JSON.parse(await readFile(commitPath, 'utf8'));

  const report = {
    run_sequence: commit.run_sequence,
    branch_name: commit.branch_name,
    task_ids: commit.task_ids,
    validation_status: validation.status,
    review_decision: review.decision,
    commit_sha: commit.commit_sha,
    report_status: review.decision === 'accept' ? 'completed' : 'needs_attention',
    remaining_risks: review.risk_findings,
    next_step: review.decision === 'accept' ? 'Developer reviews the branch and decides on the merge.' : 'Address review findings and rerun validation.',
    generated_at: new Date().toISOString(),
  };

  const markdown = [
    '# Execution Report',
    '',
    `- Branch: ${report.branch_name}`,
    `- Tasks: ${report.task_ids.join(', ')}`,
    `- Validation: ${report.validation_status}`,
    `- Review: ${report.review_decision}`,
    `- Commit: ${report.commit_sha || 'pending'}`,
    `- Next step: ${report.next_step}`,
  ].join('\n');

  return { report, markdown };
}

async function main() {
  const { values } = parseArgs({
    options: {
      review: { type: 'string' },
      validation: { type: 'string' },
      commit: { type: 'string' },
      'json-out': { type: 'string' },
      'md-out': { type: 'string' },
    },
    strict: true,
  });

  if (!values.review || !values.validation || !values.commit || !values['json-out'] || !values['md-out']) {
    throw new Error('--review, --validation, --commit, --json-out and --md-out are required');
  }

  const { report, markdown } = await buildExecutionReport({
    reviewPath: path.resolve(values.review),
    validationPath: path.resolve(values.validation),
    commitPath: path.resolve(values.commit),
  });

  const jsonOut = path.resolve(values['json-out']);
  const mdOut = path.resolve(values['md-out']);
  await mkdir(path.dirname(jsonOut), { recursive: true });
  await mkdir(path.dirname(mdOut), { recursive: true });
  await writeFile(jsonOut, `${JSON.stringify(report, null, 2)}\n`, 'utf8');
  await writeFile(mdOut, `${markdown}\n`, 'utf8');

  process.stdout.write(`${JSON.stringify(report, null, 2)}\n`);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : String(error));
    process.exit(1);
  });
}