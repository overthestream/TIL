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

**ex: table called users with three fields: two VARCHAR & an auto-incrementing PRIMARY KEY**

```sh
api=>
CREATE TABLE users(
  ID SERIAL PRIMARY key
  name VARCHAR(30)
  email VARCHAR(30)
);
```

**add users**

```sh
INSERT INTO users (name, email)
  VALUES ('Jerry','jerry@example.com'), ('George','george@example.com);
```

### Express.js server 만들기

```sh
mkdir node-api-postgres
cd node-api-postgres
yarn init
yarn add express pg
```

make <code>index.js</code>

```js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(
	bodyParser.urlencoded({
		extended: true,
	})
);

app.get('/', (req, res) => {
	res.json({ info: 'Node.js, Express, and Postgres API' });
});

app.listen(port, () => {
	console.log(`App running on port: ${port}.`);
});
```

### connect postgres & node.js

node-postgres module(package: pg)

<code>query.js</code>

```js
const Pool = require('pg').Pool;
const pool = new Pool({
	user: 'tutorial',
	host: 'localhost',
	database: 'api',
	password: 'password',
	port: 5432,
});
```

### CRUD: Create

ex: create all the functions for each route

- GET - / | displayHome()
- GET - /users | getUsers()
- GET - /users/:id | getUserById()
- POST - users | createUser()
- PUT - /users/:id | updateUser()
- DELETE - /users/:id | deleteUser()

<code>qury.js</code>

```js
const Pool = require('pg').Pool;
const pool = new Pool({
	user: 'tutorial',
	host: 'localhost',
	database: 'api',
	password: 'password',
	port: 5432,
});
const getUsers = (request, response) => {
	pool.query('SELECT * FROM users ORDER BY id ASC', (error, results) => {
		if (error) {
			throw error;
		}
		response.status(200).json(results.rows);
	});
};

const getUserById = (request, response) => {
	const id = parseInt(request.params.id);

	pool.query('SELECT * FROM users WHERE id = $1', [id], (error, results) => {
		if (error) {
			throw error;
		}
		response.status(200).json(results.rows);
	});
};

const createUser = (request, response) => {
	const { name, email } = request.body;

	pool.query('INSERT INTO users (name, email) VALUES ($1, $2)', [name, email], (error, results) => {
		if (error) {
			throw error;
		}
		response.status(201).send(`User added with ID: ${result.insertId}`);
	});
};

const updateUser = (request, response) => {
	const id = parseInt(request.params.id);
	const { name, email } = request.body;

	pool.query(
		'UPDATE users SET name = $1, email = $2 WHERE id = $3',
		[name, email, id],
		(error, results) => {
			if (error) {
				throw error;
			}
			response.status(200).send(`User modified with ID: ${id}`);
		}
	);
};

const deleteUser = (request, response) => {
	const id = parseInt(request.params.id);

	pool.query('DELETE FROM users WHERE id = $1', [id], (error, results) => {
		if (error) {
			throw error;
		}
		response.status(200).send(`User deleted with ID: ${id}`);
	});
};

module.exports = {
	getUsers,
	getUserById,
	createUser,
	updateUser,
	deleteUser,
};
```

### Set CRUD in a REST API

<code>index.js</code>

```js
const db = require('./query');

app.get('/users', db.getUsers);
app.get('/users/:id', db.getUserById);
app.post('/users', db.createUser);
app.put('/users/:id', db.updateUser);
app.delete('/users/:id', db.deleteUser);
```

**to get users**
: http://localhost:3000/users

(by Id)
: http://localhost:3000/users/1

**POST**
use curl

```sh
curl --data "name=Elaine&email=elaine@example.com"
http://localhost:3000/users
```

**PUT**

```sh
curl -X PUT -d "name=Kramer" -d "email=kramer@example.com" http://localhost:3000/users/1
```

**DELETE**

```sh
curl -X "DELETE" http://localhost:3000/users/1
```
