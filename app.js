var socket = require('socket.io-client')('http://10.10.1.143:3000');
socket.on('connect', function(){

});


socket.on('typing', function (data) {
    var message = "Welcome to Socket.IO Chat – ";
    console.log(message, data);
    const spawn = require("child_process").spawn;
    const pythonProcess = spawn('python',["PRINT.py Print.py --firstName=Jefferson --lastName=Aguilar --company=alun ideas --assistentType=vip --assistentId=asdasdasdasdasdasdas"]);
});

socket.on('disconnect', function(){}); 