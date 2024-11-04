const express = require('express');
const app = express();
const port = process.env.PORT || 3000; // Use the PORT environment variable provided by Heroku, or default to 3000

// Define a route for the root URL
app.get('/', (req, res) => {
  res.send('Welcome to my portfolio!'); // Message to display at the root URL
});

// Define other routes
app.get('/AboutMe', (req, res) => {
  res.send('Hello!');
});

app.get('/Projects', (req, res) => {
  res.send('These are a couple of projects I like to show.');
});

app.get('/Contactus', (req, res) => {
  res.send('If you have any questions, do not hesitate. Send me a message down below or contact me on my email.');
});

// Start the server
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});