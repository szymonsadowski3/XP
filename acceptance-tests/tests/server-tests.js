var makeRequest = require("../helpers/makeRequest").makeRequest;
var connect = require("../helpers/wifi").connect;

var xp = {
    Server: function () {
        var command;

        this.setCommand = function (c) {
            command = c;
        }

        this.response = function () {
            // return `[echo] ${command}`;
            return {
                then: (resolve, reject) => {
                    makeRequest(command).then(resolve);
                }
            }
        }
    }
};

function wifi() {
    var ssid;
    var pwd;
    this.setSsid = function (ssid) { this.ssid = ssid; console.log(`ssid set to: ${ssid}`) }
    this.setPwd = function (pwd) { this.pwd = pwd; console.log(`pwd set to: ${pwd}`) }

    this.connect = function () {
        return {
            then: (resolve, reject) => {
                connect(this.ssid, this.pwd).then(resolve);
            }
        }
    }
}

module.exports.xp = xp;
module.exports.wifi = wifi;
