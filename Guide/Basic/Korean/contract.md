# 두 과정의 연결·보존·삭제 계약

| 항목 | 값 |
|---|---|
| 계약 schema | 1 |
| 클러스터/context | observability-lab / kind-observability-lab |
| 노드 | observability-lab-control-plane, observability-lab-worker |
| 관리 경로 | ~/.local/share/observability-practice/observability-lab |
| kubeconfig | 관리 경로/kubeconfig |
| 노드 mount | 관리 경로/nodes/<role> → /var/local/observability |
| Gateway | envoy-gateway-system/lab, HTTP 80 |
| 기반 버전 | config/versions.env |

up은 기존 전용 노드를 재사용하기 전에 Docker label과 정확한 bind mount를 검사합니다. verify가 foundation.json에 현재 owner ID와 버전 지문을 기록합니다. Observability는 같은 계약과 버전을 확인하고 실제 노드·Cilium·Gateway 준비도 검사합니다.

기존 통합 과정과 저장 경로를 유지하여 새로 clone했다는 이유로 기존 데이터를 잃지 않도록 합니다. Pod 재시작은 WSL 폴더를 유지합니다. destroy는 경로와 owner marker, symlink, 노드 소유권을 확인하고 전용 클러스터와 전체 폴더를 제거합니다. root가 만든 파일의 삭제에는 sudo가 필요할 수 있습니다.

기반 버전을 바꾸려면 후속 과정의 호환 버전도 함께 검토해야 합니다. 임의 이름의 일반 클러스터는 이 전용 실습 환경으로 취급하지 않습니다.
