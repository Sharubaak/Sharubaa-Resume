var connect = require('connect');
 
var app = connect();
 function 

// respond to all requests
app.use(function(req, res){
  res.end('Hello\n');
});
 
//create node.js http server and listen on port
http.createServer(app).listen(3000);