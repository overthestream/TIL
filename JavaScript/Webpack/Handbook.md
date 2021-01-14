# [웹팩 핸드북 : 웹팩을 가장 쉽고 빠르게 배우는 방법](https://joshua1988.github.io/webpack-guide/motivation/problem-to-solve.html#웹팩으로-해결하려는-문제)

<hr/>

## WebPack

### 웹팩이란?

최신 프론트엔드 프레임워크에서 많이 사용되는 **Module Bundler**

> 모듈 번들러 : 웹 애플리케이션을 구성하는 *HTML, CSS, JS, Image*를 모두 각각의 모듈로 보고 이를 조합해서 하나의 결과물로 만드는 도구

### 모듈이란?

프로그래밍 관점에서 특정 기능을 가지는 작은 코드 단위

```javascript
// math.js
function sum(a, b) {
	return a + b
}

function substract(a, b) {
	return a - b
}

const pi = 3.14

export { sum, substract, pi }
```

이 `math.js`는 3가지 기능을 가진 모듈

비슷한 기능을 하나의 의미있는 파일로 관리하면 모듈이 됨

> 웹팩의 모듈은 프로그램으로서의 모듈에 국한되지 않고 **웹 애플리케이션을 구성하는 모든 자원** 을 의미함

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

- 자바스크립트 변수 유효 범위
- 브라우저별 HTTP 요청 숫자 제약
- 사용하지 않는 코드 관리
- Dynamic Loading & Lazy Loading 미지원

1. 자바스크립트 변수 유효 범위 문제
   var -> let, const, ES6의 Modules 문법, 웹팩의 모듈 번들링으로 해결

2. 브라우저별 HTTP 요청 숫자의 제약
   HTTP 요청 회수를 줄이는 것이 웹 애플리케이션의 성능을 높이고, 사용자가 사이트를 조작하는 시간을 앞당김
   웹팩으로 이 요청 횟수를 파악 가능

3. Dynamic Loading & Lazy Loading 미지원
   웹팩의 **Code Splitting** 을 이용해 원하는 모듈을 원하는 타이밍에 로딩 가능

<hr/>

## Node.js & NPM

웹팩 사용을 위해 설치되어 있어야 함

### Node.js

브라우저 밖에서 자바스크립트를 실행할 수 있는 환경
터미널의 "node" 명령어 사용

### NPM

NPM=(Node Package Manager) 자바스크립트 라이브러리 설치 및 관리용 패키지 매니저

```sh
npm init -y
```

```json
//package.json
{
	"name": "demo",
	"version": "1.0.0",
	"description": "",
	"main": "index.js",
	"scripts": {
		"test": "echo \"Error: no test specified\" && exit 1"
	},
	"keywords": [],
	"author": "",
	"license": "ISC"
}
```

scripts, dependencies, devDependencies 등이 주로 사용됨

#### 명령어

#### 설치

```sh
npm install(i) [library] (--save-prod || 생략 : dependencies에 등록 / --save-dev || 생략 + -D : devDependencies에 등록)||(gulp --global(-g) - global->/usr/local/lib/node_modules)
```

dependencies : 빌드에 포함
devDependencies : 개발 시에만 쓰고, 빌드 시에는 빠지게 됨

#### 커스텀

scripts에 정의해두면 사용 가능
예를 들어

```json
{
  "scripts" : {
    "hello":"echo hi"
  }
}
```

``` sh
npm run hello (커스텀 명령어)
```

<hr/>

## concepts
빌드를 위한 4가지 주요 속성
- entry
- output
- loader
- plugin
### Entry
웹팩에서 웹 자원을 변환하기 위한 최초 진입점, 자바스크립트 파일 경로 

보통 index 파일 

웹 애플리케이션의 전반적인 구조와 내용이 담겨 있어야 함 
> 전반적인 import 구조 등이 포함 → dependency graph

멀티 페이지 애플리캐이션은 엔트리 포인트가 여러 개가 될 수 있음 
### Output
 웹팩의 결과물에 대한 정보를 입력하는 속성

웹팩을 돌린 후 결과물의 파일 경로 
filename, path 속성을 정의해야 함 

filename 속성에 entry 명, 모듈 ID, 해시 값 등을 포함하는 옵션을 추가하는 것도 가능 
### Loader 
웹팩이 웹 애플리케이션을 해석할 때 자바스크립트 파일이 아닌 웹 자원(HTML, CSS, Image, Font 등)을 변환하도록 돕는 속성 

module 이라는 이름을 사용

오른쪽에서 왼쪽 순으로 적용됨
 
예시
``` js
module: {
  rules: [
    {
      test: /\.css$/,
      use: [
        { loader: 'style-loader' },
        {
          loader: 'css-loader',
          options: { modules: true }
        },
        { loader: 'sass-loader' }
      ]
    }
  ]
}
```


사용 시마다 구글링 해서 .. 복잡하다
### Plugin
웹팩의 기본적인 동작에 추가적인 기능을 제공 

결과물의 형태를 바꾸는 역할 

생성자 함수로 생성한 객체 인스턴스들만 추가 가능 
``` js
// webpack.config.js
var webpack = require('webpack');
var HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  plugins: [
    new HtmlWebpackPlugin(),
    new webpack.ProgressPlugin()
  ]
}
```

> 위 4개 이외에도 reslove, devServer, devtool 등 알면 좋음 

