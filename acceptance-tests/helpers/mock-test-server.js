var createServer = require('net').createServer;

const USERS = [12, 40, 50, 70, 2, 3, 4]
const ADMINS = [1, 2]

var LOGGED_USER = false;

var server = createServer(function (socket) {
    socket.on("data", data => {
        console.log(`incoming data: ${data}`);
 
        // OLD APPROACH. TO BE REIMPLEMENTED IN BOARD.
        // if (!LOGGED_USER) {
        //     const login = data.toString().replace(/"/g, "");
        //     if (login === userId || login === adminId) {
        //         LOGGED_USER = userId;
        //         socket.write("SUCCESS");
        //     } else {
        //         socket.write("FAILED");
        //     }
        // } else {
        let msg = data.toString().split(";");
        let command = msg[0];
        switch (command) {
            case "LOGIN":
                if (LOGGED_USER) {
                    socket.write("ALREADY LOGGED IN");
                } else {
                    const login = msg[1];
                    if ([...USERS, ...ADMINS].includes(Number(login))) {
                        LOGGED_USER = login;
                        socket.write("SUCCESS");
                    } else {
                        socket.write("FAILED");
                    }
                }
                break;
            case "LOGOUT":
                if (!LOGGED_USER) {
                    socket.write("ALREADY LOGGED OUT");
                } else {
                    LOGGED_USER = null;
                    socket.write("SUCCESS");
                }
                break;
            case "OPEN":
                if (LOGGED_USER) {
                    socket.write("DOOR OPENED");
                } else {
                    socket.write("ACCESS DENIED");
                }
                break;
            default:
                socket.write("COMMAND NOT FOUND : " + command);
                break;
            // }
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
