# TypeORM에 대해서 알아봅시당.

express와 관계형 DB를 조합할 때 사용되는 ORM중 하나.
Data Mapper, Active Record 패턴 지원

<hr/>

## ORM은 뭐양

Object Relational Mapping

### 영속성(Persistence)

데이터를 생성한 프로그램이 **종료되어도 사라지지 않는** 데이터의 특성

영속성을 갖지 않는 데이터는 메모리에서만 존재하므로, 프로그램을 종료하면 모두 없어짐 (RAM 대신 HDD에 저장하면 안없어지는 그 느낌)

#### Object Persistence(영구적 객체)

메모리 상의 데이터를 파일 시스템, 관계형 데이터베이스 혹은 객체 데이터베이스 등을 활용하여 영구적으로 저장하여 영속성을 부여한다.

웹 앱이 CRUD로 데이터베이스에 저장하는 그 느낌

#### Persistence Layer

프로그램의 아키텍처에서, 데이터에 영속성을 부여하는 계층

Persistence Framework를 통해 개발 많이 함

#### Persistence Framework

SQL Mapper, ORM 등

### ORM이란.

Object Relational Mapping
객체 관계 매핑.

객체와 관계형 데이터베이스의 데이터를 **자동으로 매핑**해주는(짝짓는) 것을 말한다.

- 객체 지향 프로그래밍은 클래스를 사용하고, 관계형 데이터베이스는 **테이블**을 사용
- 객체 모델과 관계형 모델 간에 불일치가 존재
- ORM을 통해 객체 간의 관계를 바탕으로 SQL을 자동으로 생성하여 불일치를 해결

데이터베이스 데이터 <-매핑-> Object 필드

- 객체를 통해 간접적으로 데이터베이스 데이터를 다룸

Persistence API라고도 할 수 있음(그냥 객체를 RDB에 매핑해주는 API라고 생각하자)

### ORM의 장단점

#### 장점

**객체 지향적 코드로 더 직관적이고 비즈니스 로직에 집중 가능**

- ORM을 통해 SQL이 아닌 직관적 코드로 데이터를 조작하여 개발자가 객체 모델로 프로그래밍하는 것을 도와줌
- 선언문, 할당, 종료 등 부수적인 코드가 없거나 줄어듦
- 각종 객체에 대한 코드를 별도로 작성하여 코드의 가독성 증가
- SQL의 절차적 접근이 아닌 객체 지향적 접근이 가능

**재사용 및 유지보수 편리성 증가**

- ORM은 독립적으로 작성되어 있고, 해당 객체를 재활용 가능
- 때문에 모뎅레서 가공된 데이터를 컨트롤러에 의해 뷰와 합쳐지는 형태로 디자인 패턴을 견고하게 다지는데 유리
- 매핑 정보가 명확하여, ERD를 보는 것에 대한 의존도를 낮출 수 있음

**DBMS에 대한 종속성 감소**

- 객체 간의 관계를 바탕으로 SQL을 자동으로 생성하므로 RDBMS의 데이터 구조와 객체지향 모델 사이의 간격을 좁힐 수 있음
- 대부분 ORM 솔루션은 DB에 종속적이지 않음
- 예를 들어 DBMS를 교체하더라도 적은 리스크와 시간이 소요

#### 단점

**ORM으로만 완벽히 서비스를 구현하기 어려움**

- 사용은 편하나 설계는 신중하게 해야함
- 프로젝트의 복잡성이 커질 경우 난이도 또한 올라갈 수 있음
- 잘못 구현된 경우 속도 저하 및 심각할 경우 일관성이 무너지는 문제점
- 대형 쿼리는 속도를 위해 SP를 쓰는 등 튜닝이 필요할 수도 있음
- DBMS의 고유 기능을 이용하기가 어려움

**프로시저가 많은 시스템에서는 객체 지향적인 장점을 활용하기가 어려움**

### Obeject-Relational Impedance Mismatch

#### Granularity (세분성)

경우에 따라 DB의 테이블 수보다 더 많은 클래스를 가진 객체 모델이 있을 수 있음
예를 들어, Person 클래스에 멤버로 Address라는 클래스가 있는 경우, DB에는 person이라는 하나의 테이블에 Address를 저장할 수 있음

#### Inheritance (상속)

RDBMS에는 상속의 개념이 없다

#### Identity (일치)

RDBMS는 sameness라는 하나의 개념을 확실히 정의하는데 이것이 바로 primary key
(PK가 같아야 동일)

