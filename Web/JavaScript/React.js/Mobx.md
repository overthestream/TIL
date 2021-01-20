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

## [Mobx 리액트에 적용한 Counter 예제](https://velog.io/@velopert/MobX-2-리액트-프로젝트에서-MobX-사용하기-oejltas52z)

**Counter.js**

```js
import React, { Component } from 'react';
import { decorate, observable, action } from 'mobx';
import { observer } from 'mobx-react';

class Counter extends Component {
	number = 0;

	increase = () => {
		this.number++;
	};

	decrease = () => {
		this.number--;
	};

	render() {
		return (
			<div>
				<h1>{this.number}</h1>
				<button onClick={this.increase}>+1</button>
				<button onClick={this.decrease}>-1</button>
			</div>
		);
	}
}

decorate(Counter, {
	number: observable,
	increase: action,
	decrease: action,
});

export default observer(Counter);
```

**App.js**

```js
import React, { Component } from 'react';
import Counter from './Counter';

class App extends Component {
	render() {
		return (
			<div>
				<Counter />
			</div>
		);
	}
}

export default App;
```

state, props 없이 Data 주고받기가 가능하다

## 다른 파일에 store 만들기!

**stores/counter.js**

```js
import { observable, action } from 'mobx';

decorate(CounterStore, {
	number: observable,
	increase: action,
	decrease: action,
});

export default class CounterStore {
	number = 0;

	increase = () => {
		this.number++;
	};

	decrease = () => {
		this.number--;
	};
}
```

## Provider로 프로젝트에 스토어 적용

**index.js**

```js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'mobx-react'; // MobX 에서 사용하는 Provider
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import CounterStore from './stores/counter'; // 방금 만든 스토어 불러와줍니다.

const counter = new CounterStore(); // 스토어 인스턴스를 만들고

ReactDOM.render(
	<Provider counter={counter}>
		{/* Provider 에 props 로 넣어줍니다. */}
		<App />
	</Provider>,
	document.getElementById('root')
);

registerServiceWorker();
```

## inject로 컴포넌트에 스토어 주입

**Counter.js**

```js
import React, { Component } from 'react';
import { observer, inject } from 'mobx-react';

@inject('counter')
@observer
class Counter extends Component {
	render() {
		const { counter } = this.props;
		return (
			<div>
				<h1>{counter.number}</h1>
				<button onClick={counter.increase}>+1</button>
				<button onClick={counter.decrease}>-1</button>
			</div>
		);
	}
}

export default Counter;
```

스토어를 props로 전달받을 수 있다.

## 특정 값만 스토에서 받아오기도 가능

```js
import React, { Component } from 'react';
import { observer, inject } from 'mobx-react';

// **** 함수형태로 파라미터를 전달해주면 특정 값만 받아올 수 있음.
@inject((stores) => ({
	number: stores.counter.number,
	increase: stores.counter.increase,
	decrease: stores.counter.decrease,
}))
@observer
class Counter extends Component {
	render() {
		const { number, increase, decrease } = this.props;
		return (
			<div>
				<h1>{number}</h1>
				<button onClick={increase}>+1</button>
				<button onClick={decrease}>-1</button>
			</div>
		);
	}
}

export default Counter;
```

```js
import React from 'react';
import ShopItem from './ShopItem';
import { inject, observer } from 'mobx-react'; // 불러오기

const items = [
	{
		name: '생수',
		price: 850,
	},
	{
		name: '신라면',
		price: 900,
	},
	{
		name: '포카칩',
		price: 1500,
	},
	{
		name: '새우깡',
		price: 1000,
	},
];

// **** onPut 함수 추가됨
const ShopItemList = ({ onPut }) => {
	const itemList = items.map((item) => <ShopItem {...item} key={item.name} onPut={onPut} />);
	return <div>{itemList}</div>;
};

// **** inject, observer 적용
export default inject(({ market }) => ({
	onPut: market.put,
}))(observer(ShopItemList));
```

이런 느낌.

## 스토어끼리 관계 형성

스토어끼리 접근을 하기 위해서는 **RootStore** 이 필요하다.

### 예제

**src/stores/index.js**

```js
import CounterStore from './counter';
import MarketStore from './market';

class RootStore {
	constructor() {
		this.counter = new CounterStore(this);
		this.market = new MarketStore(this);
	}
}

export default RootStore;
```

root 스토어에서 다른 스토어를 불러오고 생성해준 후, this를 파라미터로 넣어준다. -> 이거 스토어 클래스 생성자에서 받아서 처리

this를 파라미터로 넣어주면, 각 스토어에서 루트 스토어로 접근이 가능하므로,

스토어 -> 루트 스토어 -> 다른 스토어 이게 가능 .

함수형 스토어는 없나 .?

provide 할 때도 편리. 따로 생성 안하고 루트만 넣어주면 된다 .

**src/index.js**

```js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'mobx-react'; // MobX 에서 사용하는 Provider
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import RootStore from './stores';

const root = new RootStore(); // *** 루트 스토어 생성

ReactDOM.render(
	<Provider {...root}>
		{' '}
		{/* *** ...root 으로 스토어 모두 자동으로 설정 */}
		<App />
	</Provider>,
	document.getElementById('root')
);

registerServiceWorker();
```

this.root.다른스토어 이런 식으로 접근 가능

## Mobx 리액트 컴포넌트 최적화

1. 리스트 렌더링 시 컴포넌트에 리스트 데이터만 props로 넣자.

리스트 렌더링 시에는 성능을 신경써야 한다.

리액트는 그 바뀐거 리렌더링을 하잖아?

예를 들어서 리스트 렌더링 컴포넌트에 유저 정보가 들어 있으면,

유저가 바뀔 때도 리렌더링 되니까 느려진다. 이런건 분리를 하자

2. 세부 참조는 최대한 늦게 하자

세부참조 혹은 역참조 = dereference

```js
const itemList = items.map((item) => (
	<BasketItem
		name={item.name}
		price={item.price}
		count={item.count}
		key={item.name}
		onTake={onTake}
	/>
));
```

이런게 세부 참조임, 그런데 이걸 아이템 컴포넌트 내부에서 하면. 좋겠다 이거죠.

```js
const itemList = items.map((item) => <BasketItem item={item} key={item.name} onTake={onTake} />);
```

3. 함수는 미리 바인딩하고, 파라미터는 내부에서 넣기

클린코드죠.. 함수는 변수에 넣어서 하란말이야

## [from mobx doucument](https://mobx.js.org/observable-state.html)

#### makeObservable(target, annotations?, options?)

모든 객체가 target 인수가 될 수 있다.

-> 클래스의 constructor에서 target에 this 넣어서 호출

annotation: 저스트 주석 넣는 것 .

#### makeAutobservable(target, overrides?, options)
