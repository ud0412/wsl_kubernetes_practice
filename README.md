# WSL Kubernetes Practice — Basic

Windows WSL에서 kind Kubernetes, Cilium CNI, Gateway API와 Envoy Gateway를 직접 준비하는 한국어 기초 과정입니다. **[교본 시작](Guide/Basic/Korean/README.md)**

WSL 설정은 설정 앱을 기본 경로로 안내합니다. [사전 준비](Guide/Basic/Korean/01-wsl/02-practice.md) 후 수동 실습 또는 자동 구축을 선택합니다. AI는 클러스터를 설치하지 않습니다.

```bash
# WSL Bash, 이 저장소 루트. 사전 도구 준비 완료 후
bash scripts/lab.sh up
bash scripts/lab.sh verify
```

완료 후 [Observability Practice Basic](https://github.com/ud0412/observability_practice/tree/master/Guide/Basic/Korean)을 이어서 진행합니다. 두 저장소를 같은 부모 폴더에 clone합니다. 후속 과정은 이 클러스터를 사용하고 자체 클러스터를 만들지 않습니다.

실습 환경 이름은 `observability-lab`, 노드는 control-plane·worker 두 개입니다. 이 이름은 후속 과정과 기존 실습 저장 경로의 호환성을 위해 유지합니다. 메모리는 WSL 12~16GB, PC RAM 32GB 이상을 기준으로 합니다.

`bash scripts/lab.sh destroy`는 후속 Observability와 수동 샘플을 포함하여 클러스터와 모든 관리 실습 데이터를 제거합니다. [연결·삭제 계약](Guide/Basic/Korean/contract.md)을 확인하세요.

[고정 버전](config/versions.env) · [Podman 선택 배경](Guide/Basic/Korean/appendix-podman.md) · [검증 범위](Guide/Basic/Korean/validation.md)
