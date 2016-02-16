var http = require("http");
var express = require("express");
var app = express();
var port = process.env.port || 5001;
 
var io = require('socket.io').listen(app.listen(port));
 
app.use(express.static(__dirname + '/public'));
 
app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html')
});
 
io.sockets.on('connection', function (socket) {
    socket.on('pirstatus', function (data) {
        io.sockets.emit('pirstatus', data);
    });

var socket = require('socket.io-client')('http://127.0.0.1:5001');
socket.emit('pirstatus', false);
var gpio = require("gpio");
var gpio4 = gpio.export(4, 
{
	direction: "in",
	ready: function() 
	{
		console.log('ready');
	}
});

gpio4.on("change", function(val) 
{
	console.log(val)
	if (val == 0) {
		socket.emit('pirstatus', false);   
	}
	else{
		socket.emit('pirstatus', true);   
	}
});




});
 
console.log("Listening on port " + port);


