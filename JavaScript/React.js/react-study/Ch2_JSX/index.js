import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
); //ReactDOM.render = 컴포넌트를 페이지에 렌더링하는 함수, 첫 파라미터 : 페이지에 렌더링할 내용, 두번째 파라미터는 해당 JSX(첫 파라미터)를 렌더링할 document 내부 요소 (public/index.html의 id=root 인 요소에 렌더링됨) 

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
