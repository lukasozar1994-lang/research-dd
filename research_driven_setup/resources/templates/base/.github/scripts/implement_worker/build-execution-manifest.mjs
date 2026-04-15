import { readFile, writeFile, mkdir } from 'node:fs/promises';
import path from 'node:path';
import { parseArgs } from 'node:util';

function parseMarkdownTable(markdown) {
  return markdown
    .split('\n')
    .filter((line) => line.startsWith('| TASK-'))
    .map((line) => line.split('|').slice(1, -1).map((cell) => cell.trim()));
}

function parseTaskRows(markdown) {
  return parseMarkdownTable(markdown).map((row) => {
    const [taskId, purpose, inputArtifacts, filesToCreateOrUpdate, implementationUnits, testsRequired, completionCriteria] = row;
    const combined = row.join(' ');
    return {
      task_id: taskId,
      purpose,
      input_artifacts: inputArtifacts.split(',').map((item) => item.trim()).filter(Boolean),
      target_files: filesToCreateOrUpdate.split(',').map((item) => item.trim()).filter(Boolean),
      implementation_units: implementationUnits.split(',').map((item) => item.trim()).filter(Boolean),
      tests_required: testsRequired.split(',').map((item) => item.trim()).filter(Boolean),
      completion_criteria: completionCriteria,
      browser_required: /browser|playwright/i.test(combined),
    };
  });
}

function inferValidationCommands(taskId, browserRequired) {
  const commands = {
    'TASK-002': ['node --test tests/implement_worker/test_execution_manifest_builder.mjs'],
    'TASK-003': ['node --test tests/implement_worker/test_branch_preflight.mjs'],
    'TASK-005': [
      'node --test tests/implement_worker/test_review_packet.mjs',
      'node --test tests/implement_worker/test_commit_after_gate.mjs',
      'node --test tests/implement_worker/test_execution_report.mjs',
    ],
    'TASK-007': ['node --test tests/implement_worker/test_mcp_config_snapshot.mjs'],
    'TASK-008': ['node --test tests/implement_worker/test_execution_manifest_builder.mjs'],
  };

  const selected = commands[taskId] ?? ['node --test tests/implement_worker/*.mjs'];
  if (browserRequired) {
    return [...selected, 'npx --no-install playwright-cli --help'];
  }
  return selected;
}

export async function buildExecutionManifest({ planDir, scope = 'all', runSequence = '001', branchName }) {
  const taskBreakdown = await readFile(path.join(planDir, '07_task_breakdown.md'), 'utf8');
  const taskRows = parseTaskRows(taskBreakdown);
  const scopedTasks = scope === 'all' ? taskRows : taskRows.filter((task) => task.task_id === scope);

  if (scopedTasks.length === 0) {
    throw new Error(`No tasks matched scope: ${scope}`);
  }

  const topicSlug = path.basename(path.dirname(planDir));
  const runtimeRoot = path.join(path.dirname(planDir), 'przebieg_implementacji');
  const runDir = path.join(runtimeRoot, runSequence);
  const resolvedBranch = branchName ?? `${topicSlug}-${runSequence}`;
  const browserRequired = scopedTasks.some((task) => task.browser_required);

  return {
    schema_version: '1.0.0',
    topic_slug: topicSlug,
    plan_path: planDir,
    run_sequence: runSequence,
    branch_name: resolvedBranch,
    selected_scope: scope,
    task_ids: scopedTasks.map((task) => task.task_id),
    tasks: scopedTasks.map((task) => ({
      ...task,
      validation_commands: inferValidationCommands(task.task_id, task.browser_required),
    })),
    browser_required: browserRequired,
    validation_commands: [...new Set(scopedTasks.flatMap((task) => inferValidationCommands(task.task_id, task.browser_required)))],
    target_files: [...new Set(scopedTasks.flatMap((task) => task.target_files))],
    runtime_paths: {
      runtime_root: runtimeRoot,
      run_dir: runDir,
      branch_context: path.join(runDir, 'branch-context.json'),
      checkpoints_dir: path.join(runDir, 'checkpoints'),
      validation_dir: path.join(runDir, 'validation-packets'),
      review_dir: path.join(runDir, 'review-packets'),
      commit_record: path.join(runDir, 'commit.json'),
      report_json: path.join(runDir, 'execution-report.json'),
      report_md: path.join(runDir, 'execution-report.md'),
    },
  };
}

async function main() {
  const { values } = parseArgs({
    options: {
      plan: { type: 'string' },
      scope: { type: 'string', default: 'all' },
      output: { type: 'string' },
      'run-seq': { type: 'string', default: '001' },
      branch: { type: 'string' },
    },
    strict: true,
  });

  if (!values.plan) {
    throw new Error('--plan is required');
  }

  const manifest = await buildExecutionManifest({
    planDir: path.resolve(values.plan),
    scope: values.scope,
    runSequence: values['run-seq'],
    branchName: values.branch,
  });

  if (values.output) {
    const resolvedOutput = path.resolve(values.output);
    await mkdir(path.dirname(resolvedOutput), { recursive: true });
    await writeFile(resolvedOutput, `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');
  }

  process.stdout.write(`${JSON.stringify(manifest, null, 2)}\n`);
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch((error) => {
    console.error(error instanceof Error ? error.message : String(error));
    process.exit(1);
  });
}