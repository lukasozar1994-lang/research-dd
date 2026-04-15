#!/usr/bin/env bash
set -euo pipefail

repo_root=""
task_id=""
task_ids=""
task_slug=""
topic=""
run_seq="001"
branch_name=""
decision=""
output=""
allow_empty="false"
dry_run="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root)
      repo_root="$2"
      shift 2
      ;;
    --task-id)
      task_id="$2"
      shift 2
      ;;
    --task-ids)
      task_ids="$2"
      shift 2
      ;;
    --task-slug)
      task_slug="$2"
      shift 2
      ;;
    --topic)
      topic="$2"
      shift 2
      ;;
    --run-seq)
      run_seq="$2"
      shift 2
      ;;
    --branch-name)
      branch_name="$2"
      shift 2
      ;;
    --decision)
      decision="$2"
      shift 2
      ;;
    --output)
      output="$2"
      shift 2
      ;;
    --allow-empty)
      allow_empty="true"
      shift
      ;;
    --dry-run)
      dry_run="true"
      shift
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 1
      ;;
  esac
done

repo_root="${repo_root:-$PWD}"

if [[ "$decision" != "accept" ]]; then
  echo "Commit requires --decision accept" >&2
  exit 2
fi

if [[ -z "$task_id" || -z "$task_slug" || -z "$topic" || -z "$branch_name" ]]; then
  echo "Missing required arguments" >&2
  exit 1
fi

cd "$repo_root"

subject="$task_id: $task_slug"
body_lines=(
  "Topic: $topic"
  "Run: $run_seq"
  "Branch: $branch_name"
  "Tasks: $task_ids"
  "Gate: accept"
)

message_full="$subject"
message_full+=$'\n\n'
message_full+="${body_lines[0]}"
for ((i = 1; i < ${#body_lines[@]}; i++)); do
  message_full+=$'\n'
  message_full+="${body_lines[$i]}"
done

commit_sha=""
if [[ "$dry_run" != "true" ]]; then
  git add -A
  commit_args=(commit -m "$subject")
  for line in "${body_lines[@]}"; do
    commit_args+=( -m "$line" )
  done
  if [[ "$allow_empty" == "true" ]]; then
    commit_args+=( --allow-empty )
  fi
  git "${commit_args[@]}" >/dev/null
  commit_sha="$(git rev-parse HEAD)"
fi

changed_files="$(git diff --name-only HEAD~1..HEAD 2>/dev/null || true)"
timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

body_lines_joined="$(printf '%s\n' "${body_lines[@]}")"
json="$(SUBJECT="$subject" \
TOPIC="$topic" \
RUN_SEQ="$run_seq" \
BRANCH_NAME="$branch_name" \
TASK_ID="$task_id" \
TASK_IDS_CSV="$task_ids" \
BODY_LINES="$body_lines_joined" \
MESSAGE_FULL="$message_full" \
COMMIT_SHA="$commit_sha" \
TIMESTAMP="$timestamp" \
CHANGED_FILES="$changed_files" \
node <<'NODE'
const data = {
  schema_version: '1.0.0',
  topic_slug: process.env.TOPIC,
  run_sequence: process.env.RUN_SEQ,
  branch_name: process.env.BRANCH_NAME,
  primary_task_id: process.env.TASK_ID,
  task_ids: (process.env.TASK_IDS_CSV || '').split(',').map((item) => item.trim()).filter(Boolean),
  message_subject: process.env.SUBJECT,
  message_body_lines: (process.env.BODY_LINES || '').split('\n').filter(Boolean),
  message_full: process.env.MESSAGE_FULL || '',
  commit_sha: process.env.COMMIT_SHA || '',
  committed_at: process.env.TIMESTAMP,
  changed_files: (process.env.CHANGED_FILES || '').split('\n').map((item) => item.trim()).filter(Boolean),
  gate_decision: 'accept',
};

process.stdout.write(JSON.stringify(data, null, 2));
NODE
)"

if [[ -n "$output" ]]; then
  mkdir -p "$(dirname "$output")"
  printf '%s\n' "$json" > "$output"
fi

printf '%s\n' "$json"