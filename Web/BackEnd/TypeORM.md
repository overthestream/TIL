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

## Decorator

### ref

https://yangeok.github.io/orm/2020/12/14/typeorm-decorators.html

### Entity

#### Entity

데이터베이스 테이블을 정의하기 전에 실행해야하는 데코레이터

기본적으로 테이블 명을 클래스 명으로 매핑

옵션 추가적 지정 가능

- name: 테이블명
- database: DB명
- schema: schema명
- engine: DB엔진명
- synchronize: false시 schema 싱크를 건너뜀
- orderBy: QueryBuilder, find시 엔티티 기본순서 지정

```js
@Entity() // 옵션 X
@Entity('User') // 문자열만 주면 name 인수가 됨
@Entity({ // 객체 형식으로 옵션 전달 가능
	name: 'User',
	engine: 'MyISAM',
	database: 'exambple_dev',
	schema: 'schema_with_best_tables',
	synchronize: false,
	orderBy {
		name: 'ASC', // 오름차순
		id: 'DESC' // 내림차순
	}
})
```

#### Entity inheritance

공통된 테이블 필드의 중복을 없애기

##### Concrete table inheritance

중복된 칼럼 => 베이스가 되는 추상 클래스를 선언한 후 확장

**ex**

```js
abstract class Content {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	title: string;

	@Column()
	description: string;
}

@Entity()
export class Question extends Content {
  @Column()
  answersCount: number
}

@Entity()
export class Post extends Content {
  @Column()
  viewCount: number
}
```

##### Single table inheritance

<code>@TableInheritance()</code>, <code>@ChildEntity</code> 사용

데이터베이스에 부모 테이블이 생성됨

모든 ChldEntity가 부모 테이블에 들어감

**Single**인 이유가 있다 그죠

```js
@Entity()
@TableInheritance({ column: { type: 'varchar', name: 'type' } })
class Content {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	title: string;

	@Column()
	description: string;
}

@ChildEntity()
export class Photo extends Content {
	@Column()
	size: string;
}

@ChildEntity()
export class Question extends Content {
	@Column()
	answersCount: number;
}

@ChildEntity()
export class Post extends Content {
	@Column()
	viewCount: number;
}
```

##### Embedded entities

이름이 비슷하고 타입이 같은 칼럼을 묶는 패턴

User.name은 User.nameFirst, User.nameLast로 분기

```js
export class Name {
	@Coulmn()
	first: string;

	@Column()
	last: string;
}

@Entity()
export class User {
	@PrimaryGeneratedColumn()
	id: string;

	@Column((type) => Name)
	name: Name;

	@Column()
	isActive: boolean;
}
```

#### ViewEntity

##### SQL view란

view는 가상 테이블로, 실제 데이터가 저장되는 것은 아니지만 view를 통해 데이터를 가상 테이블로 관리가 가능

1개의 view로 여러 테이블의 데이터를 조회할 수 있음

복잡한 쿼리를 간단한 쿼리로 압축 가능

데코레이터에는 <code>@Entity()</code>와 달리

name, database, schema, expression(view를 정의)가 인자로 들어감

expression에는 SQL 쿼리문이나 QueryBuilder에 체이닝할 수 있는 메서드가 들어갈 수 있음

### Column

#### Column

entity의 속성을 테이블 칼럼으로 표시

#### IdColumn

@Column()의 옵션인 primary를 대체. PK를 만듦

##### PrimaryGeneratedColumn

자동 생성되는 ID값을 표현하는 방식을 아래와 같이 2가지 옵션을 사용할 수 있도록 도와줌

increment: 기본 옵션, 1씩 증가하는 아이디
uuid: 유니크한 uuid사용

```js
// using increment
@Entity()
export class User {
	@PrimaryGeneratedColumn()
	id: number;
}

// using uuid
@Entity()
export class User {
	@PrimaryGeneratedColumn('uuid')
	id: string;
}
```

##### Generated

