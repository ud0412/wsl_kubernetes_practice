# 02 설명 — kind 노드와 데이터 폴더

kind는 Kubernetes 노드를 Docker 컨테이너로 실행합니다. 노드 내부에서는 containerd가 Pod 컨테이너를 실행합니다. 두 노드는 같은 WSL의 자원을 공유합니다.

기본 CNI를 제외하고 생성해 Cilium을 직접 설치합니다. 그래서 생성 직후 NotReady는 예상한 중간 상태입니다.

후속 실습에서 Pod가 재시작되어도 데이터를 보존하도록 각 노드의 `/var/local/observability`를 전용 WSL 폴더에 연결합니다. `extraMounts`는 이 폴더 연결 설정입니다. 클러스터 이름과 저장 경로는 후속 과정과 공유합니다.


[목차](../README.md) · [다음](02-practice.md)
