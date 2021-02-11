# [관계형 데이터베이스](https://en.wikipedia.org/wiki/Relational_database)

**관계형 데이터베이스(Relational DataBase)**는 **관계형 모델(Relational Model)**에 기반한 데이터베이스이다.
관계형 DB를 관리하기 위해 **RDBMS(Relational DataBase Management System)**이라는 소프트웨어 시스템을 사용

DB에 질의 및 관리를 위해 **SQL(Structured Query Language)**를 사용하기도 함

## 관계형 모델 
**관계형 모델**은 데이터를 1개 이상의, column(attribute)과 row, row(record, tuple)를 식별할 unique한 key들로 이루어진 테이블(또는 관계)로 표현한다 
일반적으로 각각의 table(relation)은 하나의 entity type(하나의 데이터 타입)을 대표한다.

ex로 entity type이 한 사람이라고 할 때,
- row는 각 entity type의 instance를 표현한다(ex: Lee) 
- column은 instance에 귀속된 값을 나타낸다(ee: 성씨)