PK로 쓰는 ID외에 추가로 uuid를 기록하기 위해서 사용

```js
@Entity()
export class User {
	@Column()
	@Generated('uuid')
	uuid: string;
}
```

#### DateColumn

##### CreateDateColumn

칼럼이 추가된 시각을 자동으로 기록, 옵션을 적지 않을 시 datetime 타입으로 기록

```js
@Entity()
export class User {
	@CreateDateColumn()
	createdAt: Date;
}
```

##### UpodateDateColumn

칼럼이 수정된 시각을 자동으로 기록, 옵션을 적지 않을 시 datetime 타입으로 기록

```js
@Entity()
export class User {
	@UpdateDateColumn()
	updatedAt: Date;
}
```

##### DeleteDateColumn

**sodt delete란?**

- 데이터 열을 실제로 삭제하지 않고, 삭제 여부를 나타내는 칼럼인 deletedAt을 사용
- 일반적인 삭제 대신 삭제된 열을 갱신하는 UPDATE문을 사용
- 시각이 기록되지 않은 열들만 필터해서 쿼리하도록 도와줌
- 다른 테이블과 JOIN시 항상 삭제된 열을 검사하므로 성능이 하락
- 복구하거나 예전 기록을 확인하고자 할 때 간편

```js
@Entity()
export class User {
	@DeleteDateColumn()
	deletedAt: Date;
}
```

### Relation

일대일, 일대다, 다대다 관계 등

#### OneToOne

예시로 User와 Profile 테이블

1:1 관계, User에서 target relation type을 Profile로, Profile에서 target relation type을 User로 지정.

<code>@JoinColumn()</code>을 사용한 필드는 FK로 타겟 테이블에 등록됨(반드시 한쪽 테이블에서만 사용해야 함)

관계는 단방향과 양방향 모두 작성 가능(uni-directional, bi-directional)

```js
@Entity()
export class Profile {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	gender: string;

	@Column()
	photo: string;

	@OneToOne(() => User, (user) => user.profile)
	user: User;
}

@Entity()
export class User {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	name: string;

	@OneToOne((type) => Profile, (profile) => profile.user)
	@JoinColumn()
	profile: Profile;
}
```

```
+-------------+--------------+----------------------------+
|                        profile                          |
+-------------+--------------+----------------------------+
| id          | int(11)      | PRIMARY KEY AUTO_INCREMENT |
| gender      | varchar(255) |                            |
| photo       | varchar(255) |                            |
| userId      | int(11)      | FOREIGN KEY                |
+-------------+--------------+----------------------------+

+-------------+--------------+----------------------------+
|                          user                           |
+-------------+--------------+----------------------------+
| id          | int(11)      | PRIMARY KEY AUTO_INCREMENT |
| name        | varchar(255) |                            |
| profileId   | int(11)      | FOREIGN KEY                |
+-------------+--------------+----------------------------+
```

DESC문에서 이런 st로 나온다 .

이를 검색하기 위해서는 관계를 지정하는 작업도 필요

```js
// using find* method
const userRepo = connection.getRepository(User);
const users = await userRepo.find({ relations: ['profile'] });

// using query builder
const users = await connection
	.getRepository(User)
	.createQueryBuilder('user')
	.leftJoinAndSelect('user.profile', 'profile')
	.getMany();
```

#### ManyToOne/OneToMany

예시로 User와 Photo 테이블

1:N 관계

```js
@Entity()
export class User {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	name: string;

	@OneToMany((type) => Photo, (photo) => photo.user)
	photos: Photo[];
}

@Entity()
export class Photo {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	url: string;

	@ManyToOne((type) => User, (user) => user.photos)
	user: User;
}
```

@OneToMany()/@ManyToOne()에서는 @JoinColumn()을 생략할 수 있음.
@OneToMany()는 @ManyToOne()이 없으면 안됩니다. 하지만 반대로 @ManyToOne()은 @OneToMany()이 없어도 정의할 수 있습니다.
@ManyToOne()을 설정한 테이블에는 relation id가 외래키를 가지고 있게 됩니다.

