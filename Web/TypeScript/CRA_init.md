# CRA TS ESLint Prettier Airbnb init

```sh
npm i cra-template-ts-prettier-eslint-airbnb
npx create-react-app myapp --template ts-prettier-eslint-airbnb
```

**package.json**

```json
{
	"scripts": {
		"build": "react-scripts build",
		"eject": "react-scripts eject",
		"lint": "eslint src/ --ext .js,.jsx,.ts,.tsx",
		"lint:fix": "npm run lint -- --fix",
		"start": "react-scripts start",
		"test": "react-scripts test"
	},
	"dependencies": {
		"react": "^17.0.1",
		"react-dom": "^17.0.1"
	},
	"devDependencies": {
		"@testing-library/jest-dom": "^5.11.9",
		"@testing-library/react": "^11.2.3",
		"@testing-library/user-event": "^12.6.0",
		"@types/jest": "^26.0.20",
		"@types/react": "^17.0.0",
		"@types/react-dom": "^17.0.0",
		"@typescript-eslint/eslint-plugin": "^4.14.0",
		"@typescript-eslint/parser": "^4.14.0",
		"eslint": "^7.18.0",
		"eslint-config-airbnb-typescript": "^12.0.0",
		"eslint-config-prettier": "^7.2.0",
		"eslint-plugin-import": "^2.22.1",
		"eslint-plugin-import-helpers": "^1.1.0",
		"eslint-plugin-jsx-a11y": "^6.4.1",
		"eslint-plugin-prettier": "^3.3.1",
		"eslint-plugin-react": "^7.22.0",
		"eslint-plugin-react-hooks": "^4.2.0",
		"node-sass": "^4.14.1",
		"prettier": "^2.2.1",
		"react-scripts": "^4.0.1",
		"typescript": "4.1.3"
	}
}
```

```sh
yarn add styled-components
npm i -D @types/styled-components # 스타일드 컴포넌트 + 타입 정의
npm install --save-dev typescript-styled-plugin # 스타일드 컴포넌트 하이라이터
```

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
```

Mobx

```sh
yarn add mobx mobx-react
```

**tsconfig.json**

```json
"compilerOptions": {
  "useDefineForClassFields": true
}
```
