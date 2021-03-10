# react express 연동하기

## 백엔드, 프론트 같이 로컬로 돌리려면 ..

에러가 난다.

간단하게 말하자면

```sh
yarn add cors
```

```js
const cors = require('cors');
app.use(cors());
```

하면 일단은 해결 가능.

## 값 받아오기

컴포넌트가 마운트 될 때 ,

즉 <code>componentDidMount</code> , 또는 <code>useEffect(callback, [])</code> 시 데이터를 서버로부터 받아오도록 한다.

**예시**

```js
useEffect(() => {
	// localhost:3000 에서 서버가 돌아가고 있다
	// /items 에서 get 형식으로, json 형식의 데이터 response로 보내도록 라우팅된 상태
	fetch('http://localhost:3000/items')
		.then((res) => res.json()) // res.json() 으로 데이터를 받아서 콜백 ..
		.then((data) => console.log(data));
}, []);
```

## react에서 express로

### Axios

**REF** https://velog.io/@zofqofhtltm8015/Axios-사용법-서버-통신-해보기

브라우저, Node.js를 위한 Promise API를 활용하는 HTTP 비동기 통신 라이브러리

Ajax와 비슷한 역할

#### 특징

- 운영 환경에 따라 브라우저의 XMLHttpRequest 객체 또는 Node.js의 http api 사용
- Promise(ES6) API 사용
- 요청과 응답 데이터의 변형
- HTTP 요청 취소
- HTTP 요청과 응답을 JSON 형태로 자동 변경

#### 설치 및 사용

```sh
yarn add axios
```

```js
import axios from 'axios';
```

##### GET

```js
axios.get(url, [, config]);
```

위의 예시를 axios로 구현해본다면.

```js
import axios from 'axios';
useEffect(() => {
	// localhost:3000 에서 서버가 돌아가고 있다
	// /items 에서 get 형식으로, json 형식의 데이터 response로 보내도록 라우팅된 상태
	axios
		.get('http://localhost:3000/items')
		.then((res) => res.json()) // res.json() 으로 데이터를 받아서 콜백 ..
		.then((data) => console.log(data));
}, []);
```

##### POST

axios.post("url주소",{
data객체
},[,config])

##### DELETE

    axios.delete(URL,[,config]);

```js
axios.delete("/thisisExample/list/30").then(function(response){
    console.log(response);
      }).catch(function(ex){
      throw new Error(ex)
}
```

##### PUT

    axios.put(url[, data[, config]])
