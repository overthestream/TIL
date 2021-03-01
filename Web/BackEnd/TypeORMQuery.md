# QueryBuilder

## How To Create & Use QueryBuilder

세가지 예시

### Create

#### Using Connection

```js
const user = await getConnection()
	.createQueryBuilder()
	.select('user')
	.from(User, 'user')
	.where('user.id = :id', { id: 1 })
	.getOne();
```

#### Using Entity Manager

```js
import { getManager } from 'typeorm';

const user = await getManager()
	.createQueryBuilder(User, 'user')
	.where('user.id = :id', { id: 1 })
	.getOne();
```

#### Using Repository

```js
import { getRepository } from 'typeorm';

const user = await getRepository(User)
	.createQueryBuilder('user')
	.where('user.id = :id', { id: 1 })
	.getOne();
```

### Use

#### SELECT

```js
import { getConnection } from 'typeorm';

const user = await getConnection()
	.createQueryBuilder()
	.select('user')
	.from(User, 'user')
	.where('user.id = :id', { id: 1 })
	.getOne();
```

#### INSERT

```js
import { getConnection } from 'typeorm';

await getConnection()
	.createQueryBuilder()
	.insert()
	.into(User)
	.values([
		{ firstName: 'Timber', lastName: 'Saw' },
		{ firstName: 'Phantom', lastName: 'Lancer' },
	])
	.execute();
```

#### UPDATE

```js
import { getConnection } from 'typeorm';

await getConnection()
	.createQueryBuilder()
	.update(User)
	.set({ firstName: 'Timber', lastName: 'Saw' })
	.where('id = :id', { id: 1 })
	.execute();
```

#### DELETE

```js
import { getConnection } from 'typeorm';

await getConnection()
	.createQueryBuilder()
	.delete()
	.from(User)
	.where('id = :id', { id: 1 })
	.execute();
```

## Get Value Using Query Builder

값을 하나만 얻을 때: getOne

```js
const timber = await getRepository(User)
	.createQueryBuilder('user')
	.where('user.id = :id OR user.name = :name', { id: 1, name: 'Timber' })
	.getOne();
```

실패 시 에러를 throw 할 때: getOneOrFail

```js
const timber = await getRepository(User)
	.createQueryBuilder('user')
	.where('user.id = :id OR user.name = :name', { id: 1, name: 'Timber' })
	.getOneOrFail();
```

여러 개 가져올 때: getMany

```js
const users = await getRepository(User).createQueryBuilder('user').getMany();
```

raw한 result를 얻기: getRawOne, getRawMany
(위의 getOne등은 entity를 얻기)

```js
const { sum } = await getRepository(User)
	.createQueryBuilder('user')
	.select('SUM(user.photosCount)', 'sum')
	.where('user.id = :id', { id: 1 })
	.getRawOne();

const photosSums = await getRepository(User)
	.createQueryBuilder('user')
	.select('user.id')
	.addSelect('SUM(user.photosCount)', 'sum')
	.groupBy('user.id')
	.getRawMany();

// result will be like this: [{ id: 1, sum: 25 }, { id: 2, sum: 13 }, ...]
```

## CreateQueryBuilder의 파라미터

```js
createQueryBuilder('user') === createQueryBuilder().select('user').from(User, 'user');
```

## Where의 Parameter

```js
.where("user.name = :name", { name: "Timber" })
```

==

```js
.where("user.name = :name")
.setParameter("name", "Timber")
```

```js
.where("user.name IN (:...names)", { names: [ "Timber", "Cristal", "Lina" ] })
```

AND 사용

```js
createQueryBuilder("user")
    .where("user.firstName = :firstName", { firstName: "Timber" })
    .andWhere("user.lastName = :lastName", { lastName: "Saw
```

OR 사용

```js
createQueryBuilder('user')
	.where('user.firstName = :firstName', { firstName: 'Timber' })
	.orWhere('user.lastName = :lastName', { lastName: 'Saw' });
```

## 순서 추가

```js
createQueryBuilder('user').orderBy('user.id');
```
