# [clean-code-javacscript](https://github.com/qkraudghgh/clean-code-javascript-ko/blob/master/README.md#목차)

clean code 책을 번역, 자바스크립트에 적용한 내용

비단 자바스크립트만이 아닌 그냥 코딩 실력 자체에 도움이 될 내용

## 변수 (Variables)
### 의미 있고 발음하기 쉬운 변수명 

##### 예시
``` js
const yyyymmdstr = moment().format('YYYY/MM/DD') // 나쁜 예
const currentDate = moment().format('YYYY/MM/DD') // 좋은 예 
```
### 동일한 유형의 변수에는 동일한 형식으로 
##### 예시
``` js
// 나쁜 예
getUserInfo()
getClientData()
getCurstomerRecord()

// 좋은 예
getUser()
```

### 검색가능한 이름 
코드는 작성하는 것 만큼, 또는 그 이상으로 읽는 일이 많다. 

그러므로 읽기 쉽고 검색 가능하게 작성할 것.
> buddy.js ESLint 유용

즉, 상수 같은 것에 이름을 붙여라 이 말 
##### 예시 
``` js 
// 나쁜 예 : 86400000이 뭔데?
setTimeout(blastoff, 86400000)

// 좋은 예
const MILLISECONDS_IN_A_DAY = 86400000
setTimeout(blastoff, MILLISECONDS_IN_A_DAY)
```

### 의도를 나타내는 변수 사용 
##### 예시
``` js
const address = 'One Infinite Loop, Cupertino 95014'
const cityZipCodeRegex = /^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$/

// 나쁜 예 : 저 배열이 대체 뭔데..
saveCityZipCode(address.match(cityZipCodeRegex)[1], address.match(cityZipCodeRegex)[2])

// 좋은 예 (배열 할당)
const [, city, zipCode] = address.match(cityZipCodeRegex) || []
saveCityZipCode(city, zipCode)
```

### 자신만 알아볼 수 있는 작명을 피하라
명시적인 것 >>>>>>> 암시적인 것
##### 예시 
``` js
// 나쁜 예 : PS에서 해온대로 하면 못알아먹어 ..
let n 

// 좋은 예
let caseNum
```

### 문맥상 필요 없는것들은 쓰지 마라 
##### 예시
``` js
// 나쁜 예 : 차 객체의 차 색? 오우 쉣..
const Car = { 
  carMake: 'BMW',
  carModel: 'M3',
  carColor: '파란색'
}

// 좋은 예 : 
const Car = {
  make: 'BMW',
  model: 'M3',
  color: '파란색'
}
```

### 기본 매개변수 적용이 short circuiting보다 깔끔하다 
##### 예시
``` js
// 나쁜 예 : 복잡해.
function createMicrobrewery(name) {
  const breweryName = name || 'Hipster Brew Co.'
}

// 좋은 예 
function createMicrobrewery(name = 'Hipster Brew Co.'){

}
```
<hr/>

## 함수(Function)
### 함수 인자는 2개 이하가 이상적이다 
매개 변수의 개수를 제한하는 것은 함수 테스팅을 쉽게 만들어준다. 

매개변수가 3개 이상이면 테스트 해야하는 경우의 수가 많아지고 각기 다른 인수들로 여러 사례들을 테스트해야 한다.

3개 이상이라면 인자를 통합하는 것이 이상적이다.

__객체__ 를 사용하면 통합이 쉽겠죠?

또는 ES6의 __비구조화(destructuring) 구문__ 
##### 예시 
``` js
const array = [1, 2]
const [one, two] = array
```
##### 장점 
1. 함수 인자 및 리턴 값 타입을 볼 때 어떤 속성이 사용되는지 즉시 알 수 있다.
2. 함수에 전달된 인수 객체의 지정된 기본타입 값을 복제하며, 사이드 이펙트를 방지한다.
3. Linter 사용시 미사용 인자를 경고하거나 비구조화 없이 코드를 짤 수 없게 할 수 있다.

##### 예시
``` js 
// 나쁜 예
function createMenu(title, body, buttonText, cancellable) {
  // ...
}

// 좋은 예 
function createMenu({ title, body, buttonText, cancellable }) {
  // ...
}

createMenu({
  title: 'Foo',
  body: 'Bar',
  buttonText: 'Baz',
  cancellable: true
})
```
### 하나의 함수는 하나의 행동만 
소프트웨어 엔지니어링에서 가장 중요한 규칙. 

