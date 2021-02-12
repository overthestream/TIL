# [관계형 데이터베이스](https://en.wikipedia.org/wiki/Relational_database)

**관계형 데이터베이스(Relational DataBase)**는 **관계형 모델(Relational Model)**에 기반한 데이터베이스이다.
관계형 DB를 관리하기 위해 **RDBMS(Relational DataBase Management System)**이라는 소프트웨어 시스템을 사용

DB에 질의 및 관리를 위해 **SQL(Structured Query Language)**를 사용하기도 함

## 관계형 모델

**관계형 모델**은 데이터를 1개 이상의, column(attribute)과 row, row(record, tuple)를 식별할 unique한 key들로 이루어진 테이블(또는 관계)로 표현한다
일반적으로 각각의 table(relation)은 하나의 entity type(하나의 데이터 타입)을 대표한다.

ex로 entity type이 한 사람이라고 할 때,

- row는 각 entity type의 instance를 표현한다(ex: Lee)
- column은 instance에 귀속된 값을 나타낸다(ex: 성씨)

## Keys

table의 각각의 row는 그것만의 unique한 key를 가진다.
table 속 row들은 연결된 row의 unique key에 대한 column을 추가하여(foreign keys) 다른 table의 row들과 연결될 수 있다.

이 과정에는 테이블에서 하나의 row만 선택하거나 수정하는 기능이 포함되므로 대부분 테이블의 각 row에 대하여 unique한 primary key(PK)가 있다.
테이블에 새 행이 기록되면 PK에 대한 새 고유값이 생성된다. 이 값은 시스템에서 테이블에 접근하는데 사용되는 key이다.

DB 내의 PK는 테이블 간의 관계를 정의하는 데 사용된다.
PK가 다른 table로 이동 시 그 키는 다른 테이블의 foreign key가 된다.

foreign key를 통해 일대일, 일대다, 다대다 관계를 형성할 수 있는데 보통은 다대다 관계를 사용

## Transaction

DB에서 데이터에 대한 하나의 논리적 실행 단계가 트랜잭션
DB가 더 효율적이고 정확하게 작동하게 하기 위해 ACID transaction을 사용

### ACID

DB 트랜잭션이 안전하게 수행된다는 것을 보장하기 위한 성질을 가리키는 약어

#### A: Atomicity, 원자성

트랜잭션 작업이 부분적으로 실행되다가 중단되지 않아야함
ex: 자금 이체라는 트랜잭션에서 자금 이체 자체는 성공 또는 실패가 가능하나, 보내는 것만 성공하고, 받는 것을 실패하는 것은 안돼

#### C: Consitency, 일관성

트랜잭션이 성공시 언제나 DB의 일관성이 유지되어야 함

#### I: Isolation, 독립성

트랜잭션 수행 시 다른 트랜잭션의 연산이 끼어들지 못하도록 함

트랜잭션 밖의 어떤 연산도 중간 데이터를 볼 수 없음

#### D: Durability, 지속성

성공적으로 수행된 트랜잭션은 영원히 반영되어야 함

## Stored Procedures(저장 프로시저)

RDBMS의 프로그래밍의 대부분은 저장 프로시저를 이용하여 구현됨

## 용어

### Tuple(record, row)

어떤 한 아이템을 대표하는 데이터셋

### Attribute(field, column)

instance에 귀속된 값

### Relation(Base relvar, table)

같은 attribute를 공유하는 tuple set
보통 table로 표현됨

### Dereived relvar(view, result set)

어떤 tuple의 set, query에 대한 응답

RDB에서는 모든 데이터가 관계를 통해 저장되고, 접근된다.

데이터를 저장하는 관계가 Relation이며 그것의 적용이 table.
데이터를 저장하지 않으나 관계 연산이 다른 관계에 적용 및 계산되는 관계가 derived relation이며 그것의 적용이 view, query임

이들은 다른 많은 관계에서 정보를 가져오나 하나의 관계로 작용하며, 추상 레이어로서 사용 가능함

#### Domain

도메인은 주어진 attribute에 대한 가능한 값들의 집합이다.

또는 attribute의 한계 값, 제한 값으로도 여겨질 수 있다.

## Constraints

constraint는 속성의 도메인을 제한시킴

constraint는 데이터가 관계에 저장되도록 데이터를 제한함

데이터가 constraint를 만족하는지를 나타내는 boolean값으로 표현(check constraints)

### Primary key

모든 관계/테이블은 PK를 가지며, 이것은 관계가 집합이 된 것의 결과물이다.
PK는 고유하게 튜플과 테이블을 특정한다

### Foregin key

foreign key는 다른 테이블의 PK column과 매치되는 attribute이다.

이것은 두계의 key를 관계맺는다

## Relational operation

### set operation

#### union

두 관계의 튜플들을 결합
= SQL UNION

#### intersection

두 관계의 공통된 튜플의 집합
= SQL INTERSECT

#### difference

차집합
= SQL EXCEPT or MINUS

#### cartesian product

두 번쨰 관계의 모든 튜플가 매치되는 튜플
= SQL Cross join

### others

#### selection

selection, restriction: 관계에서 tuple을 산출해내는 것.
특정 기준에 맞는 것 골라내기 (subset)
= SQL SELECT + WHERE

#### projection operation

extract specified attributes from a tuple or set of tuples

#### join operation

= SQL INNER JOIN

#### relational division
