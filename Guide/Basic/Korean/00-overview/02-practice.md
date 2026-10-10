# 00 실습 — 실행 위치 확인

Windows Terminal에서 PowerShell 탭과 Ubuntu 탭을 구분합니다. `wsl --...` 명령은 PowerShell에서, `kubectl`, `docker`, `helm` 명령은 Ubuntu Bash에서 실행합니다.

Windows PowerShell:

```powershell
wsl --list --verbose
```

Ubuntu 배포판의 VERSION이 2인지 확인합니다. 아직 설치하지 않았다면 다음 장에서 설치합니다.

WSL Ubuntu:

```bash
uname -s
pwd
```

Linux와 현재 폴더가 보입니다. 이 교본의 저장소 경로는 `~/practice/wsl_kubernetes_practice`를 기준으로 합니다.


[목차](../README.md) · [다음](../01-wsl/01-concept.md)
