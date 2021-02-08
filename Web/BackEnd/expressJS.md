# express.js

## ref

https://expressjs.com/ko/

## start

```sh
mkdir tutorial
cd tutorial

yarn init
.
.
.

yarn add express
```

## Hello World!

```js
const express = require('express'); // import express as express 이런 느낌?
const app = express(); // app은 express 의 instance, 즉 express app을 만들어 app에 저장
const port = 3000; // port: 3000 에서 구동되는 앱

app.get('/', (req, res) => {
	res.send('Hello World!');
});

app.listen(port, () => {
	console.log(`Example app listening at http://localhost:${port}`);
});
```

### require('express')

express.js를 import 하는 느낌인듯?

### get()

1. 첫 번째 파라미터: 문자열 형식으로 URL 패턴에 대한 정규 표현식을 받음 (이게 request인듯?)

2. 두 번째 파라미터: request handler - req, res 최소 두 개의 인자를 받아줘야 함

### send

응답으로 보낸걸 HTML로 보여주는 듯.

## 서버에 뭔가 담아서 요청하기

```js
const express = require('express'); // import express as express 이런 느낌?
const app = express(); // app은 express 의 instance, 즉 express app을 만들어 app에 저장
const port = 3000; // port: 3000 에서 구동되는 앱

app.get('/name/:user_name', function (req, res) {
	res.status(200);
	res.set('Content-type', 'text/html');
	res.send('<html><body>' + '<h1>Hello ' + req.params.user_name + '</h1>' + '</body></html>');
});

app.listen(port, () => {
	console.log(`Example app listening at http://localhost:${port}`);
});
```

### status

HTTP 상태 코드임

## 기본 라우팅

라우팅(routing): URL 및 특정한 HTTP 요청 메소드(GET, POST 등)인 특정 엔드포인트에 대한 클라이언트 요청에 애플리케이션이 응답하는 방법을 결정하는 것

각 라우트(route)는 하나 이상의 핸들러 함수를 가질 수 있으며, 이러한 함수는 라우트가 일치할 때 실행됨

라우트의 정의

```js
app.METHOD(PATH, HANDLER);
```

- app: express의 인스턴스
- METHOD: HTTP 요청 메소드 - GET, PUT, POST, DELETE
- PATH: 서버에서의 경로
- HANDLER: 라우트가 일치할 때 실행되는 함수

## Express에서 정적 파일 제공하기

이미지, css, js 등 정적 파일을 제공하려면 Express의 미들웨어 함수인 express.static 사용

디렉토리 이름을 함수에 전달하여 제공 시작

```js
app.use(express.static('public'));
```

-> public 디렉토리의 정적 파일 사용

```
http://localhost:3000/images/kitten.jpg
```

이런 식으로 로드 가능

### import as

```js
app.use('/static', express.static('public'));
```
public 대신 static 경로로 접근 가능