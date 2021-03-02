# Mocha

Node.js의 테스트 툴

테스트 코드를 구동시켜주는 테스트러너

테스트 코드는 test suite와 test로 구분할 수 있다.

- test suite: 테스트를 모아놓은 하나의 환경, <code>describe()</code>
- test: 실제 테스트를 수행하는 코드, <code>it()</code>

예를 들어, User API에 대한 테스트 코드는 api/users/user.spec.js에 작성

## 모카 테스트 코드의 구성

<code>describe()</code>함수의 첫 파라미터로 테스트 수트의 설명을 문자열로 넣고, 두번째 파라미터로 함수를 입력

비동기 로직의 콜백 형식으로 넣는 것. 그 안에 <code>it()</code> 함수로 실제 테스트 코드를 작성

예시

```js
describe('GET /users', () => {
	it('should return 200 status code', () => {
		console.log('test 1');
	});
});
```

**import 같은 것 싹다 필요 없다**

### should

assert 모듈을 예로,

예를 들어 <code>equal()</code>는 두 파라미터가 같으면 ok, 다르다면 throw error

테스트에서는 should 모듈을 사용하라고 함

```sh
yarn add -D should
```

```js
const assert = require('assert');

describe('GET /users', () => {
	it('should return 200 status code', () => {
		assert.equal(true, false);
	});
});

===

const should = require ('should')

describe('GET /users', () => {
	it('should return 200 status code', () => {
    (true).should.be.equal(true);
  });
});
```

### supertest

```sh
yarn add -D supertest
```

api 테스트가 가능하게 해주는 노드 패키지

express 객체를 가져와야 함

**ex**

```js
const request = require('supertest');
const app = require('../../app');

describe('GET /users', () => {
	it('should return 200 status code', (done) => {
		request(app)
			.get('/users')
			.expect(200)
			.end((err, res) => {
				console.log(res);
				if (err) throw err;
				done();
			});
	});
});
```

## 돌리는 법

```sh
$ node_modules/.bin/mocha spec.js경로
```

-> 당연히 <code>package.json</code>에 script를 추가하면 편하겠죠?

## ES6 문법 사용하기

<code>-r ts-node/register</code>를 붙여준당

```sh
yarn test -r ts-node/register
```

이런 st
