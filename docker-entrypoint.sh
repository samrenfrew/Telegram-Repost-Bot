#!/usr/bin/env bash
set -euo pipefail

REPOST_CONFIG_PATH="${REPOST_CONFIG_PATH:-config/defaultconfig.yaml}"
REPOST_USE_ENV="${REPOST_USE_ENV:-true}"
REPOST_DROP_PENDING_UPDATES="${REPOST_DROP_PENDING_UPDATES:-false}"

to_bool() {
  local value="${1,,}"
  [[ "$value" == "1" || "$value" == "true" || "$value" == "yes" || "$value" == "y" ]]
}

python scripts/init_db.py

args=("-c" "$REPOST_CONFIG_PATH")
if to_bool "$REPOST_USE_ENV"; then
  args+=("-e")
fi
if to_bool "$REPOST_DROP_PENDING_UPDATES"; then
  args+=("-d")
fi

exec python main.py "${args[@]}"
