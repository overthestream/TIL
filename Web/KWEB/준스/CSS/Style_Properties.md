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

### letter-spacing

글자간 간격. %, em, px 등 사용

### vertical-align

세로 방향 정렬에 관한 속성

element를 line box 내부에서 수직 정렬하고자 할 때, 또는 table의 한 셀에서 수직정렬할 때 사용 


**inline, table-cell** element에만 사용 가능.

#### 그러면 block-element에서는 어떻게 수직 정렬을?

1.table-cell 형태로 바꿔준다.

```CSS
.p {
  display: table-cell;
  vertical-align: middle;
}
```

2. 포지션 직접 조정
3. margin
4. flex
 ```CSS
 .p {
   display: flex;
   align-items: center;
 }
 ```
5. div element로 container를 만들어 `line-height` 속성 사용
   
2,3은 유지보수에 안 좋아보인다 그죠?

## 폰트와 관련된 속성

### font-size

글자 크기. em, px 등의 값 사용

### font-weight 

글자의 두께에 관한 속성 

100단위로 값을 지정함.

이외에도, normal, bolder 등의 값이 가능하며, 각각 400, 700의 상수값이다.

### font-family

글꼴을 지정함.

기본 폰트 외에 웹 폰트를 import하여 사용하거나, 직접 폰트 파일을 import하여 사용할 수도 있다.

### color

글자의 색상을 지정함,

red, blue 등의 색 이름이나,

rgb(r,g,b) 값이나 rgba(r,g,b,a), hsl(h, s%, l%), hsla(h, s%, l%, a), #FFFFFF(hex) 값 모두 사용 가능하다.

단, a는 투명도, hsl은 각각 색조, 채도, 명도이다.

이러한 색 속성은 `background-color`등의 속성에서도 사용 가능하다.

## 배경과 관련된 속성

### background-color

해당 element의 배경 색을 지정.

앞의 color와 동일한 값을 가질 수 있다.

### background-image

배경에 image를 삽입할 수 있다.

한 박스에 여러 Image를 삽입하려면 쉼표로 여러 값을 나열해 주면 된다.

`url("이미지 URL")`형태의 값으로 이미지를 넣을 수 있다.

`linear-gradient(rgba(0, 0, 255, 0.5), rgba(255, 255, 0, 0.5))` 처럼 그라데이션을 그릴 수도 있다.

### background-repeat

배경 이미지가 어떻게 반복될지 지정할 수 있다.

no-repeat, repeat-x, repeat-y, repeat, space, round 등의 값을 지정 가능하다.

초기값은 repeat이므로 이미지 크기와 요소 너비, 높이가 맞지 않다면 지정을 해줘야 한다.

### background-size

이미지 사이즈를 지정 가능하다.

이미지가 여러개면 쉼표로 구분해준다.

쉼표 없이 공백으로 구분하여 너비, 높이를 한번에 지정 가능하며,

하나의 값만 지정시, 높이는 auto가 된다.

contain은 이미지가 찌그러지거나 잘리지 않는 선에서 제일 크게 설정하는 값이다.

cover는 이미지가 찌그러지지 않는 한도에서 가장 크게 설정한다. 단, 가로세로 비가 다르다면 이미지를 잘라낸다.

auto는 이미지의 원본 크기를 유지한다. 