# 04 설명 — 규칙과 실제 요청 전달을 구분하기

Gateway API는 어디로 요청을 보낼지 표현하는 Kubernetes 리소스입니다. CRD는 Kubernetes가 그 리소스를 이해하게 만드는 정의입니다. 정의만 설치하면 요청이 전달되는 것은 아닙니다.

Envoy Gateway controller는 규칙을 읽고 Envoy Proxy를 준비합니다. 실제 브라우저 요청은 이 Proxy가 받습니다.

GatewayClass는 구현 선택, Gateway는 요청을 받을 입구, HTTPRoute는 경로별 목적지입니다. 이번에는 입구까지 준비하고 Grafana·샘플 목적지는 후속 과정에서 연결합니다.

Envoy chart가 Gateway API CRD를 함께 설치하므로 별도 CRD bundle을 중복 설치하지 않습니다. controller Service가 아닌 Envoy Proxy Service로 접속해야 합니다.


[목차](../README.md) · [다음](02-practice.md)
