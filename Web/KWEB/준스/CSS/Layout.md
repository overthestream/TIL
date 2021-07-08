# Layouts

CSS를 이용하여 레이아웃을 설계하는 방법.

## 레이아웃이란

직역하면 배치.

HTML 요소를 배치하고 정돈

## Box Model

HTML 요소는 사각형 형태의 레이아웃을 가지며, 이것을 box model이라고 한다.

padding, border, margin, content의 네가지 요소로 구분된다.
* content: 텍스트나 이미지 등 박스의 실질적 내용
* padding: content와 border 사이의 여백
* border: content와 padding을 감싸는 테두리
* margin: border 바깥, 다른 요소와의 간격

### content
width와 height가 너비와 높이를 지정해준다.

### Border
border-width, border-height, border-top, border-style, border-color 등이 있다.

### margin
marin은 겹칠 수 있따.

margin collapsing(마진 겹침 또는 마진 상쇄)
형제 요소 간에 상하 margin, 빈 요소간의 상하 margin, 부모 요소의 top margin과 첫 자식의 top margin, 부모 요소의 bottom maring과 마지막 자식의 bottom margin이 겹칠 때 발생

## Position

static, relative, absolite, fixed 네가지가 존재

기본 값은 static (왼쪽에서 오른쪽으로, 위에서 아래로)

나머지는 top, left, right, bottom 속성을 통해 위치를 정할 수 있다.

* relative: static으로 지정되었을 때 기주으로 방향 속성의 값에 따라 배치.

* absolute: static이 아니라 부모 요소를 기준으로 배치 
* fixed: absolute와 유사하지만, 스크롤 해도 그대로다.