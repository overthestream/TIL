// 리액트 앱 분석

// 리액트를 사용할 수 있게 해 줌 : 리액트 생성 시 node modules 디렉터리가 생성, 이 디렉터리에 react 모듈 설치 -> import
// 사실 import는 브라우저에는 없고, Node.js에서 지원하는 기능 : import 기능 위해 브라우저에서는 bundler 사용 -> 여기에서 index.js가 사용됨
import React from "react"

// 웹팩의 로더가 파일, css 를 import해준다
import logo from "./logo.svg"
import "./App.css"

// App 컴포넌트를 만들어준다. 함수형 컴포넌트
// 컴포넌트 렌더링 시 함수에서 반환하고 있는 내용을 나타냄
// HTML같지만 HTML이 아니라 jsx
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  )
}

export default App // -> index.js. 