함수가 2개 이상의 행동을 한다면 작성은 물론 디버깅, 이해도 어려워짐
##### 예시
``` js
// 나쁜 예
function emailClients(clients) {
  clients.forEach(client => {
    const clientRecord = database.lookup(client)
    if (clientRecord.isActive()) {
      email(client)
    }
  })
}

// 좋은 예
function emailClients(clients) {
  clients
    .filter(isClientActive)
    .forEach(email)
}

function isClientActive(client) {
  const clientRecord = database.lookup(client)
  return clientRecord.isActive()
}
```

### 함수명은 함수가 무엇을 하는지 명시 
##### 예시
``` js
// 나쁜 예:

function AddToDate(date, month) {
  // ...
}

const date = new Date();

// 뭘 추가하는 건지 이름만 보고 알아내기 힘듭니다.
AddToDate(date, 1);

// 좋은 예

function AddMonthToDate(date, month) {
  // ...
}

const date = new Date();
AddMonthToDate(date, 1);
```

### 중복된 코드는 작성하지 마라 
추상화를 잘 해서 중복을 피하면 유지보수가 몹시 쉬워짐 

### 객체 생성시 Object.assign 사용 
##### 예시
``` js
// 나쁜 예
const menuConfig = {
  title: null,
  body: 'Bar',
  buttonText: null,
  cancellable: true
};

function createMenu(config) {
  config.title = config.title || 'Foo';
  config.body = config.body || 'Bar';
  config.buttonText = config.buttonText || 'Baz';
  config.cancellable = config.cancellable !== undefined ? config.cancellable : true;
}

createMenu(menuConfig);

// 좋은 예 
const menuConfig = {
  title: 'Order',
  // 유저가 'body' key의 value를 정하지 않았다.
  buttonText: 'Send',
  cancellable: true
};

function createMenu(config) {
  config = Object.assign({
    title: 'Foo',
    body: 'Bar',
    buttonText: 'Baz',
    cancellable: true
  }, config);

  // config는 이제 다음과 동일합니다: {title: "Order", body: "Bar", buttonText: "Send", cancellable: true}
  // ...
}

createMenu(menuConfig);
```

### 매개변수로 플래그를 사용하지 마라 
플래그 사용 자체가 함수가 한가지 이상의 역할을 하고 있다는 것이다. 

boolean 기반으로 코드가 나뉜다면 함수를 분리하라 
##### 예시
``` js
// 나쁜 예
function createFile(name, temp) {
  if (temp) {
    fs.create(`./temp/${name}`);
  } else {
    fs.create(name);
  }
}

// 좋은 예
function createFile(name) {
  fs.create(name);
}

function createTempFile(name) {
  createFile(`./temp/${name}`);
}
```

### 사이드 이펙트를 피하라 
함수는 값을 받아서 어떤 일을 하거나 값을 리턴할 때 사이드 이펙트를 만들어냄. 

파일에 쓰여질 수도 있고, 전역 변수를 수정할 수도 잇음. 

어떤 구조체도 없이 객체 사이의 상태를 공유하거나, 무엇이든 쓸 수 있는 변경가능한 데이터 유형을 사용하거나, 같은 사이드 이펙트를 여러 개 만들면 안된다.

### 전역 함수를 사용하지 마라 
전역 함수는 JavaScript에서 다른 라이브러리들과 충돌이 일어날 수 도 있다.

### 명령형 보다는 함수형 프로그래밍을 지향하라
더 깔끔하고 테스팅이 쉽다.

### 조건문을 캡슐화 하라
=== 함수는 하나의 역할만(다른 함수로 만들어 써라 Like isQueueEmpty)
### 부정조건문을 사용하지 마라
### 조건문을 최대한 피하라
다형성을 이용하면 조건문을 최대한 피할 수 있음.

조건문은 clean code 컨셉에 어긋난다.

##### 예시
``` js
// 나쁜 예
class Airplane {
  // ...
  getCruisingAltitude() {
    switch (this.type) {
      case '777':
        return this.getMaxAltitude() - this.getPassengerCount();
      case 'Air Force One':
        return this.getMaxAltitude();
      case 'Cessna':
        return this.getMaxAltitude() - this.getFuelExpenditure();
    }
  }
}

// 좋은 예
class Airplane {
  // ...
}

class Boeing777 extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getPassengerCount();
  }
}

class AirForceOne extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude();
  }
}

class Cessna extends Airplane {
  // ...
  getCruisingAltitude() {
    return this.getMaxAltitude() - this.getFuelExpenditure();
  }
}
```

