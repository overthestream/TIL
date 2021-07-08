# Selectors

CSS는 선택자를 통해 원하는 요소를 선택할 수 있다.

## Universal Selector 

전체 선택자는 HTML 문서의 모든 요소를 선택한다.
*로 작성한다.

```CSS
* {margin: 0;}
```

## Tag, Clss, Id Selector

태그, 클래스, 아이디를 기준으로 요소를 선택

* tag: tag-name
* class: .class-name
* id: #id

``` CSS
ul{ list-style: none;}
.title-thumbnail{ font-size: 20px;}
#article {padding: 0;}
div .title { font-weight: bold;}
```
이처럼 선택자를 중복 가능

## Child Selector & Descendants Selector

* 자식 선택자
parent > child의 형태로 쓰며, 

parent 선택자로 선택된 요소의 바로 밑에 있는 자식 요소 중 child 선택자에 맞는 것을 선택 

* 자손 선택자
parent child 형태

바로 밑이 아니라 parent 산하의 모든 요소 중 선택 

## Pseudo-class Selector 

가상 클래스 선택자는 특정한 상태에 놓여있는 요소들을 선택 

예를 들면 `hover`, `disabled` 등 상태를 가상클래스라고 하며,
:pseudo-class의 형태로 쓴다.

예를 들면 뭐 
``` CSS
button:hover{
  background-color:red;
}
```
