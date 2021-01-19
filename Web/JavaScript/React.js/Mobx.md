# [Mobx tutorial](https://medium.com/@jsh901220/mobx-처음-시작해보기-a768f4aaa73e)

리액트에서 state와 props만으로는 데이터 관리가 난잡하고 어렵다.

상위 component에서 state들을 만들고 props로 하위 component들로 뿌려주는 방식

상태관리 라이브러리 사용 시, Global한 store를 이용해 쉽게 state관리가 가능

## Mobx의 개념.

1. state: 어플리케이션의 데이터 상태.

2. derivations: 파생값, 어플리케이션에서 자동으로 계산되는 모든 값.

3. Reaction: derivation과 유사한 개념이나 차이점은 값을 생성하지 않는 함수라는 것 대체로 I/O와 연관된 작업. 자동으로 DOM을 업데이트하게 해주고, 네트워크 요청을 하도록 해줌.

4. Action: state를 변경하는 모든 것. 동기적으로 처리됨

Actions -Mutate-> state -update-> Derivations, Reactions

## [state 관리하기](https://velog.io/@velopert/begin-mobx)

observable 함수는 observable state를 만들어준다 (관찰받는 상태인 state)

#### observable

```js
import { observable } from 'mobx';

const calculator = observable({
	a: 1,
	b: 1,
});
```

observable state는 mobx가 이 객체를 관찰하게 되어 변화가 일어나면 바로 탐지가능

#### reaction

특정 값이 바뀔 때 어떤 작업을 하고 싶을 때.

```js
import { observable, reaction } from mobx;
const calculator = observable({
  a:1,
  b:1
});
reaction(
  () => calculator.a,
  (value, reaction) => {
    console.log(`a 값이 ${value}로 바뀌었습니다.`)l
  }
)
reaction(
  () => calculator.b,
  value => {
    console.log(`b 값이 ${value} 로 바뀌었네요!`);
  }
);
```

첫 인자가 observable value, 두번째 인자가 reaction 함수인 듯 함

#### computed

연산된 값을 사용해야 할 때. 이 값을 조회할 때마다 특정 작업을 처리하는 것이 아니라, 이 값에서 의존하는 값이 바뀔 때 미리 값을 계산해놓고, 조회 시에는 캐싱된 데이터를 사용

```js
import { observable, reaction, computed } from 'mobx';

// Observable State 만들기
const calculator = observable({
	a: 1,
	b: 2,
});

// **** computed 로 특정 값 캐싱
const sum = computed(() => {
	console.log('계산중이예요!');
	return calculator.a + calculator.b;
});

sum.observe(() => calculator.a); // a 값을 주시
sum.observe(() => calculator.b); // b 값을 주시

calculator.a = 10;
calculator.b = 20;

//**** 여러번 조회해도 computed 안의 함수를 다시 호출하지 않지만..
console.log(sum.value);
console.log(sum.value);

// 내부의 값이 바뀌면 다시 호출 함
calculator.a = 20;
console.log(sum.value);
```

#### autorun

autorun 은 reaction 이나 computed 의 observe 대신에 사용 될 수 있는데, autorun 으로 전달해주는 함수에서 사용되는 값이 있으면 자동으로 그 값을 주시하여 그 값이 바뀔 때 마다 함수가 주시되도록 해줍니다. 여기서 만약에 computed 로 만든 값의 .get() 함수를 호출해주면, 하나하나 observe 해주지 않아도 됩니다.

```js
import { observable, autorun } from 'mobx';

// Observable State 만들기
const calculator = observable({
	a: 1,
	b: 2,
});

// computed 로 특정 값 캐싱
const sum = computed(() => {
	console.log('계산중이예요!');
	return calculator.a + calculator.b;
});

// **** autorun 은 함수 내에서 조회하는 값을 자동으로 주시함
autorun(() => console.log(`a 값이 ${calculator.a} 로 바뀌었네요!`));
autorun(() => console.log(`b 값이 ${calculator.b} 로 바뀌었네요!`));
autorun(() => sum.get()); // su

calculator.a = 10;
calculator.b = 20;

// 여러번 조회해도 computed 안의 함수를 다시 호출하지 않지만..
console.log(sum.value);
console.log(sum.value);

calculator.a = 20;

// 내부의 값이 바뀌면 다시 호출 함
console.log(sum.value);
```

#### class 적용

```js
import { decorate, observable, computed, autorun } from 'mobx';

class GS25 {
	basket = [];

	get total() {
		console.log('계산중입니다..!');
		// Reduce 함수로 배열 내부의 객체의 price 총합 계산
		// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
		return this.basket.reduce((prev, curr) => prev + curr.price, 0);
	}

	select(name, price) {
		this.basket.push({ name, price });
	}
}

// decorate 를 통해서 각 값에 MobX 함수 적용
decorate(GS25, {
	basket: observable,
	total: computed,
});

const gs25 = new GS25();
autorun(() => gs25.total);
gs25.select('물', 800);
console.log(gs25.total);
gs25.select('물', 800);
console.log(gs25.total);
gs25.select('포카칩', 1500);
console.log(gs25.total);
```

#### Action

상태에 변화를 일으키는 것.

개발자 도구에서 변화의 세부 정보를 볼 수 있고, 변화를 한꺼번에 일으켜서 변화가 일어날 때마다 reaction이 나타나는 것이 아니라, 모든 액션이 끝난 후 reaction이 나타나도록 함 ( 동기적 )

```js
import { decorate, observable, computed, autorun, action } from 'mobx';

class GS25 {
	basket = [];

	get total() {
		console.log('계산중입니다..!');
		// Reduce 함수로 배열 내부의 객체의 price 총합 계산
		// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
		return this.basket.reduce((prev, curr) => prev + curr.price, 0);
	}

	select(name, price) {
		this.basket.push({ name, price });
	}
}

decorate(GS25, {
	basket: observable,
	total: computed,
	select: action, // **** 액션 명시
});

const gs25 = new GS25();
autorun(() => gs25.total);
gs25.select('물', 800);
console.log(gs25.total);
gs25.select('물', 800);
console.log(gs25.total);
gs25.select('포카칩', 1500);
console.log(gs25.total);
```

#### transaction

Action 한꺼번에 일으키기

Action이 literally 동기적으로 나타나고, 그 후 reaction

```js
import { decorate, observable, computed, autorun, action, transaction } from 'mobx';

class GS25 {
	basket = [];

	get total() {
		console.log('계산중입니다..!');
		// Reduce 함수로 배열 내부의 객체의 price 총합 계산
		// https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce
		return this.basket.reduce((prev, curr) => prev + curr.price, 0);
	}

	select(name, price) {
		this.basket.push({ name, price });
	}
}

decorate(GS25, {
	basket: observable,
	total: computed,
	select: action,
});

const gs25 = new GS25();
autorun(() => gs25.total);
// 새 데이터 추가 될 때 알림
autorun(() => {
	if (gs25.basket.length > 0) {
		console.log(gs25.basket[gs25.basket.length - 1]);
	}
});

transaction(() => {
	gs25.select('물', 800);
	gs25.select('물', 800);
	gs25.select('포카칩', 1500);
});

console.log(gs25.total);
```
