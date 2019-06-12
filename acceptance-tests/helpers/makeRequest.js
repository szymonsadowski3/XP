var net = require('net');

const HOST = '127.0.0.1'
const PORT = 1337;

async function makeRequest(payload, host, port) {
    var client = new net.Socket();
    return new Promise((resolve, reject) => {

        client.connect(port || PORT, host || HOST, function () {
            console.log('Connected.');

            client.write(JSON.stringify(payload), err => {
                if (err) { console.log(err); }

                client.on('data', function (data) {
                    console.log('<< ' + data);
                    resolve(data.toString());
                })
            });
        });
    });
}

// makeRequest("hello").then(console.log)

module.exports.makeRequest = makeRequest;