but OOP에서는 객체 식별(a==b)와 객체 동일성(a.equals(b))를 모두 정의

#### Associations (연관성)

객체 지향 언어는 reference를 사용하여 연관성을 나타내지만 RDBMS는 foreign key를 이용하여 나타냄

#### Navigation (탐색/순회)

OOP: 하나의 연결에서 다른 연결로 이동하며 탐색 및 순회
RDBMS: 원하는 대상 엔터티를 select

<hr/>

## Active Record 패턴

모델 자체에 쿼리 메소드를 정의하고, 모델의 메소드를 사용하여 객체를 저장, 제거, 불러오는 방식

**공식 Docs의 예제코드**

```ts
import { BaseEntity, Entity, PrimaryGeneratedColumn, Column } from 'typeoprm';

@Entity()
export class User extends BaseEntity {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	firstName: string;

	@Column()
	lastName: string;

	@Column()
	isActive: boolean;

	static findByName(firstName: string, lastName: string) {
		return this.createQueryBuilder('user')
			.where('user.firstName = :firstName', { firstName })
			.andWhere('user.lastName = :lastName', { lastName })
			.getMany();
	}
}
```

<code>BaseEntity</code> 클래스를 상속한 후 사용 가능

JS의 방식으로 DB를 다루는 편리함 ↓

```js
// save example
const user = new User();
user.firstName = 'Timber';
user.lastName = 'Saw';
user.isActive = true;
await user.save();

// remove example
await user.remove();

// load example
// User라는 클래스 자체가 DB가 되는 듯 하다.
const users = await User.find({ skip: 2, take: 5 });
const newUsers = await User.find({ isActive: true });
const timber = await User.findOne({ firstName: 'Timber', lastName: 'Saw' });
const timber = await User.findByName('Timber', 'Saw');
```

## Data Mapper 패턴

분리된 클래스에 쿼리 메소드를 정의하며, Repository를 이용해 객체를 저장, 제거, 불러온다.

모델에 접근하는 방식이 아니라 Repository에서 데이터에 접근

**공식 Docs의 예제 코드**

클래스 정의

```ts
import { Entity, PrimaryGeneratedColumn, Column } from 'typeorm';

@Entity
export class User {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	firstName: string;

	@Column()
	lastName: string;

	@Column()
	isActive: boolean;
}
```

정의한 클래스를 Generic 타입을 이용해 상속

```js
import { EntityRepository, Repository } from 'typeorm';
import { User } from '../entity/User';

@EntityRepository()
export class UserRepository extends Repository<User> {
	findByName(firstName: string, lastName: string) {
		return this.createQueryBuilder('user')
			.where('user.firstName = :firstName', { firstName })
			.andWhere('user.lastName = "lastName', { lastName })
			.getMany();
	}
}
```

이후 <code>getRepository()</code>를 사용하여 만들어진 모델 사용

```js
const userRepository = connection.getRepository(User);

// save example
const user = new User();
user.firstName = 'Timber';
user.lastName = 'Saw';
user.isActive = true;
await userRepository.save(user);

// remove example
await userRepository.remove(user);

// load example
const users = await userRepository.find({ skip: 2, take: 5 });
const newUsers = await userRepository.find({ isActive: true });
const timber = await userRepository.findOne({ firstName: 'Timber', lastName: 'Saw' });
```

대충 전자는 모델 자체에 쿼리가 정의된 것.

후자는 모델과 쿼리를 분리하는 것.

## 그럼 어떤 패턴 ?

- Active Record: 규모가 작은 애플리케이션
- Data Mapper: 규모가 큰 애플리케이션, 유지 보수에 적합

## Tutorial

typeorm을 글로벌하게 설치

```sh
yarn global add typeorm
```

CRA처럼 간단하게 init해보기

```sh
# typeorm init --name 프로젝트명 --database 데이터베이스명
typeorm init --name backend --database postgres
```

이후 위에서 본 User 예시 코드와 함께 프로젝트 폴더가 생성된다.

프로젝트 폴더에는 <code>tsconfig.json</code>, <code>package.json</code> 등등이 있고, <code>ormconfig.json</code>에 typeORM 설정이 담겨있음.

```json
{
	"type": "데이터베이스 타입",
	"host": "localhost",
	"port": 5432,
	"username": "test",
	"password": "test",
	"database": "test",
	.
	.
	.
}
```
여기서 username, password, database만 만져주면 설정 끝. 
