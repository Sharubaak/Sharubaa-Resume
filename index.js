const express = require('express');
const app = express();
const port = process.env.PORT || 3000; // Use the dynamic port provided by Heroku

app.get('/AboutMe', (req, res) => {
  res.send('Hello!');
});

app.get('/Projects', (req, res) => {
  res.send('These are a couple of projects I like to show');
});

app.get('/Contactus', (req, res) => {
  res.send('If you have any questions, do not hesitate to send me a message or contact me via email');
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
