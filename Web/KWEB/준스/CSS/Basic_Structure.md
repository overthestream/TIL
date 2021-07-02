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

