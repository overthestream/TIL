# React Tutorial

## children?

리액트 컴포넌트 사용 시 컴포넌트 태그 사이의 내용을 보여주는 props
예시

```js
(...)
<MyComp>리액트</Mycomp>
()...)
```

```js
// Mycomp.js
const MyComp = (props) => {
	return (
		<div>{props.children}</div> // 리액트 출력
	);
};
```

## useCallback

이벤트 핸들러 함수를 필요할 때만 생성하여 성능을 최적화

첫번째 인자 : 이벤트 핸들링 함수

두번째 인자 : 두번째 인자가 바뀔 때 마다 이벤트 핸들러 함수가 생성됨
