# TypeORM에 대해서 알아봅시당.

express와 관계형 DB를 조합할 때 사용되는 ORM중 하나.
Data Mapper, Active Record 패턴 지원

## ORM은 뭐양

Object Relational Mapping

### 영속성(Persistence)

데이터를 생성한 프로그램이 **종료되어도 사라지지 않는** 데이터의 특성

영속성을 갖지 않는 데이터는 메모리에서만 존재하므로, 프로그램을 종료하면 모두 없어짐

#### Object Persistence(영구적 객체)

## Active Record 패턴

모델 자체에 쿼리 메소드를
