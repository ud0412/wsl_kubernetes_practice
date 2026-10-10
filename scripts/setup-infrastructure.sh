#!/usr/bin/env bash
source "$(dirname "$0")/lib/common.sh"
trap 'echo "Foundation setup failed at line $LINENO. Fix the cause and rerun up." >&2' ERR
bash "$LAB_ROOT/scripts/preflight.sh"
bash "$LAB_ROOT/scripts/lab.sh" prepare
for stage in "$LAB_ROOT"/scripts/steps/*.sh; do bash "$stage"; done
bash "$LAB_ROOT/scripts/verify-foundation.sh"
echo 'Foundation ready. Continue with observability_practice Basic.'
