# React 최상위 API

## Ref

https://ko.reactjs.org/docs/react-api.html

## React.forwardRef

전달받은 ref 어트리뷰트를 하위 컴포넌트로 전달하는 React 컴포넌트를 생성

아래 두 방법에서 유용함

- DOM 엘리먼트로 ref 전달하기
- Higher Order Component로 ref 전달하기

즉 just ref를 하위로 전달이 가능하다는 것.

```js
const FancyButton = React.forwardRef((props, ref) => (
	<button ref={ref} className='FancyButton'>
		{props.children}
	</button>
));

// You can now get a ref directly to the DOM button:
const ref = React.createRef();
<FancyButton ref={ref}>Click me!</FancyButton>;
```
