# PostgreSQL

## 설치

```sh
brew install postgresql
```

## get up and running

```sh
brew services start postgresql
brew services stop postgresql
```

## PostgreSQL command prompt

just connect to the default postgres DB with the default login information (no option flags)

```sh
psql postgres
```

ends with # : root, superuser

command starts with \
ex: 연결 정보 보기

```sh
postgres=# \conninfo
You are connected to database "postgres" as user "overthestream" via socket in "/tmp" at port "5432".
```

- \q : Exit
- \c : connect to new database
- \dt: List all tables
- \du: List all roles
- \list : List databases

### creating a role

```sh
postgres=# CREATE ROLE rolename WITH LOGIN PASSWORD 'password';
```

role to be able to create a DB

```sh
postgres=# ALTER ROLE role CREATEDB;
```

connect postgres with new role

```
postgres=# \q
psql -d postgres -U role
```

### creating a DB

```sh
CREATE DATABASE dbname;
postgres=> \c dbname
You are now connected to database "api" as user "tutorial".
dbname=>
```

### creating a table

**ex**
```sh
api=>
CREATE TABLE users(
  ID SERIAL PRIMARY key 

)
```