# 리액트 훅 정리

## Ref

[Velopert님의 블로그](https://react.vlpt.us) 및 리액트를 다루는 기술 책 참고

[리액트 docs](https://ko.reactjs.org/docs/hooks-reference.html)

## useState

함수형 컴포넌트에서도 상태 관리가 가능하도록 함

```js
const [변수명, setter 함수명] = useState(기본값);
```

> useState는 변수와 setter함수의 배열을 반환하며, 위의 것은 배열을 비구조화 할당한 것.
> state가 변경될 때마다 리렌더링됨

## useEffect

리액트 컴포넌트가 렌더링될 때, 리렌더링될 때, 언마운트될 때, 특정 값이 바뀔 때 등 특정 작업을 수행하도록 함

### 리렌더링 시 마다 호출

두번째 인자를 아예 생략 시 **리렌더링**될 때마다 호출됨

### 특정 값이 변경될 때만 실행하기

두번째 인자로 빈 배열 대신 값을 넣어주면,

처음 **마운트**될 때에 더해, 지정한 **값이 바뀔 때**에도 호출됨

거기에 더해 클린업 함수는 **언마운트**될 때에 더해 **값이 바뀌기 직전**에 호출됨

## 마운트, 언마운트

```js
useEffect(() => {
	console.log('마운트 시 실행');
	return () => {
		console.log('언마운트 시 실행');
	};
}, []);
```

기본적으로, 두번째 인자로 **빈 배열**을 주면 **마운트**될 때(컴포넌트가 처음 렌더링 될 때) return 외의 코드가 실행되며,
**언마운트**(컴포넌트가 사라질 때)될 때 return해준 함수가 실행됨 (비교할 게 없으니까 아예 리렌더링 때는 호출이 안되는 것)

이것을 **클린 업 함수**(뒷정리 함수)라고 부름.

### 원리가 뭔가

두번째 배열 값이 이전과 같다면 호출 X 방식

## useReducer

useState 대체 hook.

상태 업데이트 로직을 분리할 수 있음

reducer 함수를 받아야 함.
->reducer 타입: <code>(state, action) => newState</code>

```js
const [state, dispatch] = useReducer(reducer, initialArg, init);
```

> state는 말그대로 state(상태 객체)
> action은 state를 변화시키는 무언가

이후 useReducer는 state와 dispatch를 반환함(Redux와 비슷한 로직)

> literally state(상태 객체)
> dispatch는 state를 변화시키는 함수(=reducer 함수)(action을 인자로 준다)

다수의 하윗값을 포함하는 상태 또는 다음 state가 이전 state에 의존적인 경우 useReducer > useState

```js
const initialState = { count: 0 };

function reducer(state, action) {
	switch (action.type) {
		case 'increment':
			return { count: state.count + 1 };
		case 'decrement':
			return { count: state.count - 1 };
		default:
			throw new Error();
	}
}

function Counter() {
	const [state, dispatch] = useReducer(reducer, initialState);
	return (
		<>
			Count: {state.count}
			<button onClick={() => dispatch({ type: 'decrement' })}>-</button>
			<button onClick={() => dispatch({ type: 'increment' })}>+</button>
		</>
	);
}
```

### 초기값이 아니라 초기화 함수를 주기

```js
function init(initialCount) {
	return { count: initialCount };
}

function reducer(state, action) {
	switch (action.type) {
		case 'increment':
			return { count: state.count + 1 };
		case 'decrement':
			return { count: state.count - 1 };
		case 'reset':
			return init(action.payload);
		default:
			throw new Error();
	}
}

function Counter({ initialCount }) {
	const [state, dispatch] = useReducer(reducer, initialCount, init);
	return (
		<>
			Count: {state.count}
			<button onClick={() => dispatch({ type: 'reset', payload: initialCount })}>Reset</button>
			<button onClick={() => dispatch({ type: 'decrement' })}>-</button>
			<button onClick={() => dispatch({ type: 'increment' })}>+</button>
		</>
	);
}
```

initial value와 init 함수를 둘 다 주기

## useMemo

컴포넌트 내부 연산 **최적화**

메모이제이션된 값을 반환

생성 함수와 그것이 의존하는 값 배열을 전달하면, 의존성이 변경되었을때만 메모이제이션된 값만 다시 계산

렌더링중에 실행되는 함수로 렌더링 중에 하지 않는 것은 이 함수내에서 하지 말 것

배열이 없으면 useEffect처럼 매 렌더링마다 새 값을 계산함

useEffect랑 비슷한 느낌이라고 생각하면 될 듯

## useCallback

```js
const memoizedCallback = useCallback(() => {
	doSomething(a, b);
}, [a, b]);
```

메모이제이션된 콜백 반환

useMemo와 상당히 비슷, 특정 결과 값이 아닌, 특정 함수를 새로 만들지 않고 재사용하고 싶을 때 사용

인라인 콜백과 의존성 값의 배열을 전달하면 의존성이 변경되었을때만 콜백을 변경함

useCallback(fn, deps) === useMemo(() => fn, deps)

## useRef

함수형 컴포넌트에서 ref 사용하기

.current 프로퍼티로 전달된 인자로 초기화된 변경 가능한 ref 객체를 반환

```js
const refContainer = useRef(initialValue);
```

**예시**

```js
function TextInputWithFocusButton() {
	const inputEl = useRef(null);
	const onButtonClick = () => {
		// `current` points to the mounted text input element
		inputEl.current.focus();
	};
	return (
		<>
			<input ref={inputEl} type='text' />
			<button onClick={onButtonClick}>Focus the input</button>
		</>
	);
}
```

**useRef 변수는 값이 바뀐다고 해서 컴포넌트가 리렌더링되지 않음**

왜냐, 매번 동일한 객체를 제공하므로, .current를 변형한다고 해서 리렌더링을 발생시키지 않음

너가 useIntersectionObserver 못만든 이유가 있었어 정훈아..

React가 DOM 노드에 ref를 달거나 뗄 때 어떤 코드를 실행하고싶다면, 콜백 ref를 사용할 것.

### 콜백 ref

ref가 다른 노드에 연결될때마다 해당 콜백을 호출함

**예시**

```js
function MeasureExample() {
	const [height, setHeight] = useState(0);

	const measuredRef = useCallback((node) => {
		if (node !== null) {
			setHeight(node.getBoundingClientRect().height);
		}
	}, []);

	return (
		<>
			<h1 ref={measuredRef}>Hello, world</h1>
			<h2>The above header is {Math.round(height)}px tall</h2>
		</>
	);
}
```

### 다른 용례: 변수 만들기

값 변경이 바로바로 리렌더링으로 이어지지 않을 때

ex: id값 등

useRef 호출 시 인자를 넣어주면 그것이 .current의 기본값이 됨.

> 원래는 null 넣어줘야 한다
