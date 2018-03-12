var express = require('express');
var app = express();
var server = app.listen(3000);
app.use(express.static('public'));

console.log("this server is now running.");
var socket = require('socket.io');
var io = socket(server);
io.sockets.on('connection', newConnection);
var PythonShell = require('python-shell');

function newConnection(socket){
	console.log('new connection: ' + socket.id);
	//console.log(dateQuery);
	socket.on('dateQuery', sendQuery);

	function sendQuery(dateQuery){
		console.log(dateQuery);
		socket.emit('data');
		var spawn = require('child_process').spawn;
    		var pythonProcess = spawn('python3', ["/home/CoryBoris/Python_SQL_Projects/test.py", dateQuery]);

		pythonProcess.stdout.on('data', function (data){
			
		console.log(data.toString());
		data = data.toString();	
		socket.emit('data');
		});
		
	}
}