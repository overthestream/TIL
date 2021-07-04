# Style Properties 

## 텍스트와 관련된 속성 

### [text-align](https://developer.mozilla.org/ko/docs/Web/CSS/text-align)

블록 요소, 표의 칸 상자 등에서 텍스트의 수평(가로) 정렬 (워드의 그것)

값 : center, left, right, justify (가운데, 왼쪽, 오른쪽, 양쪽), start, end(쓰기 방식에 따라 left 또는 right)

justify는 마지막줄을 제외함. justify-all 값은 마지막 줄에도 적용 

초기값: start

**참고**

인라인 콘텐츠를 가운데 정렬하지 않고, 자신(박스 요소)을 정렬하는 법은 margin을 auto로 설정하는 것.

``` CSS
.sth1 {
  margin: auto;
}
.sth2 {
  margin: 0 auto;
}
.sth3 {
  margin-left: auto;
  margin-right:auto;
}
```

### [text-decoration](https://developer.mozilla.org/ko/docs/Web/CSS/text-decoration)

text를 선(line)을 이용하여 꾸민다. 

세부 속성으로 `text-decoration-line`, `text-decoration-color`, `text-decoration-style`,`text-decoration-thickness` 가 있따.

각 값을 `text-decoration` 속성 값으로 차례대로 나열해도 된다.

**text-decoration은 모든 하위 텍스트 요소에 적용**

따라서 자식 요소는 부모가 적용한 decoration을 제거할 수 없다.

#### text-decoration-line 

* none : 없음
* underline : 밑줄
* overline : 윗줄
* line-through : 취소선
* blink : 사용 자제.
  
여러 개를 한 번에 쓸 수도 있다.

```CSS
.sth1 {
  text-decoration-line: underline overline;
}
.sth2 {
  text-decoration-line: underline line-through
}
```

#### text-decoration-color

* 색 이름: red, blue, green ...
* HEX: #ffffff, #000000...
* rgb: rgb(255, 90, 255) / rgba 가능
* hsl: hsl(70, 100%, 40%) / hsla 가능 
* currentColor: 글자 색 (초기 값)

#### text-decoration-style

text-decoration-line의 style을 구체화함 

* solid: single line
* double: double line
* dotted: dotted line
* dashed: dashed line(언더바)
* wavy: wavy line 

#### text-decoration-thickness 

* auto: 브라우저가 자동으로 선택 
* from-font: 폰트가 굵기 정보를 가지고 있다면 그것을 사용, 아니면 auto로 작용 
* <length>
* <percentage>

### line-height

줄 간격에 관한 속성. 100%는 1, 150%는 1.5 등으로 표현함 

블록 요소에는 line box의 minimum height를 명시한다.

또는 <length>,<percentage> 사용 가능