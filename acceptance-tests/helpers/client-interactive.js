const net = require('net');

const HOST = '127.0.0.1'
const PORT = 1337;

const client = new net.Socket();
client.connect(PORT, HOST, function () {
    console.log('Connected. Tell me what to send!');
    process.stdout.write("> ");

    const stdin = process.openStdin();
    stdin.addListener("data", data => {
        let msg = data.toString().trim();

        if (msg === "q") {
            client.end();
            return;
        }

        client.write(msg);
    });
});

client.on('data', function (data) {
    console.log('<< ' + data);
    process.stdout.write("> ");
});

client.on('close', function () {
    console.log('Connection closed');
});
