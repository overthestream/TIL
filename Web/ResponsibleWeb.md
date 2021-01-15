# 반응형 웹 (Responsible Web)
디바이스 별로 레이아웃이 달라지는 웹

즉, 화면의 크기에 따라 레이아웃이 달라지는 웹 

<hr/>

## 미디어 쿼리 (Media Query)
화면의 크기에 따라 CSS를 다르게 적용하는 것

화면 사이즈를 인식해 서로 다른 CSS를 적용해 줌 

보통 스마트폰, 태블릿, PC 세 개 정도를 구분함 
> 320px ~ 768px → 스마트폰
> 768px ~ 1024px → 태블릿
> 1024px ~ → PC

### 작성법 
공통적으로 적용할 css를 작성한 다음 미디어 쿼리를 따로 작성한다.
``` css
@media [Only | Not] MediaType and (조건식) and (조건식) and ... {
  /* 실행문 */
}
```
### 조건식을 이루는 대표적인 Media Feature
width : max-width, min-width

height : max-height, min-height

뷰포트의 너비와 높이 : HTML 컨텐츠의 내용을 표시하는 전체적인 크기(!= 화면의 크기)

device : device-width, device-height 

디바이스가 출력할 수 있는 영역의 크기, 즉 스크린의 해상도

orientation

세로 or 가로 모드 판단 

aspect-ratio : max-aspect-ratio, min-aspect-ratio 

스크린의 너비와 높이의 비율, Value는 너비/높이 형태로 작성한다. 

### 예시 
``` css
.a-box {
  width: 100px;
  height: 100px;
  background-color: red;
}

@media all and (min-width: 768px) and (max-width: 1024px) {
  .a-box {
    width: 200px;
    height: 50px;
    background-color: blue;
  }
}
```
모든 Media Type에서, 뷰포트의 크기가 최소 768px(min-width) 그리고 최대 1024px(max-width)일 때 실행문의 스타일을 적용 