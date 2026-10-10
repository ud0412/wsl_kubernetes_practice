# 03 설명 — CNI는 Pod의 통신을 연결합니다

Pod가 IP를 받고 다른 Pod와 통신하려면 네트워크 구성이 필요합니다. 이 역할을 Cilium CNI가 담당합니다. Kubernetes Service로 통신할 때 사용하는 kube-proxy는 유지합니다.

실습 자원을 줄이기 위해 Hubble과 Cilium Gateway 기능은 켜지 않습니다. HTTP Gateway는 다음 장의 별도 Envoy Gateway가 담당합니다.

Helm chart는 여러 Kubernetes 설치 파일을 묶은 패키지입니다. values.yaml은 그 패키지에서 조정할 설정입니다. 설치 후에는 이름이 보이는 것보다 노드와 Cilium이 Ready인지, 실제 통신이 되는지 확인해야 합니다.


[목차](../README.md) · [다음](02-practice.md)
