#!/usr/bin/env bash
source "$(dirname "$0")/lib/common.sh"
case "${1:-help}" in
prepare)
	"$PYTHON_BIN" "$LAB_ROOT/scripts/lib/state.py" prepare >/dev/null
	"$PYTHON_BIN" "$LAB_ROOT/infrastructure/render.py"
	;;
up) bash "$LAB_ROOT/scripts/setup-infrastructure.sh" ;;
verify) bash "$LAB_ROOT/scripts/verify-foundation.sh" ;;
status)
	owned_state
	docker info >/dev/null
	owned_nodes
	k get nodes
	k get pods -A
	;;
destroy) bash "$LAB_ROOT/scripts/destroy-infrastructure.sh" ;;
*) echo 'Usage: bash scripts/lab.sh prepare|up|verify|status|destroy' ;;
esac
