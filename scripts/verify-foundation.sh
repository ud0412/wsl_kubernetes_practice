#!/usr/bin/env bash
source "$(dirname "$0")/lib/common.sh"
owned_state
docker info >/dev/null
owned_nodes
node_count=$(docker ps -q --filter "label=io.x-k8s.kind.cluster=$LAB_NAME" | wc -l)
[[ $node_count -eq 2 ]] || {
	echo 'Expected two running owned kind nodes.' >&2
	exit 1
}
k wait --for=condition=Ready nodes --all --timeout=180s
k version -o json | "$PYTHON_BIN" -c 'import json,sys; assert json.load(sys.stdin)["serverVersion"]["gitVersion"] == "v'"$KUBERNETES_VERSION"'", "Unexpected Kubernetes server version"'
k get nodes -o json | "$PYTHON_BIN" -c 'import json,sys; d=json.load(sys.stdin); assert {x["metadata"]["name"] for x in d["items"]} == {"observability-lab-control-plane","observability-lab-worker"}'
k -n kube-system rollout status daemonset/cilium --timeout=180s
ready envoy-gateway-system envoy-gateway
k wait --for=condition=Established crd/gateways.gateway.networking.k8s.io --timeout=120s
k -n envoy-gateway-system wait --for=condition=Accepted gateway/lab --timeout=180s
k -n envoy-gateway-system wait --for=condition=Programmed gateway/lab --timeout=180s
if [[ ${1:-} == --check ]]; then
	"$PYTHON_BIN" "$LAB_ROOT/scripts/lib/state.py" check-foundation
else
	"$PYTHON_BIN" "$LAB_ROOT/scripts/lib/state.py" write-foundation
fi
echo 'Foundation ownership, nodes, Cilium and Gateway are ready.'
