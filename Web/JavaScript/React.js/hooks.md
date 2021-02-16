# 리액트 훅 정리

## useState

함수형 컴포넌트에서도 상태 관리가 가능하도록 함

```js
const [변수명, setter 함수명] = useState(기본값);
```

> useState는 변수와 setter함수의 배열을 반환하며, 위의 것은 배열을 비구조화 할당한 것.
> state가 변경될 때마다 리렌더링됨