DESC

```
+-------------+--------------+----------------------------+
|                         photo                           |
+-------------+--------------+----------------------------+
| id          | int(11)      | PRIMARY KEY AUTO_INCREMENT |
| url         | varchar(255) |                            |
| userId      | int(11)      | FOREIGN KEY                |
+-------------+--------------+----------------------------+

+-------------+--------------+----------------------------+
|                          user                           |
+-------------+--------------+----------------------------+
| id          | int(11)      | PRIMARY KEY AUTO_INCREMENT |
| name        | varchar(255) |                            |
+-------------+--------------+----------------------------+
```

마찬가지로 검색을 위해서는 관계를 지정해줘야 함

```js
// using find* method
const userRepository = connection.getRepository(User);
const users = await userRepository.find({ relations: ['photos'] });
// or from inverse side
const photoRepository = connection.getRepository(Photo);
const photos = await photoRepository.find({ relations: ['user'] });

// using query builder
const users = await connection
	.getRepository(User)
	.createQueryBuilder('user')
	.leftJoinAndSelect('user.photos', 'photo')
	.getMany();
// or from inverse side
const photos = await connection
	.getRepository(Photo)
	.createQueryBuilder('photo')
	.leftJoinAndSelect('photo.user', 'user')
	.getMany();
```

#### ManyToMany

예시로 Category와 Question,
M:N 관계

```js
@Entity()
export class Category {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	name: string;
}

@Entity()
export class Question {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	title: string;

	@Column()
	text: string;

	@ManyToMany(() => Category)
	@JoinTable()
	categories: Category[];
}
```

<code>@JoinTable()</code>이 반드시 필요하며 한쪽에만 넣어주면 됨

DESC

```
+-------------+--------------+----------------------------+
|                        category                         |
+-------------+--------------+----------------------------+
| id          | int(11)      | PRIMARY KEY AUTO_INCREMENT |
| name        | varchar(255) |                            |
+-------------+--------------+----------------------------+

+-------------+--------------+----------------------------+
|                        question                         |
+-------------+--------------+----------------------------+
| id          | int(11)      | PRIMARY KEY AUTO_INCREMENT |
| title       | varchar(255) |                            |
| text        | varchar(255) |                            |
+-------------+--------------+----------------------------+

+-------------+--------------+----------------------------+
|              question_categories_category               |
+-------------+--------------+----------------------------+
| questionId  | int(11)      | PRIMARY KEY FOREIGN KEY    |
| categoryId  | int(11)      | PRIMARY KEY FOREIGN KEY    |
+-------------+--------------+----------------------------+
```

마찬가지로 관계 지정이 필요

```js
// using find* method
const questionRepository = connection.getRepository(Question);
const questions = await questionRepository.find({ relations: ['categories'] });

// using query builder
const questions = await connection
	.getRepository(Question)
	.createQueryBuilder('question')
	.leftJoinAndSelect('question.categories', 'category')
	.getMany();
```

#### Tree entity

셀프 조인이란 1개의 테이블에서 부모-자식 관계를 나타낼 수 있는 패턴

4가지 패턴으로 지원

자기 참조 구조체 이런거네요 그쵸

##### Adjacency list

자기 참조를 @ManyToOne(), @OneToMany() 데코레이터로 표현

```js
@Entity()
export class Category {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	name: string;

	@Column()
	description: string;

	@ManyToOne((type) => Category, (category) => category.children)
	parent: Category;

	@OneToMany((type) => Category, (category) => category.parent)
	children: Category[];
}
```

##### Nested Set

@Tree(), @TreeChildren(), @TreeParent()를 사용

쓰기에는 비효율적, 여러개의 루트를 가질 수 없으며,
인자로 'nested-set'이 들어감

