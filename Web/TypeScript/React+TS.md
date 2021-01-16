# React implementation using Typescript

[타입스크립트로 컴포넌트 children 사용하기](https://www.carlrippon.com/react-children-with-typescript/)

## UseState 사용하기

제네릭 사용

```ts
const [count, setCount] = useState<number>(0);
```

## Map

배열. Mapping

```ts
arr.map(callback, [thsArg]);
```

- callback : 새로운 배열의 요소를 생성하는 함수.
  - currentValue: 현재 처리하는 요소
  - index: 현재 처리하는 요소의 index 값
  - array: 현재 처리하는 원본 배열
- thisArg(선택 항목): callback함수에서 사용할 this 레퍼런스

##### 예시

```js
var numbers = [1, 2, 3, 4, 5];

var processed = numbers.map(function (num) {
	return num * num;
});
```

#### 데이터 배열을 컴포넌트 배열로 변환하기

```js
import React from 'react';

const IterationSample = () => {
	const names = ['눈사람', '얼음', '눈'];
	const nameList = names.map((name) => <li>{name}</name>);
	return <ul>{nameList}</ul>;
};

export default IterationSample;
```

### 스타일드 컴포넌트

```ts
const Container = styled.div<{ age: number }>`
	color: ${(props) => (props.age > 20 ? 'red' : 'gray')};
`;
```
