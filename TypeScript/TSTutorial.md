# 타입스크립트 배워보기 
## 타입스크립트란 ?
TypeScript는 자바스크립트의 슈퍼셋인 오픈소스 프로그래밍 언어이다.
> 자바스크립트와 달리 정적 타입을 명시할 수 있음. 
> 변수나 함수의 목적을 더욱 명확하게 전달할 수 있다. 

즉, 자바스크립트 확장판 같은 느낌, 자바스크립트 엔진으로 큰 애플리케이션을 개발할 수 있음.

자바스크립트 프로그램이 타입스크립트 프로그램으로도 동작한다.

타입스크립트에서 자신이 원하는 타입을 정의하고 프로그래밍을 하면 자바스크립트로 컴파일되어 실행이 가능하다.

자바 스크립트 사용 전 있을만한 타입 에러를 미리 잡는 것.

<hr/>

## 개발환경 만들기
타입스크립트 컴파일러 (타입스크립트→자바스크립트)
``` sh 
npm install -g typescript
```

<hr/>

## 문법

### 타입 선언하기 
변수 선언 시 뒤에 타입을 선언 
##### 예시
``` ts
const isDone:boolean = true
const message:string = 'hello world'
const numbers: number[] = [1,2,3] // 배열은 대괄호 
let mightBeUndef: string | undefined = undefined // | 사용 시 여러 타입 사용 가능
let color: 'red' | 'orange' | 'yellow' = 'red' // 값을 타입으로도 사용 가능 
```

### interface 사용하기
interface는 클래스, 객체의 타입을 지정할 때 사용 
##### 예시 
``` ts
interface Shape {
  getArea(): number // Shape 인터페이스를 이용한 객체, 클래스는 getArea 라는 number return 함수가 꼭 있어야 함 
}

class Circle implements Shale { // interface 를 이용한 class 선언 

}
```


<hr/>

## create-react-app using TS 
``` sh
yarn create react-app my-app --template typescript

```

## 기존 React App에 TS 적용하기
``` sh
npm install --save typescript @types/node @types/react @types/react-dom @types/jest

# or

yarn add typescript @types/node @types/react @types/react-dom @types/jest
```
Next, rename any file to be a TypeScript file (e.g. src/index.js to src/index.tsx) and restart your development server!

<hr/>

## 리액트 컴포넌트의 타입 ?
### React.FC
__React.FC__ 사용 시 props를 넣어줄 때, props들을 하나의 객체로 만들어서 __Generics__ 로 넣은 후, 인자로 전달 
##### 예시
``` ts
import React from 'react'
type GreetingProps = {
  name: string
}

const Greetings: React.FC<GteetingProps> = ({name}) => (
  <div>Hello, {name}</div>
)
```
#### 특징 
1. props에 __children__ 이 기본적으로 들어가 있음 
2. 컴포넌트의 defaultProps, propTypes, contextTypes를 설정할 때 자동완성이 가능 
children이 option으로 들어가있기에 컴포넌트의 props의 타입이 명백하지 않다고 볼 수 있다.

처리하고싶다면 Props 안에 children을 설정해야 함 
##### 예시
``` ts
type GreetingProps = { // interface 사용 가능 
  name: string
  children: React.ReactNode
}
```
또한 defaultProps가 작동하지 않음 
__사용하지 않는 것을 권장__

### 이런식으로 쓰자 
``` ts 
import React from 'react'

type GreetingsProps = {
  name: string
  mark: string
  optional?: string // 있어도, 없어도 되는 props는 ? 문자를 사용!!
  onClick: (name: string) => void // 함수 props : (인자:타입) => 리턴 값 타입
}

const Greetings = ({name, mark, optional}: GreetingsProps) => {
  return (
    <div>
      Hello, {name} {mark}
      {optional && <p>{optional}</p>}
    </div>
  )
}

export default Greetings
```
<hr/>