```js
@Entity()
@Tree('nested-set')
export class Category {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	name: string;

	@TreeChildren()
	children: Category[];

	@TreeParent()
	parent: Category;
}
```

##### Materialized path

구체화된 경로 혹은 경로 열거라고 부릅니다. 간단하고 효율적입니다. nested set과 사용방법은 같습니다. @Tree()의 인자로 materialized-path이 들어갑니다.

##### Closure table

부모와 자식 사이의 관계를 분리된 테이블에 특별한 방법으로 저장

nested set과 사용방법은 같습니다. @Tree()의 인자로 closure-table이 들어갑니다.

#### JoinColumn/JoinTable

아래는 아래 2개의 데코레이터에 공통으로 사용할 수 있는 옵션입니다.

- eager 옵션이 있어서 N+1 문제를 제어할 수 있음
- cascade, onDelete 옵션이 있어 관계가 연결된 객체를 추가/수정/삭제되도록 할 수 있음. 버그를 유발할 수 있으니 주의해서 사용하는 것이 좋음

##### JoinColumn

@JoinColumn()을 사용시 테이블에 자동으로 칼럼명과 참조 칼럼명을 합친 이름의 칼럼을 만듦

```js
@Entity()
export class Post {
	@ManyToOne((type) => Category)
	@JoinColumn({
		name: 'category_id',
		referencedColumnName: 'name',
	})
	category: Category;
}

@Entity()
export class Category {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	name: string;
}
```

##### JoinTable

M:N 연결 테이블

```js
@Entity()
export class Question {
	@ManyToMany((type) => Category)
	@JoinTable({
		name: 'question_categories',
		joinColumn: {
			name: 'question',
			referencedColumnName: 'id',
		},
		inverseJoinColumn: {
			name: 'category',
			referencedColumnName: 'id',
		},
	})
	categories: Category[];
}

@Entity()
export class Category {
	@PrimaryGeneratedColumn()
	id: number;

	@Column()
	name: string;
}
```

#### RelationId

```js
// using many to one
@Entity()
export class Post {
	@ManyToOne((type) => Category)
	category: Category;

	@RelationId((post: Post) => post.category)
	categoryId: number;
}

// using many to many
@Entity()
export class Post {
	@ManyToMany((type) => Category)
	categories: Category[];

	@RelationId((post: Post) => post.categories)
	categoryIds: number[];
}
```

#### Subscriber

CRUD 이벤트 발생을 리슨

다음과 같은 데코레이터들을 가지고 있습니다.
@AfterLoad, @AfterInsert, @BeforeInsert, @AfterUpdate, @BeforeUpdate, @AfterRemove, @BeforeRemove

### Index/Unique/Check

#### Index

테이블 쿼리 속도를 올려줌
테이블 내 1개 혹은 그 이상의 칼럼으로 생성
키 필드 외 다른 것이 없으므로 보통보다 적은 공간 차지
인덱싱(빠르게 값 찾기)위해 사용

```js
// using with single column
@Entity()
export class User {
	@Index()
	@Column()
	firstName: string;

	@Index({ unique: true })
	@Column()
	lastName: string;
}

// using with entity
@Entity()
@Index(['firstName', 'lastName'], { unique: true })
export class User {
	@Column()
	firstName: string;

	@Column()
	lastName: string;
}
```

#### Unique

특정 칼럼에 고유키 제약 조건을 생성

```js
@Entity()
@Unique(['firstName', 'lastName'])
export class User {
	@Column()
	firstName: string;

	@Column()
	lastName: string;
}
```

#### Check

테이블에서 데이터 추가 쿼리가 날아오면 값을 체크

```js
@Entity()
@Check('"age" > 18')
export class User {
	@Column()
	firstName: string;

	@Column()
	firstName: string;

	@Column()
	age: number;
}
```

### Transaction

트랜잭션이란 
DB 내에서 하나의 그룹으로 처리해야하는 명령문을 모아서 처리하는 작업의 단위 
