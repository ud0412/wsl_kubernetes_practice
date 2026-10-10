"""Render foundation resources only; never deploy."""
import sys
from pathlib import Path
import yaml
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts/lib"))
from state import state_path, check_owner

def render():
    path = state_path()
    check_owner(path)
    v = dict(line.split("=", 1) for line in (ROOT / "config/versions.env").read_text().splitlines() if line and not line.startswith("#"))
    kind = {"kind": "Cluster", "apiVersion": "kind.x-k8s.io/v1alpha4", "networking": {"disableDefaultCNI": True},
            "nodes": [{"role": role, "image": v["KIND_NODE_IMAGE"], "extraMounts": [{
                "hostPath": str(path / "nodes" / role), "containerPath": "/var/local/observability"}]}
            for role in ("control-plane", "worker")]}
    proxy = {"apiVersion": "gateway.envoyproxy.io/v1alpha1", "kind": "EnvoyProxy", "metadata": {"name": "lab-proxy", "namespace": "envoy-gateway-system"},
             "spec": {"provider": {"type": "Kubernetes", "kubernetes": {"envoyService": {"type": "ClusterIP"}}}}}
    gateway_class = {"apiVersion": "gateway.networking.k8s.io/v1", "kind": "GatewayClass", "metadata": {"name": "lab-gateway"},
                     "spec": {"controllerName": "gateway.envoyproxy.io/gatewayclass-controller", "parametersRef": {
                         "group": "gateway.envoyproxy.io", "kind": "EnvoyProxy", "name": "lab-proxy", "namespace": "envoy-gateway-system"}}}
    gateway = {"apiVersion": "gateway.networking.k8s.io/v1", "kind": "Gateway", "metadata": {"name": "lab", "namespace": "envoy-gateway-system"},
               "spec": {"gatewayClassName": "lab-gateway", "listeners": [{"name": "http", "protocol": "HTTP", "port": 80,
                          "allowedRoutes": {"namespaces": {"from": "All"}}}]}}

    for filename, documents in [("foundation-kind.yaml", [kind]), ("foundation-gateway.yaml", [proxy, gateway_class, gateway])]:
        (path / "rendered" / filename).write_text(yaml.safe_dump_all(documents, sort_keys=False))
    print("Rendered foundation resources")

if __name__ == "__main__": render()
