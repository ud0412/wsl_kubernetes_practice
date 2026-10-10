# 02 실습 — CNI 없는 kind 클러스터 생성

실행 위치: WSL Bash, 이 저장소 루트. 새 터미널마다 아래 접속 정보부터 설정합니다.

```bash
cd ~/practice/wsl_kubernetes_practice
export PATH="$HOME/.local/bin:$PATH"
export LAB_STATE_DIR="$HOME/.local/share/observability-practice/observability-lab"
export KUBECONFIG="$LAB_STATE_DIR/kubeconfig"
source config/versions.env
bash scripts/lab.sh prepare
```

prepare는 관리 폴더와 foundation-kind.yaml·foundation-gateway.yaml만 준비합니다. 처음에는 다음으로 생성합니다.

```bash
kind create cluster --name observability-lab --config "$LAB_STATE_DIR/rendered/foundation-kind.yaml" --kubeconfig "$KUBECONFIG"
kubectl config current-context
kubectl get nodes -o wide
```

context는 kind-observability-lab, 두 노드는 control-plane과 worker입니다. NotReady와 CoreDNS Pending은 CNI 설치 전 정상입니다. 이미 같은 실습 클러스터가 있다면 create를 반복하지 않고 `bash scripts/steps/01-cluster.sh`로 소유권을 확인한 뒤 재사용합니다.

```bash
cat "$LAB_STATE_DIR/rendered/foundation-kind.yaml"
```

확인: disableDefaultCNI=true, 노드 2개, 각 노드의 hostPath와 containerPath가 연결됩니다. 이미지 버전은 Kubernetes 1.36.4입니다. 생성 실패는 `docker info`, kind 오류와 WSL 디스크 여유를 먼저 확인합니다.


[목차](../README.md) · [다음](../03-cilium/01-concept.md)
