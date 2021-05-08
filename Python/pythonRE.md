# [정규표현식 in Python by re](https://wikidocs.net/4308)

```python
import re
```

## 메타 문자

```
. ^ $ * + ? { } [ ] \ | ( )
```

#### [ ]

문자 클래스, character class
[] 안의 문자들과 매치
e.g. <code>[abc]</code>는 a, b, c 중 하나와 매치

만약 하이픈 - 를 이용시, 범위를 의미.
<cdoe>[a-c] === [abc]</code>
<code>[a-zA-z]</code> === 알파벳
<code>[0:9]</code> === 숫자

만약 <code>^</code>는 not의 의미.
e.g. <code>[^0-9]</code> === 숫자가 아닌 문자

-> 간단하게 나타낸 문자 클래스
<code>\d</code> === <code>[0-9]</code> : 숫자
<code>\D</code> === <code>[^0-9]</code> : 숫자가 아닌 문자
<code>\s</code> === <code>[ \t\n\r\f\v]</code> : whitespace 문자. (빈칸은 공백 문자 의미)
<code>\S</code> === <code>[^ \t\n\r\f\v]</code> : whitespace 문자가 아닌 것 (빈칸은 공백 문자 의미)
<code>\w</code> === <code>[a-zA-Z0-9_]</code> : 문자+숫자(alphanumeric)
<code>\W</code> === <code>[^a-za-z0-9_]</code> : 문자+숫자(alphanumeric)가 아닌 것

즉, 대문자는 소문자의 반대.

#### .

Dot은 <code>\n</code>를 제외한 모든 문자와 매치됨.

e.g. <code>a.b</code>는 a+모든문자+b.
but, ab 는, ab사이에 아무것도 존재하지 않으므로 매치되지 않음

진짜 dot을 사용하려면, <code>[.]</code>사용하기!

#### \*

star operation

계산이론에서 배운 그것.
0~infinite회의 반복이다.
e.g. <code>ca\*t</code> === {ct, cat, caat, ...}

#### +

이것도 그거다~
1~infinite 회.
e.g. <code>ca+t</code> === {cat, caat, ...}

#### {}

반복 횟수를 고정

{n} = n회 반복.
{m,n} = m에서 n회 반복.
{m,} = m회 이상 반복
{,n} = n회 이하 반복.

즉, {1,} === +, {0,} === \*

#### ?

=== {0,1}

#### |

or의 의미.
e.g.
<code>(Crow|Servo)</code>는 Crow와 Servo를 매치

#### ^

문자열의 맨 처음과 일치
i.e., search를 match처럼 이용 가능

#### $

문자열의 끝과 일치

#### ()

괄호로 그루핑을 하면,
이후 <code>m.group()</code>함수에서 인덱스를 통해 접근 가능
0: 전체 문자열
1: 첫 괄호
2: second 괄호...

또한, 그루핑된 놈을 재사용하는 것도 가능,
e.g.
<code>p = re.compile(r'(\b\w+)\s+\1')</code>
<code>\1</code> 는 <code>\b\w+</code>를 의미.

그룹 네임도 만들 수 있다.

```
(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)
```

그룹 명이 name으로서 생김.

#### 전방 탐색

문자열을 소모하지 않고 매칭해볼 수 있음

##### 긍정형

문자열이 맞을 때만.
e.g.

```python
p=re.compile(".+(?=:)")
m=p.search("http://google.com")
```

을 하면, m은 http: 까지 읽고, http를 리턴한다.

##### 부정형

<code>.bat</code>, <code>.exe</code>를 제외하는 regEX
<code>._[.](?!bat$|exe$)._$</code>

## re 모듈 사용하기

```python
import re
p = re.compile('ab*')
```

<code>re.compile()</code> 사용 시 정규표현식을 컴파일 하여 리턴.
이후 그 패턴 객체 (위에서는 <code>p</code>) 사용하여 작업 수행

> 컴파일 시 특정 옵션 주는 것도 가능하며 패턴이란 정규식을 컴파일한 결과.

### 패턴 객체의 method

#### match()

문자열의 처음부터 해당 정규식과 매치가 완료되는지 조사

결과로 match 객체 또는 None을 반환

그래서 보통 이런 식으로 작성

```python
p = re.compile(정규표현식)
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')
```

#### search()

<code>match()</code>와 거의 비슷하나, 문자열의 처음부터가 아니라, 문자열 전체를 검색 하여 첫 문자열을 match객체로서 반환

#### findAll()

<code>search()</code> 처럼 작용하나, 해당 결과물을 리스트로 반환

#### finditer()

<code>findAll()</code>와 비슷하다, 이터레이터를 반환

각각의 이터레이터는 match객체를 포함.

### 위에서 받은 match 객체의 method

#### group()

매치된 문자열을 반환

#### start()

시작 인덱스

#### end()

끝 인덱스 (NULL 포함)

#### span()

(시작,끝) 인덱스 튜플

### 축약하기

```python
p = re.compile('[a-z]+')
m = p.match("python")
```

equals to

```python
m = re.match('[a-z]+', "python")
```

### 컴파일 옵션

<code>DOTALL</code>, <code>S</code> : <code>.</code>가 줄바꿈 문자까지 매치되도록 변경
<code>IGNORECASE</code>, <code>I</code> : 대소문자 구분 X
<code>MULTILINE</code>,<code>M</code>: 여러 줄과 매치됨
<code>VERBOSE</code>,<code>X</code>: verbose모드

e.g.

```python
p=re.compile('a.b', re.S)
m=p.match('a\nb')
```
