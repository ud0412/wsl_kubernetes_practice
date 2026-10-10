# 검증 범위

2026-10-10 소스 검사: 계약·보존·삭제 테스트 4개, Markdown 링크·YAML, Bash 구문과 ShellCheck 통과. 사용자 환경에 클러스터를 설치하지 않았습니다.

AI는 WSL 클러스터를 설치하지 않습니다. 소스 검사에서는 YAML 렌더링, 문서 링크, Bash 구문·ShellCheck, 소유권·삭제 경계를 확인합니다. 실제 WSL Settings 앱과 CNI/Gateway 런타임 확인은 실습자가 수행합니다.

실습 확인표:

- [ ] GUI로 CPU·메모리 설정 후 free/nproc 확인
- [ ] 내부 Docker Engine과 고정 도구 버전 확인
- [ ] 노드 생성 직후 예상 NotReady 확인
- [ ] Cilium 설치 후 두 노드 Ready와 DNS/Service 통신
- [ ] Gateway CRD Established, Gateway Accepted/Programmed, Proxy Ready
- [ ] 자동 up과 수동 실습이 같은 기반 환경을 만듦
- [ ] 후속 Observability가 기존 클러스터를 사용함
- [ ] Pod 재시작에서 저장 데이터 유지, destroy에서 전체 데이터 삭제
