var express = require('express');
app = express();
server = require('http').createServer(app);
io = require('socket.io').listen(server);
var port = 5000; 
server.listen(port);
app.use(express.static('public'));
 
var brightness = 50;
 
io.sockets.on('connection', function (socket) 
{
	socket.emit('led1', {value: brightness});
	socket.emit('led2', {value: brightness});
	socket.emit('led3', {value: brightness});
	
	socket.on('led1', function (data) 
	{
		brightness = data.value;
		//console.log(brightness);
		//var buf = new Buffer(1);
		//buf.writeUInt8(brightness, 0);
		io.sockets.emit('led1', {value: brightness});   
	});
	socket.on('led2', function (data) 
	{
		brightness = data.value;
		//console.log(brightness);
		//var buf = new Buffer(1);
		//buf.writeUInt8(brightness, 0);
		io.sockets.emit('led2', {value: brightness});   
	});
	
	socket.on('led3', function (data) 
	{
		brightness = data.value;
		//console.log(brightness);
		//var buf = new Buffer(1);
		//buf.writeUInt8(brightness, 0);
		io.sockets.emit('led3', {value: brightness});   
	});	

});
console.log("running on port: *." + port);
