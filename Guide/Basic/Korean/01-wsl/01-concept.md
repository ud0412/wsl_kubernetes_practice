# 01 설명 — WSL CPU·메모리와 도구의 역할

Kubernetes와 관측 도구는 WSL의 CPU·메모리를 사용합니다. PC RAM 32GB 이상에서 WSL에 12~16GB, 권장 16GB를 설정합니다. CPU는 PC의 논리 프로세서 수에 맞춰 4~6개 정도부터 시작합니다.

WSL 설정 앱에서 memory·processor 값을 변경할 수 있습니다. `.wslconfig`는 기본적으로 없는 파일이므로 파일을 찾는 것부터 시작하지 않습니다. 앱을 기본 경로로 사용하고 파일 방식은 앱이 없는 경우의 보충 경로입니다.

| 도구 | 역할 |
|---|---|
| Docker Engine | kind 노드 컨테이너 실행 |
| kind | 가벼운 로컬 Kubernetes 생성 |
| kubectl | Kubernetes 조회·변경 |
| Helm | 여러 Kubernetes 설정을 묶은 chart 설치 |
| Python | 설정 파일과 관리 상태 준비 |

전체 부하와 실습 안정성을 우선하여 WSL 내부 Docker Engine을 기본으로 합니다. Docker Desktop daemon과 혼용하지 않습니다. Podman은 [보충 설명](../appendix-podman.md)에서 다룹니다.


[목차](../README.md) · [다음](02-practice.md)
