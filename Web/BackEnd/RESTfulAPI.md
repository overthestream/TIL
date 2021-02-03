# RESTful API

## [REST?](https://ko.wikipedia.org/wiki/REST)

REST = Representational State Transfer

WWW와 같은 분산 하이퍼미디어 시스템을 위한 소프트웨어 아키텍쳐의 한 형식

네트워크 아키텍처 원리의 모음

> 네트워크 아키텍처: 자원을 정의하고 자원에 대한 주소를 지정하는 방법 전반

간단한 의미로: 웹 상의 자료를 HTTP위에서 SOAP나 쿠키를 통한 세션 트래킹 같은 별도의 전송 계층 없이 전송하기 위한 아주 간단한 인터페이스

### 원리

#### REST 아키텍처의 6가지 조건

- 인터페이스 일관성(Uniform Interface): 일관적인 인터페이스로 분리 + HTTP 통해 관리
- 무상태(Stateless): 각 요청 간 클라이언트의 context는 서버에 저장 x
- 캐리 처리 가능(Cacheable): WWW에서와 같이 클라이언트는 응답을 캐싱할 수 있음(상호작용 간소화)
- 계층화(Layered System): 클라이언트는 서버 연결 계층 구조을 알 수 없음(직접인지, 중간 서버가 있는지)
- Code on demand(optional): 자바 애플릿이나 자바스크립트의 제공을 통해 서버가 클라이언트가 실행시킬 수 잇는 로직을 전송 가능
- 클라이언트/서버 구조: 아키텍처를 단순화시키고 작은 단위로 분리(decouple)함으로써 클라이언트~서버의 각 파트가 독립적으로 개선 가능

#### REST 인터페이스의 원칙

##### 자원의 식별

요청 내에 기술된 개별 자원을 식별할 수 있어야 함
자원 그 자체는 클라이언트가 받는 문서와는 개념적으로 분리되어 있음
서버는 데이터베이스 내부의 자료를 직접 전송하는 대신 그것을 HTML, XML, JSON 등으로 전송
즉, DB와 클라이언트의 **분리**

##### 메시지를 통한 리소스의 조작

클라이언트가 어떤 자원을 지칭하는 메시지와 특정 메타 데이터를 가지고 있으면 그것으로 서버 상의 자원을 변경, 삭제 가능

##### 자기서술적 메시지(Self-descriptiveness)

각 메시지는 자신을 어떻게 처리해야 할지에 대한 정보도 포함해야 함

##### 애플리케이션의 상태에 대한 엔진으로서 하이퍼미디어

클라이언트가 관련 자원에 접근하길 원한다면 리턴되는 지시자에서 구별가능해야 함

#### REST의 주요한 목표

- 구성 요소 상호작용의 규모 확장성(scalability of component interactions)
- 인터페이스의 범용성(Generality of interfaces)
- 구성 요소의 독립적인 배포(Independent deployment of components)
- 중간적 구성 요소를 이용해 응답 지연 감소, 보안 강화, 레거시 시스템 인캡슐레이션(Intermediary components to reduce latency, enforce security and encapsulate legacy systems)

## [RESTful API?](https://www.redhat.com/ko/topics/api/what-is-a-rest-api)

REST 아키텍처의 제약 조건을 준수하는 API

> **API가 뭔데요**
> 애플리케이션 소프트웨어를 구축하고 통합하는 정의 및 프로토콜 세트
> 정보 제공자와 사용자 간의 계약, 소비자에게 필요한 콘텐츠(request) + 생산자에게 필요한 콘텐츠(response)
> 즉 유저, 클라이언트, 서버, 서버 속 리소스 사이의 조정자
>
> > ex : 날씨 서비스용 API에서, 사용자는 위치를 제공(요청), 생산자는 날씨를 응답으로 답함

RESTful API를 통해 요청이 수행될 때 이것은 리소스 상태에 대한 표현을 요청자에게 전송

> 여기서 표현의 형식은 HTTP, JSON, HTML, XLT, XML 등

- 위의 6가지 REST 제한 조건 만족

### 구성

- 자원: RESOURCE - URI
> **URI는 뭔데요**
> 통합 자원 식별자, Uniform Resource Identifier
> 인터넷에 있는 자원을 나타내는 유일한 주소, 인터넷에서 요구되는 기본 조건으로서 인터넷 프로토콜에 붙어다님
> URL등의 상위 개념
- 행위: VERB - HTTP METHOD
- 표현: Representation

### 디자인

1. URI는 정보의 자원 표현해야 함 
2. 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현

2. django로는 어떻게 RESTful API를 만들 수 있는가
   djangoRESTframework
3. 데이터베이스를 어떻게 짤 것인가
   관계형 데이터베이스 / 비관계형 데이터베이스
   mysql, postgresql, mariadb
   mongodb

4. API Builder

5. 내 부분에서 서버와의 응답을 할만한 것 ?
