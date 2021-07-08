# Responsive Web

PC가 아니라 모바일 디바이스를 이용하거나 할 때에도 웹 페이지를 볼 수 있는데,

웹 페이지는 상하방향으로만 스크롤할 때 가독성이 좋아진다.

그러므로 렌더링되는 화면의 크기에 따라 디자인이 바뀌는 Responsive Web의 필요성이 생긴다.

## Viewport

렌더링되는 화면.
**Viewport Setting**
```HTML
<meta name="viewport" content="width=device-width", initial-scal="1">
```

## MEdia Query

media query를 통해 반응형 디자인이 가능하다.

**예시**
```css
@media only screen and (min-width: 800px) {
  /*CSS*/
}
```

너비가 ~400, 400~800, 800~1200, 1200~ 으로 보통 순서대로 설정 