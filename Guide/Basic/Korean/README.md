# WSL Kubernetes Practice — Basic / Korean

이 과정은 Observability 과정의 선행 환경을 준비합니다. 설명을 읽고 같은 주제의 실습을 진행합니다. 화면 작업은 Windows, 클러스터 명령은 WSL Ubuntu Bash에서 실행합니다.

| 순서 | 주제 | 이해하기 | 따라 하기 |
|---|---|---|---|
| 00 | 과정과 실행 위치 | [설명](00-overview/01-concept.md) | [실습](00-overview/02-practice.md) |
| 01 | WSL 설정 앱과 도구 | [설명](01-wsl/01-concept.md) | [실습](01-wsl/02-practice.md) |
| 02 | kind Kubernetes | [설명](02-kubernetes/01-concept.md) | [실습](02-kubernetes/02-practice.md) |
| 03 | Cilium CNI | [설명](03-cilium/01-concept.md) | [실습](03-cilium/02-practice.md) |
| 04 | Gateway API와 Envoy Gateway | [설명](04-gateway/01-concept.md) | [실습](04-gateway/02-practice.md) |
| 05 | 자동 구축과 후속 과정 | [설명](05-handoff/01-concept.md) | [실습](05-handoff/02-practice.md) |

자동 경로도 먼저 01 실습의 WSL·Docker·도구 준비가 필요합니다. 그다음 05 실습을 수행하세요. 선행 과정에서 SeaweedFS나 Grafana는 설치하지 않습니다.

WSL GUI 안내는 Microsoft WSL Settings를 기준으로 합니다. 별도 WSL Config 앱은 동일한 자원 항목을 설정할 수 있지만 버튼 이름은 앱마다 다릅니다. 실제 사용자 앱의 확인되지 않은 버튼 이름을 만들어 안내하지 않습니다. 최종 적용 여부는 `free -h`, `nproc`로 확인합니다.

[연결·삭제 계약](contract.md) · [검증 범위](validation.md)
