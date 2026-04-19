const express = require	('express');
const app = express();

app.use(express.json());

let users = [
	{id:1, name: "alpha"},
	{id:2, name: "Sharma"}

app.get('/users', (req, res) => {
	res.send('API is runing....');
	res.json(users);
});

app.post('/users', (req, res) => {
	const newUser = {
		id : users.length +1,
		name: req.body.name
	};
	users.push(newUser);
	res.status((201).json(newUser);

});

//server 
app.listen(3000, () => {
	console.log('Server running on port 3000');
});
