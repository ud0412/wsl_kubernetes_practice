# 04 실습 — Gateway API와 Envoy Gateway 설치

시작 조건: Cilium과 두 노드 Ready. WSL Bash, 저장소 루트.

```bash
source config/versions.env
helm upgrade --install eg oci://docker.io/envoyproxy/gateway-helm --version "v$ENVOY_GATEWAY_VERSION" -n envoy-gateway-system --create-namespace --kubeconfig "$KUBECONFIG" --kube-context kind-observability-lab -f infrastructure/envoy-gateway/values.yaml --wait --timeout 10m
kubectl wait --for=condition=Established crd/gateways.gateway.networking.k8s.io --timeout=120s
kubectl apply -f "$LAB_STATE_DIR/rendered/foundation-gateway.yaml"
kubectl -n envoy-gateway-system wait --for=condition=Accepted gateway/lab --timeout=180s
kubectl -n envoy-gateway-system wait --for=condition=Programmed gateway/lab --timeout=180s
kubectl -n envoy-gateway-system get gateway,svc,pods
```

정상 결과: controller와 Proxy Pod Ready, Gateway Accepted·Programmed입니다. Service는 ClusterIP 방식이므로 외부 IP가 없어도 정상입니다.

```bash
kubectl get gatewayclass lab-gateway
kubectl -n envoy-gateway-system describe gateway lab
bash scripts/lab.sh verify
```

verify는 완료 확인과 후속 과정에 전달할 foundation.json을 기록합니다. 아직 HTTPRoute가 없으므로 입구에 접속해 404가 나오는 상태는 목적지가 없는 중간 단계입니다. 후속 Grafana 설치에서 실제 HTTP 응답을 확인합니다.

CRD 오류면 Helm 결과, Gateway가 Programmed되지 않으면 controller 로그와 Proxy Pod Events를 확인합니다. CRD와 controller 버전은 [호환성 표](https://gateway.envoyproxy.io/news/releases/matrix/)에 맞춘 고정 조합입니다.


[목차](../README.md) · [다음](../05-handoff/01-concept.md)
