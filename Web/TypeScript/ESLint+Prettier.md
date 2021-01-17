# ESLint + Prettier(Airbnb) 적용하기 with Typescript React(CRA) + Mobx

1. Git Remote Repository 연결

```sh
mkdir todomobx
cd todomobx
git init
git remote add origin https://github.com/overthestream/todo-react-ts-mobx
git pull origin main
git checkout main
```

2. create react-app

```sh
yarn create react-app todomobx --template typescript
```

3. styled-component + highlighter

```sh
cd todomobx
npm i -D @types/styled-components # 스타일드 컴포넌트 + 타입 정의
npm install --save-dev typescript-styled-plugin # 스타일드 컴포넌트 하이라이터
```

그리고,
**tsconfig.json**

```json
{
	"compilerOptions": {
		"plugins": [
			{
				"name": "typescript-styled-plugin"
			}
		]
	}
}
```

4. Extension 설치
   ESLint, Prettier, vscode-styled-components

5. Dependencies 설치

```sh
yarn add -D @typescript-eslint/eslint-plugin @typescript-eslint/parser eslint-config-airbnb-typescript eslint-plugin-jest # ESLint
npx install-peerdeps --dev eslint-config-airbnb # Airbnb
yarn add -D prettier eslint-config-prettier eslint-plugin-prettier # Prettier
```

6. Config
   **eslintrc.js**

```js
module.exports = {
	extends: [
		'airbnb-typescript',
		'airbnb/hooks',
		'plugin:@typescript-eslint/recommended',
		'plugin:jest/recommended',
		'prettier',
		'prettier/react',
		'prettier/@typescript-eslint',
		'plugin:prettier/recommended',
	],
	plugins: ['react', '@typescript-eslint', 'jest'],
	env: {
		browser: true,
		es6: true,
		jest: true,
	},
	globals: {
		Atomics: 'readonly',
		SharedArrayBuffer: 'readonly',
	},
	parser: '@typescript-eslint/parser',
	parserOptions: {
		ecmaFeatures: {
			jsx: true,
		},
		ecmaVersion: 2018,
		sourceType: 'module',
		project: './tsconfig.json',
	},
	rules: {
		'linebreak-style': 'off',
		'prettier/prettier': [
			'error',
			{
				endOfLine: 'auto',
				singleQuote: true,
				semi: true,
				useTabs: false,
				tabWidth: 2,
				printWidth: 80,
				arrowParens: 'always',
			},
		],
	},
};
```

**package.json**

```json
"scripts": {
  "format": "prettier --write src/**/*.ts{,x}",
  "lint": "tsc --noEmit && eslint src/**/*.ts{,x}"
}
```

7. Mobx

```sh
yarn add mobx
```

**tsconfig.json**

```json
"compilerOptions": {
  "useDefineForClassFields": true
}
```
