# 00 설명 — Windows 안에 실습 환경 만들기

WSL은 Windows에서 Linux를 실행하는 환경입니다. Docker Engine은 컨테이너를 실행하고, kind는 그 컨테이너를 Kubernetes 노드로 사용합니다. 이번에는 관리용 control-plane 하나와 작업용 worker 하나를 만듭니다.

CNI는 Pod가 서로 통신하도록 연결하는 구성입니다. Cilium을 CNI로 설치합니다. 외부 HTTP 요청을 원하는 서비스로 보내려면 Gateway API 규칙과 이를 실행하는 Envoy Gateway가 필요합니다.

학습 순서는 WSL 자원 → 도구 → Kubernetes → CNI → Gateway입니다. 기본 CNI를 제외한 클러스터를 먼저 생성하므로 중간에 NotReady가 보일 수 있습니다. 단계별 정상 결과를 읽으세요.


[목차](../README.md) · [다음](02-practice.md)