### 타입 체킹을 피하라
JS는 동적 타입 언어인데, 이때문에 버그가 발생할 수 있으나, 타입 체킹 말고도 다른 방법으로 이러한 버그들을 피할 수 있다.
일관성 있는 API를 사용하라
##### 예시
```js
// 나쁜 예
function travelToTexas(vehicle) {
  if (vehicle instanceof Bicycle) {
    vehicle.pedal(this.currentLocation, new Location('texas'));
  } else if (vehicle instanceof Car) {
    vehicle.drive(this.currentLocation, new Location('texas'));
  }
}

// 좋은 예
function travelToTexas(vehicle) {
  vehicle.move(this.currentLocation, new Location('texas'));
}
```

만약 기본 자료형을 사용하고, 다형성 사용이 불가능할 때, 타입 체킹이 필요하다면 TypeScript(정적 타입 자바스크립트)를 도입해라.

### 과도한 최적화는 지양하라
최신 브라우저들은 런타임에 많은 최적화 작업을 수행하므로 코드를 최적화하는 것은 시간낭비일 가능성이 크다. 최적화가 부족한 곳만 찾아 최적화하라.

### 죽은 코드는 바로 지워라
그 코드를 재사용할 일이 있다고 해도 그것은 히스토리에 남아있으므로 그냥 지워라


<hr/>

## 객체와 자료구조(Objects and Data Structures)

### getter와 setter를 사용하라 
자바스크립트는 인터페이스와 타입, private, public 등이 없으므로 그냥 getter, setter를 사용하여 객체의 데이터에 접근하라.

에러 처리가 쉽고 캡슐화가 가능, 코드가 간단, lazy loading이 가능 

### 클로져를 이용하면 비공개 멤버를 만들 수 있다.

<hr/>

## 클래스(Classes)
### ES5의 함수보다 ES2015/ES6의 클래스를 사용하라

### 메소드 체이닝을 사용하라 

### 상속보다는 조합을 사용하라 
조합이 상속보다 평소에 이득이 많다. 
다음을 제외하고.
1. 당신의 상속관계가 "has-a" 관계가 아니라 "is-a" 관계일 때 (사람->동물 vs. 유저->유저정보)
2. 기반 클래스의 코드를 다시 사용할 수 있을 때 (인간은 모든 동물처럼 움직일 수 있습니다.)
3. 기반 클래스를 수정하여 파생된 클래스 모두를 수정하고 싶을 때 (이동시 모든 동물이 소비하는 칼로리를 변경하고 싶을 때)
> 조합 : constructor

<hr/>

## SOLID
### 단일 책임 원칙(Single Responsibility Principle, SRP)
클래스도 함수처럼, 개념적으로 단일하게 응집되어야 함.

클래스 수정시에는 수정해야하는 이유가 2개 이상 있으면 안됨 

### OCP, LSP 
무슨말임 이게 ..

### 인터페이스 분리 원칙(Interface Segregation Principle, ISP)
자바스크립트는 인터페이스가 없지만, 인터페이스는 분리해서 무거운 인터페이스는 지양해야함.

즉 옵션을 줘라
##### 예시
``` js
class DOMTraverser {
  constructor(settings) {
    this.settings = settings;
    this.options = settings.options;
    this.setup();
  }

  setup() {
    this.rootNode = this.settings.rootNode;
    this.setupOptions();
  }

  setupOptions() {
    if (this.options.animationModule) {
      // ...
    }
  }

  traverse() {
    // ...
  }
}

const $ = new DOMTraverser({
  rootNode: document.getElementsByTagName('body'),
  options: {
    animationModule() {}
  }
});
```

### 의존성 역전 원칙(Dependency Inversion Principle, DIP)
어렵네 

<hr/>

## 테스트(Testing)
테스트 코드를 작성해서 테스팅을 꼭 해봐라!!!

## 동시성(COncurrency)
### Callback 대신 Promise를 사용하라
Callback은 깔끔하지 않고 많은 중괄호 중첩을 만드므로 Promise를 사용하라
### Asunc/Await는 Promise보다도 깔끔하다

## 에러 처리 (Error Handling)
### 단순히 에러를 확인만 하지 마라 
에러를 try catch, console log 등으로 확인만하지 말고 그것에 어떤 장치를 해두어라.
### Promise의 실패를 무시하지 마라

## 포맷팅(Formatting)
Prettier 등 잘 써
### 일관된 대소문자를 사용하라
camel case, pascal case 등 일관되게 사용

### 함수 호출자와 함수 피호출자는 가깝게 사용하라
근접해 있어야 읽기가 쉽다.

<hr/>

## 주석(Comments)
### 주석을 단다는 것은 로직이 복잡하다는 것이다.
좋은 코드는 코드 자체로 말한다.
### 주석으로 된 코드를 남기지 마라
버전 관리 도구가 존재한다.
### 코드 기록을 주석으로 남기지 마라
git log를 써라
### 코드의 위치를 설명하지 마라