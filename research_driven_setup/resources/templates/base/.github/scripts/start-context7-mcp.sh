#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(CDPATH="" cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
ENV_FILE="$WORKSPACE_ROOT/.env"

if [[ -z "${CONTEXT7_API_KEY:-}" && -f "$ENV_FILE" ]]; then
  CONTEXT7_API_KEY="$({
    grep -E '^[[:space:]]*CONTEXT7_API_KEY[[:space:]]*=' "$ENV_FILE" || true
  } | tail -n 1 | sed -E 's/^[[:space:]]*CONTEXT7_API_KEY[[:space:]]*=[[:space:]]*//' | sed -E 's/^"(.*)"$/\1/; s/^'"'"'(.*)'"'"'$/\1/')"
  export CONTEXT7_API_KEY
fi

if [[ -z "${CONTEXT7_API_KEY:-}" ]]; then
  echo "CONTEXT7_API_KEY is not set. Define it in $ENV_FILE." >&2
  exit 1
fi

exec npx -y @upstash/context7-mcp --api-key "$CONTEXT7_API_KEY" "$@"