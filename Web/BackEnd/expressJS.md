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

### HTTP 메소드 처리

1. 첫 번째 파라미터: 문자열 형식으로 URL 패턴에 대한 정규 표현식을 받음 (이게 request인듯?)

2. 두 번째 파라미터: request handler - req, res 최소 두 개의 인자를 받아줘야 함

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

HTTP 상태 코드임(404 그런거)

## 라우팅

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

METHOD 목록 : get, post, put, head, delete, options, trace, copy, lock, mkcol, move, purge, propfind, proppatch, unlock, report, mkactivity, checkout, merge, m-search, notify, subscribe, unsubscribe, patch, search 및 connect

### [HTTP](https://developer.mozilla.org/ko/docs/Web/HTTP/Messages)

서버와 클라이언트 간에 데이터가 교환되는 방식

1. 시작 줄(start-line)에는 요청 또는 그에 대한 반응 (항상 한 줄)
2. 옵션: HTTP 헤더 세트(요청또는 메시지에 대한 설명)
3. 요청에 대한 모든 메타 데이터가 전송되었음을 알리는 blank line
4. 요청과 관련된 내용(HTML 등)이 옵션으로 들어가거나 응답과 관련된 문서가 들어감

시작 줄 + 헤더 -> 요청 head
HTTP 메시지의 페이로드 -> body

#### HTTP 요청

##### 시작 줄(start-line)

1. HTTP 메소드
   - GET: 리소스를 클라이언트에게 제공해달라
   - POST: 데이터를 서버에 저장해라
   - PUT: POST와 유사, 헤더 이외에 메시지(데이터)가 함꼐 전송
   - DELETE: 서버의 데이터 삭제
2. URL
   - origin: 끝에 ?와 함꼐 쿼리 문자열이 붙는 절대 경로
   - absolute: 완전한 URL
   - authority: 도메인 이름 및 옵션 포트(: ...)로 이루어진 URL의 authority component
   - asterisk: \* 하나로 서버 전체를 나타냄
3. HTTP 버전

### 라우트 핸들러

next 사용 시 2개 이상의 콜백 함수 처리도 가능

```js
app.get(
	'/example/b',
	function (req, res, next) {
		console.log('the response will be sent by the next function ...');
		next();
	},
	function (req, res) {
		res.send('Hello from B!');
	}
);
```

> 배열로 줘도 된다

### 응답 메소드

res.download() : 파일 다운로드되도록 프롬프트
res.end(): 응답 프로세스 종료
res.json(): JSON 응답 전송
res.jsonp(): JSONP 지원을 통해 JSON 응답 전송
res.redirect(): 요청의 경로 재지정
res.render(): 보기 템플릿 렌더링
res.send(): 다양한 유형의 응답 전송
res.sendFile(): 파일을 옥텟 스트림의 형태로 전송
res.sendStatus: 응답 상태 코드를 설정한 후 해당 코드를 문자열로 표현한 내용을 본문으로 전송

### app.route()

라우트 경로에 대하여 체인 가능한 라우트 핸들러 작성이 가능
(한 경로에 여러 메소드 작성)

**ex**

```js
app
	.route('/book')
	.get(function (req, res) {
		res.send('Get a random book');
	})
	.post(function (req, res) {
		res.send('Add a book');
	})
	.put(function (req, res) {
		res.send('Update the book');
	});
```

### express.Router

모듈 식의 핸들러 작성 가능
**birds.js**

```js
const express = require('express');
const router = express.Router();

router.use(function timeLog(req, res, next) {
	console.log('Time: ', Date.now());
	next();
});

// home route
router.get('/', function (req, res) {
	res.send('Birds home page');
});

// about route
router.get('/about', function (req, res) {
	res.send('About');
});
module.export = router;
```

**App.js**

```js
const birds = require('./birds');
app.use('/birds', birds);
```

## 미들웨어

**미들웨어 함수**는 요청 오브젝트(req), 응답 오브젝트(res), 다음 미들웨어 함수(next)를 인자로 받음

### 기능

- 모든 코드 실행
- 요청 및 응답 오브젝트에 대한 변경
- 요청-응답 주기를 종료
- 스택 내의 그 다음 미들웨어 호출
  현재의 미들웨어 함수가 요청-응답 주기를 종료하지 않는다면 next를 호출하여 그 다음 미들웨어 함수에 제어를 전달해야 함.
  그렇지 않으면 해당 요청은 정지된 채로 방치
  **ex**

```js
var express = require('express');
var app = express();

var myLogger = function (req, res, next) {
	console.log('LOGGED');
	next();
};

app.use(myLogger);

app.get('/', function (req, res) {
	res.send('Hello World!');
});
```

이런 식으로 짜면 app이 요청 받을때마다 myLogger가 호출

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

## PostgreSQL과 통합

모듈: pg-promise

```sh
yarn add pg-promise
```

**ex**

```js
var pgp = require('pg-promise')(/*options*/);
var db = pgp('postgres://username:password@host:port/database');

db.one('SELECT $1 AS value', 123)
	.then(function (data) {
		console.log('DATA:', data.value);
	})
	.catch(function (error) {
		console.log('ERROR:', error);
	});
```
