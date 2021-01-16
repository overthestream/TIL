# React Tutorial

## children?
리액트 컴포넌트 사용 시 컴포넌트 태그 사이의 내용을 보여주는 props
예시  
``` js
(...)
<MyComp>리액트</Mycomp>
()...)
```
``` js 
// Mycomp.js
const MyComp = props => {
  return (
    <div>{props.children}</div> // 리액트 출력
  )
}
```
