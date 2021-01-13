# [웹팩 핸드북 : 웹팩을 가장 쉽고 빠르게 배우는 방법](https://joshua1988.github.io/webpack-guide/motivation/problem-to-solve.html#웹팩으로-해결하려는-문제)

<hr/>

## WebPack

### 웹팩이란?
최신 프론트엔드 프레임워크에서 많이 사용되는 __Module Bundler__
> 모듈 번들러 : 웹 애플리케이션을 구성하는 _HTML, CSS, JS, Image_를 모두 각각의 모듈로 보고 이를 조합해서 하나의 결과물로 만드는 도구

### 모듈이란?
프로그래밍 관점에서 특정 기능을 가지는 작은 코드 단위

```javascript
// math.js
function sum(a, b) {
  return a + b;
}

function substract(a, b) {
  return a - b;
}

  const pi = 3.14;

export { sum, substract, pi }
```

이 ```math.js```는 3가지 기능을 가진 모듈

비슷한 기능을 하나의 의미있는 파일로 관리하면 모듈이 됨

> 웹팩의 모듈은 프로그램으로서의 모듈에 국한되지 않고 __웹 애플리케이션을 구성하는 모든 자원__ 을 의미함 

### 모듈 번들링
모듈을 하나의 파일로 병합 및 압축해주는 동작

> 빌드 === 번들링 === 변환

<hr/>

## Motivation

### 필요성

#### 1. 파일 단위 자바스크립트 모듈 관리
변수 유효 범위(var)가 기본적으로 전역이므로, 여러 모듈을 가진 웹 애플리케이션 개발 시 충돌 위험 해소

#### 2. 웹 개발 작업 자동화
변경된 내용 re-rendering, 배포 등에서 모듈 압축 및 변환을 자동화

#### 3. 웹 애플리케이션의 빠른 로딩 및 높은 성능
Lazy Loading의 개념
필요한 자원을 미리 로딩하는 것이 아닌 그 때 그 때 요청하기

### 웹 팩으로 해결하려는 문제
즉, 기존의 문제점은

* 자바스크립트 변수 유효 범위
* 브라우저별 HTTP 요청 숫자 제약
* 사용하지 않는 코드 관리
* Dynamic Loading & Lazy Loading 미지원

1. 자바스크립트 변수 유효 범위 문제
var -> let, const, ES6의 Modules 문법, 웹팩의 모듈 번들링으로 해결

2. 브라우저별 HTTP 요청 숫자의 제약
HTTP 요청 회수를 줄이는 것이 웹 애플리케이션의 성능을 높이고, 사용자가 사이트를 조작하는 시간을 앞당김
웹팩으로 이 요청 횟수를 파악 가능 

3. Dynamic Loading & Lazy Loading 미지원
웹팩의 __Code Splitting__ 을 이용해 원하는 모듈을 원하는 타이밍에 로딩 가능 

<hr/>

## Node.js & NPM