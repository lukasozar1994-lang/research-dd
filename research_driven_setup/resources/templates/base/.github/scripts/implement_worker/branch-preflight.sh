#!/usr/bin/env bash
set -euo pipefail

repo_root=""
topic=""
run_seq="001"
base_branch="main"
branch_name=""
output=""
dry_run="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo-root)
      repo_root="$2"
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
    --base-branch)
      base_branch="$2"
      shift 2
      ;;
    --branch-name)
      branch_name="$2"
      shift 2
      ;;
    --output)
      output="$2"
      shift 2
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
if [[ -z "$topic" ]]; then
  echo "--topic is required" >&2
  exit 1
fi

if [[ -z "$branch_name" ]]; then
  branch_name="${topic}-${run_seq}"
fi

cd "$repo_root"

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "Not a git repository: $repo_root" >&2
  exit 1
fi

created="false"
if [[ "$dry_run" != "true" ]]; then
  if git rev-parse --verify "$branch_name" >/dev/null 2>&1; then
    git switch "$branch_name" >/dev/null
  else
    if git rev-parse --verify "$base_branch" >/dev/null 2>&1; then
      git switch "$base_branch" >/dev/null
    fi
    git switch -c "$branch_name" >/dev/null
    created="true"
  fi
fi

current_branch="$(git branch --show-current)"
timestamp="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

json="{
  \"branch_name\": \"$branch_name\",
  \"run_sequence\": \"$run_seq\",
  \"created_from_ref\": \"$base_branch\",
  \"created_at\": \"$timestamp\",
  \"switched_at\": \"$timestamp\",
  \"branch_status\": \"$current_branch\",
  \"created\": $created,
  \"naming_source\": \"topic_slug + run_sequence\"
}"

if [[ -n "$output" ]]; then
  mkdir -p "$(dirname "$output")"
  printf '%s\n' "$json" > "$output"
fi

printf '%s\n' "$json"