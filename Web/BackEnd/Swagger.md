# Swagger

## Swagger가 뭐야 ?

백엔드와 프론트엔드 사이의 API를 관리하는 도구.

## Swagger.io

사이트에서 코드로 API documentation 가능

## Node.js에 적용하기

### swagger project create

```sh
$ yarn global add swagger
$ swagger project create swagger
?Framework?
 > express
$ swagger project start
```

### 기존 프로젝트에 적용하기

스웨거 UI가 있는 [레포지토리](https://github.com/swagger-api/swagger-ui)에서 그대로 다운받아서, dist 폴더 안의 파일을 기존 프로젝트에 연결

이름은 보통 docs로 많이 사용

localhost:[port번호]/docs/index.html 에 API가 있어용 (기본: petstore)

docs 안에 swagger.yaml에 api documentation 하기.

index 파일에서 url 수정 시 기본 경로가 아니라 docs로 이동

url -> http://localhost:3000/swagger.yaml

이거 안되더라.

---

다른 방법.

```sh
$ yarn add swagger-ui
```

node_modules/swagger-ui/dist에 html 저장.

이것을 express 라우팅에 추가

```js
app.use('/swagger-ui', express.static(path.join(__dirname, './node_modules/swagger-ui/dist')));
```

http://localhost:3000/swagger-ui

이거도 안되네...

---

```sh
$ yarn add swagger-ui-express swagger-jsdoc
```

**app.js**

```js
var bodyParser = require('body-parser');
var swaggerJsdoc = require('swagger-jsdoc');
var swaggerUi = require('swagger-ui-express');
const options = {
	definition: {
		openapi: '3.0.0',
		info: {
			title: 'LogRocket Express API with Swagger',
			version: '0.1.0',
			description:
				'This is a simple CRUD API application made with Express and documented with Swagger',
			license: {
				name: 'MIT',
				url: 'https://spdx.org/licenses/MIT.html',
			},
			contact: {
				name: 'LogRocket',
				url: 'https://logrocket.com',
				email: 'info@email.com',
			},
		},
		servers: [
			{
				url: 'http://localhost:3000/books',
			},
		],
	},
	apis: ['./routes/books.js'],
};

const specs = swaggerJsdoc(options);
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(specs));
```
