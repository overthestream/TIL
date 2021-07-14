# Javascript with Front-end

JS의 기본 문법을 이용하여 HTML 문서의 동적 기능을 구현해보자 ~ 

## Application of JS on HTML

FE에서 JS는 HTML을 제어하고 수정하기 위해 존재하는 언어이므로, CSS와 마찬가지로 HTML문서에 연동되어야 한다.

첫번째 방법으로 HTML 문서의 `head` 요소 안에 `script` 태그를 만들어 내부에 JS를 작성하는 것이다.

두번째 방법은 별도의 JS 파일을 만들어 JS에는 스크립트만, HTML에는 구조만 작성하는 방법이다.

HTML파일에는 script 태그의 src 속성에 JS 파일 경로를 작성하면 된다.

**Like**
``` HTML
<script type="text/javascript" src="./script.js"></script>
```

당연히, CSS 처럼 HTML과 CSS, JS의 분업 및 본연의 목적에 충실하려면 두번째 방법이 낫겠다.

다만 웹브라우저는 HTML 문서의 앞부분부터 로딩하므로 JS 파일이 연동된 sscript 태그 뒤의 요소를 JS 코드가 인식하지 못할 수도 있다. 

이것을 방지하기 위한 방법으로 script 태그를 body 태그 안에 작성하기도 하는데, 이것은 당연히 가독성을 떨어뜨린다.

**대신, script 태그에 `async` 또는 `defer` 속성을 활성화하여 이 문제를 해결할 수 있다.**

`async`를 명시하면 JS 코드는 비동기적으로 실행되며, `defer`를 명시하면, JS 코드가 문서 로딩이 끝난 뒤에 실행된다.


## DOM

문서 객체 모델 (DOM: Document Object Model)은 HTML 문서의 프로그래밍 인터페이스이자 구조를 나타내는 모델이다.

DOM을 통하여 HTML문서에서 원하는 HTML 요소를 선택하고, 그 요소의 정보에 접근하고 수정하는 등 제어가 가능하다. 

DOM을 통해 HTML 요소 내부의 텍스트, 속성값 등을 읽거나 수정할 수 있다.

### HTML 문서의 구조

HTML은 요소들이 계층 구조로 되어있다.

그러므로 DOM은 HTML 문서를 객체 형태로 표현한다.

tag(node), children 값을 가지는 tree 처럼.  .. .

document 객체가 root로 작용

### HTML 요소 조회

DOM에서 제공하는 메서드를 이용하여 HTML 요소를 조회(query)할 수 있다. 

제공하는 메서드는 다음과 같다.

* getElementById
* getElementsByTagName
* getElementsByClassName
* querySelector
* querySelectorAll

각각 요소의 자손 요소를 기준으로 id, tag, class, selector(css의 그것)에 맞는 요소를 반환한다.(`document` 객체를 주로 사용함. root 니까)

위를 보면 id는 unique 하므로 element.로 되어 있고,

나머지는 Elements이다. 여기서 요소들은 유사 배열로 반환된다. 

유사 배열이란 for문 등으로 iteration이 가능하나 Array는 아닌, HTMLCollection, NodeList 클래스의 인스턴스를 표현하는 용어이다.

querySelector 메서드들은 주어진 선택자로 선택되는 요소들을 반환한다.

또한 요소를 기준으로 상대적 위치에 있는 요소를 조회할 수도 있다.

* parentElement
* children
* firstElementChild
* lastElementChild
* previousElementSibling
* nextElementSibling

### HTML 요소 및 속성 접근 및 수정 

요소 객체에 접근하여 속성을 읽거나 쓰고 수정할 수 있다.

* innerText: 요소 내부의 텍스트에 접근 
* setAttribute: 요소의 속성 값을 변경
* getAttribute: get 요소의 속성 값
* hasAttribute: 속성이 있는지 판별
* removeAttribute: 속성 제거
* style: 요소의 CSS스타일에 접근, 대신 camelCase 이용한다.
* classList: 요소의 클래스 유사 배열에 접근할 수 있는 객체

자식 요소에 접근

* createElement: 새로운 요소를 생성하여 반환, document 객체만 사용 가능
* appendChild
* removeChild

## Browser Object Model(BOM)

브라우저 객체 모델(Browser Object Model, BOM)은 웹 브라우저의 정보에 접근하여 읽고 제어할 수 있도록 하는 객체 모델이다.

DOM과 달리 표준은 없으나 현대 브라우저들은 서로 같은 BOM 속성과 메서드를 가지고 출시되므로 브라우저별로 다른 BOM 코드를 작성할 필요가 없다.

### window 객체

DOM에서 HTML 문서의 구조와 관련된 모든 객체가 포함된 document 객체와 유사하게, BOM에서 브라우저와 관련된 객체들은 모두 window 객체에 포함되어 있다.

