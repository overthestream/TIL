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

#### 기본 타입
- Boolean
- Number
- String
- Object
- Array 
- Tuple (길이가 고정되고 각 요소의 타입이 지정된 배열)
- Enum (C의 열거형)
- Any (모든 타입 허용, 많이 쓰진 말자)
- Void
- Null 
- Undefined
- Never  (함수의 끝에 도달하지 않는다는 의미 )

##### 예시
``` ts
const isDone:boolean = true
const message:string = 'hello world'
const numbers: number[] = [1,2,3] // 배열은 대괄호 
let mightBeUndef: string | undefined = undefined // | 사용 시 여러 타입 사용 가능 (Union Type)
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

### 클래스 
객체 지향 프로그래밍

private, getter, setter 설정이 가능하다 

##### 예시 
``` ts 
class Developer {
  private name : string

  get name(): string {
    return this.name
  }

  set name(newValue: string) { // get만 설정하고, set을 미설정 하면 자동으로 readonly 변수가 된다
    if(newValue && newValue.length > 5) {
      throw new Error('이름이 너무 깁니다')
    }
    this.name = newValue;
  }
}
```

#### 추상클래스 (Abstract Class)
추상 클래스는 인터페이스와 비슷한 역할을 하면서 조금 다르다.

추상 클래스는 특정 클래스의 상속 대상이 되며, 상위 레벨에서 속성과 메소드를 정의함

abstract가 붙은 놈은 무조건 구현해야 함 (오버라이드)
##### 예시
``` ts
abstract class Developer {
  abstract coding(): void
  dring(): void{
    console.log('drink sth')
  }
}

class FrontEndDeveloper extends Developer {
  coding(): void {
    console.log('develop web')
  }
  design(): void {
    console.log('design web')
  }
}

```

### 제네릭 (Generics)
타입을 함수의 파라미터처럼 사용하는 것.

제네릭 코딩 

##### 예시
``` ts
function logText<T>(text: T): T {
  return text
}

logText<string>("Hello World") // <string> 생략 가능
```

#### 제네릭 인터페이스
##### 방법 예시
``` ts
function logText<T>(text: T): T {
  return text;
}

// 1
let str: <T>(text: T) => T = logText; 
// 2
let str: {<T>(text:T): T} = logText;

// 1
interface GenericLogTextInterface { 
  <T>(text: T): T;
}
let func: GenericLogTextInterface = logText

// 2
interface GenericLogTextInteface2<T> {
  (text: T): T
}
let func2: GenericLogTextInterface2<string> = logText
```
제네릭 클래스도 비슷한 방법으로 가능 
#### 제네릭 제약 걸기 
``` ts
function logText<T>(text: T): T {
  console.log(text.length)
  return text
}
```
에러가 발생한다. text 인자에 length가 있을지 없을지 모르니까
해결법 
``` ts
interface LengthWise {
  length: number
}
function logText<T extends LenthWise>(text: T): T {
  console.log(text.length)
  return text
}
```
제네릭 타입으로 length 프로퍼티를 가진 놈만 받게 제약을 걸 수 있다.

### d.ts
타입 스크립트 코드의 타입 추론을 돕는 파일 

### 모듈?

모듈은 전역 변수와 구분되는 자체 유효 범위를 가지며 export, import 등의 키워드를 이용해 다른 파일에서 접근함 

### Font 등 import 하기 
d.ts 파일에서 모듈 선언을 해줘야 사용 가능
##### 예시
``` ts
declare module '*.ttf'
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

## TS에서 styled-components 쓰기 

``` sh
npm i -D @types/styled-components # 스타일드 컴포넌트 + 타입 정의 
npm install --save-dev typescript-styled-plugin # 스타일드 컴포넌트 하이라이터
```
그리고, 
__tsconfig.json__
``` json
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

## ref
[타입스크립트 핸드북](https://joshua1988.github.io/ts/guide/type-inference.html#타입-추론-type-inference)

[react.vlpt.us](https://react.vlpt.us/using-typescript/01-practice.html)