# 리액트의 상태 관리 라이브러리

React의 State관리 라이브러리 - Redux vs Mobx

## 용어

Redux : Flux 개념을 바탕으로 한 React에서 현재 가장 많이 사용되는 State 관리 라이브러리, Component와 State를 연결

Mobx : Redux와 또 다른 State관리 라이브러리, 기본적으로 객체 지향 느낌, 보일러플레이트 코드들을 데코레이터(애노테이션) 제공으로 깔끔하게 해결

Store : Global 영역에서 애플리케이션의 state와 비즈니스 로직을 가지고 있는 주체

> State를 Global 영역에서 관리하는 것이 바로 State관리 라이브러리의 사용 목적
>
> Redux에서는 State와 State를 핸들링하는 비즈니스 로직을 가지고 있는 Reducer, Action 등을 포함하는 의미
>
> Mobx에서는 Store는 명확히 State와 비즈니스로직을 포함하는 Class

Observable : Mobx에서 Rerendering 대상이 되는 state 값을 관찰 대상 (observable value)라고 칭하며, @observable 데코레이터로 지정한 State는 관찰 대상으로 지정되고, 그 State는 값이 변경될 때마다 Rerendering 됨

불변성 : state 값을 setState 메소드를 이용해 변경하는것 = 불변성을 유지하는 것

## State 관리 라이브러리 사용 목적 

### 다중 계층 컴포넌트에서 데이터와 메소드 접근의 복잡성 해결 

여러 개의 Component가 조합되어 페이지가 구성될 때 (부모 자식 컴포넌트)Component간 상호작용 즉 데이터(State, Props)와 메소드의 접근이 까다로움
__State를 Global한 영역에서 관리하여 접근이 용이하게 됨__

### 컴포넌트에 집중된 비즈니스 로직의 분리

State관리 라이브러리 없이 개발하면 모든 로직이 Component에만 집중되어 코드를 알아보기가 힘듦. 사용 시 Component는 Controller 역할을 맡게 되어 적절히 분리하여 아키텍쳐를 구성할 수 있음 

## Mobx

### 객체 지향적

class를 객체지향적으로 사용

### 서버 개발자들에게 친숙한 아키텍쳐

Java Spring Framework와 유사한 아키텍쳐 구조

### Decorator

데코레이터를 제공하여 Redux를 사용할 때 React Component와 State를 연결하는 코드가 사라짐

### 캡슐화

Mobx Configuration 설정으로 state는 오직 메소드로만 변경되도록 private하게 관리 가능

### 불변성 유지가 쉬움 

State의 불변성을 유지하기 위해서 다른 코드나 라이브러리르 사용할 필요 없음


## ref

[우아한 형제들 기술 블로그](https://woowabros.github.io/experience/2019/01/02/kimcj-react-mobx.html)
