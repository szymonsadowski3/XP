var createServer = require('net').createServer;

var server = createServer(function (socket) {
    socket.on("data", data => {
        console.log(`incoming data: ${data}`);
        let msg = data.toString().split(":");
        if (msg[0] == "sayhi") {
            socket.write(sayHi(msg[1]));
        } else {
            socket.write(`[echo] ${data}`);
        }

    })

    socket.on("error", err => {
        if (err.errno === "ECONNRESET") {
            console.log(`Client disconnected`);
        }
    })
});

const port = 1337;
server.listen(port, '127.0.0.1');
console.log(`listening on port: ${port}`);

function sayHi(arg) {
    return "Hi! " + arg;
}
