# Scroll in JS

## REF

https://tech.lezhin.com/2017/07/13/intersectionobserver-overview
https://velog.io/@doondoony/IntersectionObserver
https://y0c.github.io/2019/06/30/react-infinite-scroll/

## 세로 스크롤

document.documentElement. ->

- **scrollHeight**: 화면에 보이지 않는 높이까지 포함한 페이지의 총 높이
- **scrollTop**: 이미 스크롤되어서 보이지 않는 구간의 높이
- **clientHeight**: 클라이언트에게 보여지고 있는 페이지의 높이

즉 스크롤 아래까지 다 내리면, **scrollHeight === scrollTop+clientHeight**겠지요

window.pageYOffset

## Intersection Observer API

부모 엘리먼트 또는 최상위 document의 viewport와 대상 엘리먼트의 교차 영역에서 발생한 변경 사항을 비동기적으로 감시하는 방법을 제공

즉 DOM 엘리먼트 간에 영역이 겹쳐지는 것을 감시

-> scroll이벤트 감지, resize 등의 비싼 비용의 이벤트의 퍼포먼스 성능 개선

쉬운 lazy-load, infinite scroll이 가능

### 객체 생성

```js
const io = new IntersectionObserver(callbback, {
  root: null,
  rootMargin: '0px',
  threshold: 0.5.
})
```

1. root: <code>Element</code> 또는 <code>null</code>

관측 대상을 감싸는 element.
null -> viewport

---

2. rootMargin: margin 값

root 요소를 감싸는 margin 값 지정

---

3. threshold: target element가 root와 몇 % 교차했을 때, callback을 실행할 것인가 -> float 값

0.0 ~ 1.0 의 값, element가 50% 보였을 때 실행할 것이라면 0.5를 주면 된다.

- 여러 구간에서 callback을 실행하고 싶다면, 배열로 작성

ex: 노출도 10%당 무언가 하고싶다면, [0.0, 0.1, ... 0.9, 1.0] 이렇게 줘라

---

4. callback: 호출될 함수

매개변수로 전달가능한 놈: <code>entries</code>(Element 배열 -> target), <code>observer</code>(자기자신)

### 예시

#### lazy-load

```js
const images = document.querySelectorAll('.image-box');
const threshold = 0.8;
const lazyLoadOption = { root: null, threshold };
const lazyLoadImage = (entries, observer) => {
	entries.forEach((entry) => {
		const { target } = entry;
		if (entry.isIntersecting) {
			target.style.backgroundImage = `url("${target.dataset.src}")`;
			target.style.backgroundSize = `cover`;
			target.style.backgroundColor = `transparent`;
			target.textContent = '';
		}
	});
};
const lazyLoadingIO = new IntersectionObserver(lazyLoadImage, lazyLoadOption);
images.forEach((image) => lazyLoadingIO.observe(image));
```

#### Infinite Scroll

```HTML
<ul class="infinite-container"></ul>
```

여기에 <code>li</code>를 만들어낸다고 치자

```js
const ioOptions = {
	root: null,
	threshold: 1,
};
const loadingNewCats = (newCats) => {
	const loadingTemplate = `<li><span>Loading New Cats...</span></li>`;
	return new Promise((resolve, reject) => {
		container.insertAdjacentHTML('beforeend', loadingTemplate);
		setTimeout(() => {
			resolve(newCats);
			container.removeChild(container.lastChild);
		}, 1000);
	});
};

const handleInfiniteScrolling = (entries, observer) => {
	const $last = [...entries].pop();
	if ($last.isIntersecting) {
		loadingNewCats(createNewCats()).then((newCats) => {
			container.append(...newCats);
			currentLast = lastChild();
			observer.unobserve($last.target);
			observer.observe(currentLast);
		});
	}
};
const io = new IntersectionObserver(handleInfiniteScrolling, ioOptions);
```

### custom hook

```js
import { useEffect } from 'react';

export default ({ root, target, onIntersect, threshold = 1.0, rootMargin = '0px' }) => {
	useEffect(() => {
		if (!root) {
			return;
		}

		const observer = new IntersectionObserver(onIntersect, {
			root,
			rootMargin,
			threshold,
		});

		if (!target) {
			return;
		}

		observer.observe(target);

		return () => {
			observer.unobserve(target);
		};
	}, [target, root, rootMargin, onIntersect, threshold]);
};

useIntersectionObserver({
	root: rootRef.current,
	target: targetRef.current,
	onIntersect: ([{ isIntersecting }]) => {
		if (isIntersecting && !loading && currentPage.current < totalPage.current) {
			loadMoreImage();
		}
	},
});
```
