var wifi = require('node-wifi');

// wifi.init({
//     iface: null // network interface, choose a random wifi interface if set to null
// });

// // Scan networks
// wifi.scan(function (err, networks) {
//     if (err) {
//         console.log(err);
//     } else {
//         console.log(networks.map(x => x.ssid));
//     }
// });
// wifi
//     .connect({ ssid: "bran the broken", password: "dancingpanda" })
//     .then(() => "ok").then(console.log);

function connect(ssid, pwd) {
    wifi.init({
        iface: null 
    });
    console.log(`connecting to: ${ssid} with ${pwd}`);
    
    return wifi
        .connect({ ssid: ssid, password: pwd })
        .then(() => "ok");
}


module.exports.connect = connect;
