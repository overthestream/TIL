# Built-in Objects

JS에서 number, string, array, function 등은 모두 객체이다. (object는 객체가 아니다.)

## Property와 Method

object의 peroperty를 이용하는 함수는, 객체 내부에 정의하여 namespace 오염을 방지해야 하며, 이러한 함수를 method라고 한다.

이때, `this` 킼워드를 이용하여 자기 자신이 속한 객체에 접근한다.

단..! method 표현 시 arrow function을 이용하면, arrow function에서의 this를 정하는 방식이 일반적 함수와 다르므로 전통적인 함수 표현 방식을 사용하는 것이 좋다! 

## Class and Instance

동일한 형태의 객체를 생성하기 위해 class를 이용한다.

객체의 설계도와 같은 역할을 하며, 클래스는 각 객체가 갖는 속성, 상수, 메서드에 대한 정보의 집합이다. 

클래스를 통해 생성된 객체를 instance라고 한다.

인스턴스를 생성하려면 클래스를 통해 객체를 생성하는 매개체가 필요한데, 이 매개체를 생성자(constructor)라고 부른다.

보통 생성자를 이용하여 인스턴스를 생성할 때는 new 키워드를 사용한다.

또한, 객체는 const로 선언되어도 속성이나 메서드는 재할당 가능하다.

## Global Methods(Functions)

global object의 메서드로서 함수처럼 사용할 수 있는 메서드들.

isFinite, isNan, parseInt 등등..

## String Objects

String 객체의 메서드들.
* length
* includes
* replace
* replaceAll
* split
* substring
* toLowerCase
* toUppercase
* trim

등등. 이름만 봐도 뭐하는지 알제.

## Array Obhects

* length
* concat
* filter
* find
* findIndex
* forEach
* includes
* join
* map
* pop
* push
* reverse
* slice
* sort

## Date Objects

날짜와 시간을 다루는 클래스. 

생성자를 이용하여 인스턴스를 형성한다.

* now
* getFullYear
* getMinutes
* getUTCDate
* getUTCHours
* toLocaleString

## Math Objects

* E
* LN2
* PI
* SQRT2
* abs
* ceil
* cos
* sxp
* floor
* log
* max
* min
* pow
* random
* round
* sqrt 