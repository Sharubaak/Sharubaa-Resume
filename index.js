var connect = require('connect');
var http = require('http');
 
var app = connect();
 function Aboutme(req,res,next)
{
    res.setHeader('Content-Type','text/plain');
    res.end('Hi, My name is sharubaa');

}

function Projects(req,res,next)
{
    res.setHeader('Content-Type','text/plain');
    res.end('These are my projects');

}

//create node.js http server and listen on port
app.use('/Aboutme',Aboutme)
app.use('/Projects',Projects)
http.createServer(app).listen(3000);
console.log('Server is running')