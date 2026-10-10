# 01 실습 — WSL 설정 앱과 도구 준비

## 1. Windows PowerShell에서 WSL 준비

처음 설치할 때 PowerShell을 관리자 권한으로 열어 실행합니다.

```powershell
wsl --install -d Ubuntu-24.04
wsl --update
wsl --list --verbose
```

재부팅을 요청하면 완료한 뒤 Ubuntu를 실행해 Linux 사용자 이름과 비밀번호를 만듭니다. 이미 설치했다면 중복 설치하지 않고 배포판과 VERSION 2를 확인합니다.

## 2. WSL 설정 앱으로 자원 설정

1. Windows **시작 메뉴**에서 `WSL Settings` 또는 `WSL 설정`을 검색하여 실행합니다.
2. 왼쪽 **Memory and Processor**(메모리·프로세서 관련 메뉴)를 엽니다.
3. **Memory Size**에서 최대 메모리를 `16GB`로 설정합니다. 단위가 MB인 입력칸이면 `16384`입니다. PC 여유에 따라 `12GB`/`12288MB`도 사용할 수 있습니다.
4. 프로세서 수 항목에서 4~6개를 설정합니다. PC 논리 프로세서 수보다 많이 입력하지 않습니다.
5. 앱의 저장·적용 동작을 완료합니다. 앱 버전에 따라 변경 즉시 저장되거나 재시작 안내가 표시됩니다.

[Microsoft의 실제 설정 앱 화면](https://learn.microsoft.com/en-us/windows/wsl/media/wsl-settings.png)을 참고할 수 있습니다. 사용 중인 앱이 별도 `WSL Config` 앱이면 같은 메모리·CPU 항목을 설정하되 위 메뉴 이름이 동일하다고 가정하지 않습니다.

설정 적용을 위해 실행 중인 WSL 작업을 저장하고 PowerShell에서 종료합니다. 모든 WSL 배포판이 종료됩니다.

```powershell
wsl --shutdown
```

Ubuntu를 다시 열어 확인합니다.

```bash
free -h
nproc
```

메모리 값은 예약 영역 때문에 정확히 16.0GiB로 나오지 않을 수 있습니다. 대략 설정한 크기와 지정한 CPU 수인지 확인합니다.

앱이 없을 때만 보충 방법으로 Windows 사용자 폴더의 `.wslconfig`를 새로 만듭니다. 기존 파일이 있으면 아래 설정을 병합합니다.

```ini
[wsl2]
memory=16GB
processors=6
swap=4GB
```

## 3. WSL에서 systemd와 기본 도구 확인

```bash
ps -p 1 -o comm=
sudo apt update
sudo apt install -y ca-certificates curl git python3 python3-venv nano
```

첫 결과가 systemd면 다음으로 진행합니다. 아니면 `sudo nano /etc/wsl.conf`로 기존 설정을 열고 `[boot]` 아래에 `systemd=true`를 추가합니다. Ctrl+O, Enter로 저장하고 Ctrl+X로 종료합니다. Windows PowerShell의 `wsl --shutdown` 후 Ubuntu를 다시 엽니다.

## 4. WSL 내부 Docker Engine 설치

WSL Ubuntu Bash에서 순서대로 실행합니다.

```bash
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
. /etc/os-release
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $VERSION_CODENAME stable" | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin
sudo systemctl enable --now docker
sudo usermod -aG docker "$USER"
newgrp docker
docker info
```

docker 그룹 변경을 새 셸에 적용합니다. Docker 그룹은 daemon을 통한 호스트 관리 권한을 갖습니다. `docker info`의 운영체제가 Docker Desktop이면 해당 Ubuntu의 Desktop integration을 해제하고 내부 Engine에 연결되는지 확인합니다.

## 5. 저장소와 버전 고정 도구 준비

```bash
mkdir -p ~/practice
cd ~/practice
git clone https://github.com/ud0412/wsl_kubernetes_practice.git
cd wsl_kubernetes_practice
python3 -m venv .venv
.venv/bin/pip install -r requirements-tools.txt
export PATH="$HOME/.local/bin:$PATH"
bash scripts/install-tools.sh
bash scripts/preflight.sh
```

정상 결과: Prerequisites OK, 아직 클러스터는 생성되지 않았습니다. `~/.local/bin`을 새 터미널에서도 사용하려면 `~/.bashrc`에 `export PATH="$HOME/.local/bin:$PATH"`를 추가하고 새 터미널을 엽니다.

```bash
kind version
kubectl version --client
helm version
df -h ~
```

kind 0.33.0, kubectl 1.36.4, Helm 4.3.0을 확인합니다. Helm의 KubeClientVersion 1.37은 Helm이 빌드에 사용한 클라이언트 라이브러리입니다. 실제 클러스터 버전과 같은 값일 필요는 없습니다. Linux 저장 공간 40GB 이상을 준비합니다.

[WSL 설정 공식 안내](https://learn.microsoft.com/en-us/windows/wsl/wsl-config) · [Docker Ubuntu 설치](https://docs.docker.com/engine/install/ubuntu/)


[목차](../README.md) · [다음](../02-kubernetes/01-concept.md)
