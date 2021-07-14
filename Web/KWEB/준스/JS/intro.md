# Introduction to Javascript

JS는 웹 분야에서 광범위하게 사용되는 interpreter형 프로그래밍 언어이다.

FE에서는 JS로 웹 페이지의 동적인 기능을 구현하며, FE 프레임워크인 Angular.js, Vue.js, React.js등에서도 쓰인다.

또한 백엔드 애플리케이션 또한 Node.js를 사용하여 JS로 구현 가능하다.

## interpreter

프로그래밍 언어는 실행 방식에 따라 컴파일러형 언어와 인터프리터형 언어로 나뉜다.

컴파일러형 언어는 실행 전에 코드를 기계어로 변환하는 컴파일 과정이 필요하며, C, C++, Java, Rust, Go 등이 있다.

반면 인터프리터 언어는 컴파일 없이 인터프리터를 통해 소스 코드를 바로 실행할 수 있으며, Python, Javascript 등이 있다.
컴파일이 불필요하므로 인터프리터에 하나의 표현식(expression)을 입력하면 바로 실행 결과를 알 수 있기도 하다. 
(REPL-Shell (Read, Eval, Print, Loop))

대신, 표현식이 실행될 때마다 해당 표현식을 분석하고 컴파일해야하므로 성능은 컴파일러형 언어에 비해 떨어진다.

## 변수 선언 

### ECMA Script 

스크립트 언어에 관한 규약으로, ES 라고도 하며 JS는 ES 표준을 따른다. 

2015년 ES6 출시 이후로 언어 표준에 큰 변화가 발생하였으며 이것을 이후로 모던 자바스크립트라고 부르고 있다.

대표적으로 var 대신 let, const 키워드를 이용하여 변수를 선언한다.

### 식별자의 선언 

JS는 다른 언어와 마찬가지로 변수나 상수 등의 식별자(identifier)를 정의하고 사용할 수 있으며 모든 식별자는 자료형이 있다.

하지만, 식별자 선언 시 자료형을 명시하지 않고, 인터프리터가 스스로 그 값을 분석하여 자료형을 지정한다. 

이것이 예상치 못한 에러나 협업 시의 어려움을 유발하므로 JS의 superset이면서도 타입을 명시하는 Typescript를 많이 사용한다. 

보통 변수, 상수, 함수는 camelCase, 클래스는 PascalCase, 상수는 대문자 스네이크 케이스(SNAKE_CASE)로 작명하는 convention이 있다. 

또한 이름은 숫자로 시작하지 않으며, 명확한 이름을 짓는 것이 좋다.

상기했듯, `var`, `let`, `const`를 이용하는데,

var은 재선언할 수 있고 재할당 할 수 있으며 변수의 유효범위나 수명 등에서 예상치 못한 에러를 발생시킬 수 있어 사용을 자제하는 게 좋다. (var은 function scope)

let으로 선언한 변수와 const로 선언한 변수는 블록 범위(block scope)를 가지며, let은 가변, const는 불변 상수이다. 둘 모두 재선언은 불가능하다.

## Data Types

JS에는 7가지 자료형이 존재한다.

* Primitive Types: number, string, boolean, undefined, null, symbol
* Compound Type: object

### Number

수를 저장하는 자료형으로 정수, 유리수 등 구분이 없고 상호 연산이 가능하다.

또한 값으로 Infinity와 NaN(Not a Number)를 가질 수 있다.

0을 나누는 연산으로부터 발생할 수 있다.

### String

문자열을 저장하는 자료형으로 +, 인덱스 연산이 가능하다.

escape sequence 문자를 사용해야 할 때도 있다.

### Boolean

true, false 두가지 값 

### Object

객체는 key, value를 가질 수 있는 자료형이다. 

Key는 Unique 문자열, value는 모든 종류의 값, 심지어 object까지 할당될 수 있다. 

객체 내부에 객체를 포함시켜 hierarchial data를 형성할 수도 있다.

### Undefined, Null

각각 값이 할당되어 있지 않은 식별자와 값을 모르는 식별자가 갖는 자료형이다.

### Array

배열은 index를 가지는 복수의 자료를 저장할 수 있는 자료구조이다.

원소의 자료형애 제한이 없어 서로 다른 자료형의 원소를 하나의 배열에 저장할 수 있으며, 배열의 크기가 정해져 있지 않아 메서드를 이용하여 원소를 자유롭게 넣고 뺄 수 있다.

## Statements and Functions

### Comparison

equality comparison은 다른 연어와 유사하게 ==와 !=로 수행도리 수 있으며, true or false 값을 반환한다.

그러나, worst programming language란 악명에 걸맞게 비교 연산에서 문제가 발생할 수 있다.

예를 들어 Number 0과 String '0'을 비교하면 자료형이 다른데도 불구하고 같다는 결과가 도출된다. 

왜냐하면 두 값에 대해 자의적으로 type coercion을 수행한 뒤 값을 비교하기 때문이다.

이렇게 비교 연산에서 ==와 !=로, 자료형 변환 이후 이루어지는 연산을 loose equality라고 한다. 

타입 변환 규칙은 몹시 어지러우므로 loose equality는 자제하자.

대신, strict equality가 존재하는데, `===`와 `!==` 연산자가 있다.

직관적이며 논리적 오류를 최소화할 수 있다.

### Conditional Statements

JS의 조건문은 여타 언어들과 유사하게, if, else 를 사용한다.

또한 switch-case, ?:(삼항 연산자)또한 지원한다.

### Iteration Statements

for, while, do-while 모두 지원한다.

또한, for-of 문도 지원한다.

예를 들면 Array에서 다음과 같이 연산 가능하다.

```JS
const fruits = ['apple', 'orange', 'mango', 'grape'];
for(const fruit of fruits){
  console.log(fruit);
}
```

Python마냥 for in 문도 사용 가능하다. 객체에 대해 동작하며 다음과 같이 사용할 수 있다

``` JS
const person = {
  age:20,
  name: 'Hoon',
  height: 183,
  sex: 'Male',
  weight: 73
};
for(const key in person) {
  console.log(key+':'+person[key]);
}
```

### Functions

function 키워드를 이용

또는 arrow function, anonymus function(함수를 다른 함수의 인자로 넘길 때 유용하게 사용)

