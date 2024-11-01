const express = require('express')
const app = express()
const port = 3000

app.get('/AboutMe', (req, res) => {
  res.send('Hello!')
})

app.get('/Projects', (req, res) => {
    res.send('These are a couple of projects I like to show')
  })
  app.get('/Contactus', (req, res) => {
    res.send('If you have any questions do not hestitate. Send me a message down below or contact me on my email')
  })

  app.get('/AboutMe', (req, res) => {
    res.send('Hello!')
  })
app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})