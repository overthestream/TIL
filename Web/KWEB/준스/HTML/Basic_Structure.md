# Basic Structure 

## Tag & Element 

HTML 예시 하나로 HTML 구조를 파악해보자면..

```HTML 
<!doctype html>
<html>
<head>
    <title>Example Domain</title>
    <meta charset="utf-8">
    <meta http-equiv="Content-type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
    <div>
        <h1>Example Domain</h1>
    </div>
</body>
</html>
```

위의 예시를 보자. 일단 4행을 보면 대괄호로 둘러싸인 title들이 `Example Domain`을 감싸고 있다. 

`대괄호 두 쌍`과 그것으로 둘러 싸인 `내부`를 **tag**라고 한다. 

`title 태그`에서는 'title'이 그 태그의 **tag name**이다.

또한 `tag 내부`, 즉 'Example Domain'을 **content**라고 한다. 

이렇게 시작 태그와 끝 태그와 그것으로 감싸진 content를 **HTML element**라고 한다.

HTML element는 내부에 다른 요소를 포함할 수 있다. 

즉, **nested** 구조가 가능하다.

내부 요소를 하위 요소(sub element) 또는 자식 요소(child element)라고 하며,

그 것을 감싸는 태그를 상위 요소(super element), 부모 요소(parent element)라고 한다.

또한 같은 층에 있는 요소를 형제 요소(sibling element)라고 한다.

그런데 meta 태그를 보면 끝 태그가 없다. 이렇게 시작 태그만 있는 요소도 존재하며, 단일 태그라고 부른다. 

또한 태그 내부에 이름 외에 다른 내용들이 적혀 있다.
이것은 해당 HTML요소의 속성(attribute)에 관한 것으로, `key="value"` 형태로 표현되어 있다. 

즉 HTML 요소는 다음과 같이 표현될 수 있다. 
```
<tagname attr1="value1" attr2="value2">content</tagname>
```

## 기본적 구조 

HTML 문서는 기본적인 틀이 있다.

먼저 맨 위에 `<!doctype html>`을 적어 HTML 문서임을 명시하고,
가장 상위 태그로 html태그, 바로 하위 태그로 head 및 body 태그가 위치해야 한다.


즉, 다음과 같은 구조를 가진다.
```HTML
<!doctype html>
<html>
  <head>
    <!-- Head Element Content -->
  </head>

  <body>
    <!-- Body Element Content-->
  </body>
</html>
```
head 요소는 해당 HTML문서의 전반적인 정보를 담고 있다. 웹 페이지의 이름을 나타내는 title 태그, UTF인코딩, viewport 등 정보를 저장하는 meta 태그, link 태그, script 태그 등등이 존재한다.

body 요소는 웹 페이지에서 사용자에게 보여질 부분이 포함되는 태그이다. 텍스트, 이미지 등의 내용이 모두 body 태그 안에 작성된다. 

## 자주 사용되는 HTML tags 

### Heading Tag

h1 ~ h6 의 태그들이며, h는 heading의 약자이다. 주로 제목을 나타낼 때 사용하며, h 뒤의 숫자는 그 크기를 나타낸다.

### p, br Tag

p 태그는 paragraph의 약자로 문단을 구분하는 태그이다. 
문단과 문단 사이에 개행 문자를 넣어주는 역할을 하며, 문단과 문단 사이에는 별도의 공간이 생긴다.

> HTML에서는 공백, 개행 등의 whitespace 문자들을 여러개가 나열되어도 모두 하나의 공백으로 취급한다. 그러므로 HTML contents 내부에서 줄바꿈을 하더라도 실제로 줄바꿈이 되지 않는다.

그래서 br 태그를 이용하는데, br 태그는 개행 문자를 삽입해주는 단일 태그이다.

### a Tag 

a 태그는 HTML 요소에 하이퍼링크를 걸어준다. 

아래 3개의 태그 속성을 이용해 하이퍼링크를 만들어준다.

* href: 하이퍼링크의 주소 
* title: 하이퍼링크의 설명, 호버 시 표시된다.
* target: 하이퍼링크 로드 옵션 
  - _blank: 새로운 창 또는 탭
  - _self: 현재 창
  - _parent, _top: 참고만 하세요 

### button Tag 

button 태그는 클릭할 수 있는 버튼을 만들어준다.

JS와 결합하여 태그 클릭 시 특정 동작이 수행되도록 할 수 있다. 

속성은 disabled, type 등이 있다. disabled 속성은 버튼을 비활성화 시키고, type은 버튼 동작에 차이를 만든다.
**ex**
``` HTML
<button type="submit" disabled>hi</button>
```

### List Tag 

항목을 나열하여 리스트를 표현하는 태그가 있다. 

순서가 없는 리스트(unordered list)를 나타내는 ul 태그

순서가 있는 리스트(ordered list)를 나타내는 ol 태그

위의 두 태그 하위 태그로 사용하는, 각 원소를 감싸는 li 태그 

### img Tag 

문서에 이미지를 삽입해주는 단일 태그.

다음과 같은 속성 존재

* src: 이미지 주소
* alt: 이미지 로딩 실패 시 표시되는 이미지 설명
* width: 너비
* height: 높이
  
### Input Tag

사용자로부터 정보를 입력받는 태그 

input, textarea, select 등 존재

* input: type 속성 값에 따라 다양한 형태로 입력 가능 
  * text: plain text
  * password: password
  * radio: 목록 중 하나 선택
  * checkbox: 목록 중 여러 개 선택 
* textarea: 여러 줄의 텍스트 입력 가능, 크기, 설명 등을 속성 통해 설정 
* select: drop-down 리스트를 만들 수 있다. 하위 항목은 option 태그로 감싸 줌.

**radio 예시**
``` HTML
<label><input type="radio" name="gender" value="male">Male</label>
<label><input type="radio" name="gender" value="female">Female</label>
```

입력 태그에는 name 속성 값을 지정해야 함 (key-value pair 형태로 사용 위힘), 그렇다면 value는?

text를 입력받는 태그는 text 값 자체가 value 값이다. 값을 지정해준다면, 기본 값이 됨

선택지 태그들에는 value 값을 지정해줘야 함.

### HTML Entities 

대괄호(tag와 혼동)나 특수 기호 등은 HTML entity(개체)를 통해 나타낸다.

개체의 이름을 사용하여 `&entityName;`으로 나타내거나 `&#entitnyNumber;`으로 나타낸다.

**자주 사용되는 것들**

* `&lt;` `&gt;` : < >
* `&quot;`: " 
* `&amp;`: & 
* `&npsp;`: non-breaking space, 여러 개의 공백 표현 가능.

이름이 없는 놈들은 유니코드 번호를 사용하여 나타낸다.

### div & span Tag

특정 기능이 없고, HTML element들을 묶어서 레이아웃을 만들어 구조화 하는 태그

non-semantic tag

div: 인접 요소와 같은 줄에 있지 않는다.

span: 인접 요소와 같은 줄에 있는다.

단, 개발자의 편의에 따라 예약되지 않은 이름을 태그 이름이나 속성 이름, 속성 값에 사용할 수 있고, 이를 CSS, JS에서 활용 가능하다.