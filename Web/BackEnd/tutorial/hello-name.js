const express = require('express'); // import express as express 이런 느낌?
const app = express(); // app은 express 의 instance, 즉 express app을 만들어 app에 저장
const port = 3000; // port: 3000 에서 구동되는 앱

app.get('/name/:user_name', function (req, res) {
	res.status(200);
	res.set('Content-type', 'text/html');
	res.send('<html><body>' + '<h1>Hello ' + req.params.user_name + '</h1>' + '</body></html>');
});

app.listen(port, () => {
	console.log(`Example app listening at http://localhost:${port}`);
});
