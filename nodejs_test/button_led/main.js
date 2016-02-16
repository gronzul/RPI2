var app = require('http').createServer(handler);
var io = require('socket.io').listen(app);
var fs = require('fs');
var sock;
var port = 5002;

app.listen(port, function()
{
 console.log('listening on *.'+ port);
});

/*
var express = require('express');
app = express();
server = require('http').createServer(app);
io = require('socket.io').listen(server);
 
var sock;
var port = 5002;

server.listen(port);
app.use(express.static('public'));
console.log('listening on *.'+ port);*/

// button is attaced to pin 18, led to 17
var GPIO = require('onoff').Gpio;
var ledGiallo = new GPIO(25, 'out');
var ledVerde = new GPIO(24, 'out');
var button = new GPIO(23, 'in', 'both');

//Init LED to off
ledVerde.writeSync(0);
ledGiallo.writeSync(0);

Led_Status="";
Colore=""; 

 
function handler (req, res) 
{
  fs.readFile('./public/index.html',
  function (err, data) {
    if (err) {
      res.writeHead(500);
      return res.end('Error loading index.html');
    }
    res.writeHead(200);
    res.end(data);
  });
}

  // pass the callback function to the
  // as the first argument to watch() and define
  // it all in one step
  button.watch(function(err, state) 
  {
    //console.log('button.watch');
    // check the state of the button
    // 1 == pressed, 0 == not pressed
    if(state == 1) {
    // turn LED on
      //console.log('LED on');
      ledVerde.writeSync(0);
      if (sock) {
        sock.emit('doled','', 'green');
      };
          
    } else {
      // turn LED off
      //console.log('LED off');
      ledVerde.writeSync(1);
      if (sock) {
        sock.emit('doled','','red');
      };
    }
  });

var led = '';
var color = 'orange';


io.on('disconnect', function (socket) 
{
	console.log('on disconnection:', socket.request.connection._peername);
});

io.on('connection', function (socket) 
{
	sock = io.sockets; 
	io.sockets.emit('doled',led, color);
	//console.log('Socket succesfully connected with remoteAddress: '+socket.request.connection.remoteAddress);
	//console.log('Socket id:' + socket.id);
	console.log('connection :', socket.request.connection._peername);
	
	socket.on('slider', function (data) 
	{
		brightness = data.value;
		io.sockets.emit('slider', {value: brightness});   
		//console.log(data.value);
	}); 
  
	socket.on('doled', function (led, color)   
	{
		if (led =='lv1'){
			ledVerde.writeSync(1); 
			}
		if (led =='lv0'){
			ledVerde.writeSync(0); 
			}
		if (led =='lg1'){
			ledGiallo.writeSync(1); 
			}
		if (led =='lg0'){
			ledGiallo.writeSync(0); 
			}			
		io.sockets.emit('doled',led, color);
		//console.log("Led:" + led + " Color:" + color);
	});
});
