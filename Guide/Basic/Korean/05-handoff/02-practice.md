# 05 실습 — 자동 구축 후 Observability로 이동

시작 조건: 01 실습의 WSL·Docker·도구 준비 완료. 자동 경로를 선택했다면 02~04 수동 설치를 반복하지 않아도 됩니다.

```bash
cd ~/practice/wsl_kubernetes_practice
bash scripts/lab.sh up
bash scripts/lab.sh verify
```

정상 결과: 노드 두 개, Cilium, Gateway 준비 성공과 Foundation ready 메시지입니다. 수동 경로를 끝냈다면 verify만 수행해도 됩니다.

```bash
export LAB_STATE_DIR="$HOME/.local/share/observability-practice/observability-lab"
export KUBECONFIG="$LAB_STATE_DIR/kubeconfig"
kubectl get nodes
cat "$LAB_STATE_DIR/foundation.json"
```

완료 기록에는 클러스터·context·노드 이름·설정 버전 지문이 들어갑니다. 비밀번호는 포함하지 않습니다.

후속 저장소를 준비합니다.

```bash
cd ~/practice
git clone https://github.com/ud0412/observability_practice.git
cd observability_practice
export WSL_KUBERNETES_REPO="$HOME/practice/wsl_kubernetes_practice"
```

[Observability Basic 시작 실습](https://github.com/ud0412/observability_practice/blob/master/Guide/Basic/Korean/00-start/02-practice.md)으로 이동합니다. 이 시점에는 클러스터를 destroy하지 않습니다.

전체 실습을 끝낼 때 어느 저장소에서든 `bash scripts/lab.sh destroy`를 실행합니다. 후속 과정의 저장 데이터도 모두 제거됩니다. destroy를 두 번 실행해도 남은 실습이 없으면 성공합니다. Docker 전역 prune은 실행하지 않습니다.


[목차](../README.md) · [다음](../README.md)