document 객체 또한 window의 하위 객체이다.

window 객체의 속성이나 메서드는 window를 명시하지 않아도 접근하거나 호출할 수 있다.

그래서 `window.document.` 가 아니라 `document.`가 가능한것

유용하게 사용되는 메서드

* alert
* confirm
* open
* close

#### screen 객체

현 웹 브라우저가 위치한 화면의 크기에 관한 객체

* width
* height
* availWidth: 최대 브라우저 너비
* availHeight
* colorDepth: 화면이 나타낼 수 있는 색상 수 

#### location 객체

현재 웹 페이지의 주소(위치)를 다룸

* hostname: 현재 페이지 호스트의 도메인 이름
* href: 현재 페이지의 주소
* pathname: 현재 페이지의 경로
* protocol: 현재 페이지의 프로토콜
* port: 현재 페이지의 포트
* assign(url): 주어진 문자열을 주소로 하는 웹 문서를 새로 여는 메서드

#### history 객체

방문한 웹 페이지의 목록을 다룸

* back: 이전 페이지를 여는 메서드
* forward: 다음 페이지를 여는 메서드
* go(delta): 현재 페이지를 기준으로 delta만큼 떨어진 페이지를 여는 메서드 (양수, 음수, 0에 따라 앞, 뒤, refresh가 모두 가능)

### Timeout and Interval

setTimeout: 일정 시간 후 함수를 실행 

clearTimeout, setInterval, clearInterval 등 

## Event and Event Listener

프로그램에서 이벤트는 어떠한 사건을 의미하며, FE에서 발생할 수 있는 이벤트로는 클릭, 키 입력, 드래그 등이 잇다.

이벤트를 이용하면 버튼을 통해 원하는 함수를 작동시키고, 키보드를 이용하여 게임 오브젝트를 컨트롤하는 등 사용자에 의해 동적으로 작동하는 웹 페이지를 구현할 수 있다.

이러한 기능은 특정 이벤트가 발생하였을 때 실행되어야 하는 작업을 명시하여 구현하며, 특정 요소에서 특정 이벤트가 발생할 때 실행될 함수를 이벤트 리스너라고 한다.

### Events 

웹 페이지에서 발생할 수 있는 이벤트는 다양하다.

* click
* mousedown
* mouseenter
* mouseleave
* keydown
* keyup
* keypress

### Event Listener

특정 요소에서 이벤트가 발생했을 때 이벤트 리스너를 실행시키려면 해당 요소와 이벤트 리스너를 등록해야 하며 크게 세가지 방법이 있다.

#### 1. HTML 요소의 속성과 속성값을 명시한다.

HTML의 요소 안에, 먼저 속성의 이름은 이벤트의 이름 앞에 접두사 on을 붙인다. 예를 들어 click 이벤트면 onclick 처럼.

이후 속성 값에 이벤트가 발생했을 때 수행될 JS 코드를 작성한다.

직관적으로 파악이 가능하지만 분리하는게 낫겠죠.

``` HTML
<button onclick="alert('Clicked!');">click!</button>
```

#### 2. HTML 요소 객체에 이벤트 리스너를 메서드로 할당하는 방법이다.

메서드의 이름은 앞의 방식과 마찬가지로 접두사 On을 붙여 작성하며 메서드의 값에 이벤트 리스너를 할당한다.

JS 파일에 작성할 수 있어 분리가 가능하며 IE 8 이전 버전 브라우저에서도 호환되며 간결하다.

but. 한 요소의 한 이벤트에 하나의 이벤트 리스너만 등록 가능하다..

``` JS
document.getElementById('btn').onclick = () =>{
  alert('Clicked!');
};
```

#### 3. 요소의 addEventListner 메서드를 이용하는 방법.

가장 권장되는 방법으로, 이벤트 이름과 이벤트 리스너를 인자로 받아 추가한다.

``` JS
document.getElementById('btn').addEventListner('click', () => {
  alert('Clicked!');
});
```

### Event Object 

비 유 티, 이 방법으로는 이벤트 리스너에서 발생한 이벤트에 대한 정보를 얻을 수 없다.

예를 들면 어떤 키를 눌렀는지, 이런 것들. 

이것은 이벤트 객체를 받음으로써 해결 가능하다. 

``` JS
document.getElementById('btn').addEventListner('click', event => {
  alert(event);
});
```

이벤트 객체의 속성 중 자주 쓰이는 속성들

* target: 이벤트가 발생한 요소 객체
* button: 마우스 이벤트를 바생시킨 마우스 버튼 
* clientX, clientY: 뷰포트 기준 마우스 이벤트가 발생한 위치
* offsetX, offsetY: 이벤트 기준 마우스 이벤트가 발생한 위치
* screenX, screenY: 웹 페이지가 존재하는 화면 기준 마우스 이벤트 발생 위치
* code: 키 입력을 발생시킨 키 

