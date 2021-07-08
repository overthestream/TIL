# Basic Structure

## CSS의 기본적인 구조 

``` css
selector {
  property1: value1;
  property2: value2;
}
```

* 선택자(selector): HTML 요소를 태그 이름, 클래스 이름, 아이디, 상태, 속성 등을 기준으로 선택하는 방법 
* 속성(property): HTML 요소에 적용하고자 하는 디자인 요소
* 속성값(value): 속성의 구체적인 값 

하나의 요소는 여러 selector에 의해 선택될 수 있으며, 그러므로 conflict가 발생할 수도 있다.

**우선 순위**
1. 속성 값의 뒤에 !important가 붙은 속성
2. HTML에서 style 속성을 사용하여 정의한 속성
3. 선택자: Id > class > tag
4. 상위 요소로부터 상속

## HTML에 CSS 적용하기 

### 1. inline style

HTML 요소 태그 안에 style attribute 값으로 property-value pair를 열거하는 방법

HTML요소에 개별적으로 디자인을 적용하는 방식이므로 선택자를 쓰지 않는다.

각 요소가 어떤 디자인을 가지는지는 쉽게 알 수 있다.

그러나 웹 페이지의 구조를 표현한다는 HTML의 목적에 위배되며, 문서가 불필요하게 길어질 수 있다. 

서식이 있는 텍스트(rich text)를 표현할 때만 자주 사용됨

``` HTML
<div>
  Already Member? <span style="font-weight: bold">Sign In</span>
</div>
<div>
  <span style="color: red">Sign Up</span>
</div>
```

### 2. internal style sheet

head 태그 내부에 `<style type="text/css">` 요소를 삽입하고 그 content에 CSS 코드를 작성한다. 

선택자를 사용할 수 있으므로 inline style보다는 효율적이지만 HTML 내부에 작성하는 것으므로 여전히 본연의 목적에는 맞지 않는다.

또한 여러 HTML 문서에 CSS를 적용할 때는 여전히 번거롭고 비효율적이다.

### 3. external style sheet

HTML 문서와 CSS 문서를 서로 다른 파일에 작성하고, HTML 문서의 head 태그 내부에 link 태그를 이용하여 CSS 파일을 import 한다.

link 태그에는 다음과 같은 attribute를 지정해주어야 한다. 

* type="text/css" : CSS 형태임을 명시 
* rel="stylesheet" : stylesheet임을 명시
* href : CSS 문서의 경로 

HTML CSS 각각 목적을 모두 달성하면서도 유지 보수가 용이하다.

## Inheritance 

하위 요소에게도 해당 속성이 그대로 적용되는가에 관한 특징.

inheritance가 no이면 기본값이 적용되고, 아니라면 부모 요소의 값이 적용된다.

각각의 property마다 inheritance가 다르다.

**inherited property의 예**
``` HTML
<p>This paragraph has <em>emphasized text</em> in it.</p>
```
```CSS
p { color: green; }
```
emphasized text 역시, 초록색으로 적용된다.

이렇게 글씨에 적용되는 속성들은 

**Non-inherited property의 예**

``` HTML
<p>This paragraph has <em>emphasized text</em> in it.</p>
```
```CSS
 p { border: medium solid; }
```
하위 요소에까지 border가 적용되어버리면 몹시 어지럽겠죠..! 

### inherit 키워드

inheritance를 specify함 

## Block vs Inline

HTML element는 block 또는 Inline element로 분류된다.

### Block-level elements

container(부모 요소)의 수평,수직 공간을 모두 차지한다. 

즉, block을 형성한다.

항상 새로운 행에서 시작하며 가능한 full width를 차지한다. 

단, width 속성으로 조절 가능.

<body> element에만 나타난다. 

### inline elements

할당된 공간만 차지한다. 즉, 개행하지 않고, 필요한 너비만 차지한다.

그러므로 width, height, margin-top, margin-bottom, padding 등이 불가능하다.

예를 들어 <span>이나 <a>, <br> 등등

div container를 사용하며 수평 정렬
### Difference 

block-level element는 다른 block element나 inline element를 포함할 수 있다. 즉, block element는 inline element보다 더 큰 구조를 만들 수 있다.

block-element는 무조건 new line에서 시작하지만, inline은 이름 그대로, line 어디서든 시작 가능하다. 

HTML5부터는 이러한 구분이 더 복잡하게 바뀌었다. inline은 phrasing으로 변경되었다. 