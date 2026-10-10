# 03 실습 — Cilium 설치와 DNS·Service 통신

시작 조건: 두 kind 노드 생성 완료. WSL Bash, 저장소 루트, 02 실습의 환경변수와 버전 읽기를 적용합니다.

```bash
helm repo add cilium https://helm.cilium.io --force-update
helm repo update cilium
helm upgrade --install cilium cilium/cilium --version "$CILIUM_VERSION" -n kube-system --kubeconfig "$KUBECONFIG" --kube-context kind-observability-lab -f infrastructure/cilium/values.yaml --wait --timeout 10m
kubectl wait --for=condition=Ready nodes --all --timeout=300s
kubectl -n kube-system get pods -l k8s-app=cilium -o wide
```

정상 결과: 두 노드 Ready, Cilium Pod 두 개 Ready입니다. [설정](../../../../infrastructure/cilium/values.yaml)을 읽어 Hubble·Gateway와 kube-proxy 설정을 확인합니다.

통신 확인용 namespace와 Pod를 잠시 만듭니다.

```bash
kubectl create namespace lab-check
kubectl -n lab-check run web --image=nginx:1.29.6-alpine
kubectl -n lab-check expose pod web --port=80
kubectl -n lab-check wait --for=condition=Ready pod/web --timeout=120s
kubectl -n lab-check run client --image=busybox:1.37.0 --restart=Never --command -- sh -c 'nslookup kubernetes.default; wget -qO- http://web'
kubectl -n lab-check wait --for=jsonpath='{.status.phase}'=Succeeded pod/client --timeout=120s
kubectl -n lab-check logs client
```

DNS 조회 결과와 nginx HTML이 나타나면 성공입니다. 확인한 뒤 정리합니다.

```bash
kubectl delete namespace lab-check
```

실패하면 `kubectl -n lab-check describe pod client`의 Events와 Cilium·CoreDNS 로그를 확인합니다. namespace를 지운 뒤 재시도하세요.

[Cilium kind 공식 설치](https://docs.cilium.io/en/stable/installation/kind/)


[목차](../README.md) · [다음](../04-gateway/01-concept.md)
