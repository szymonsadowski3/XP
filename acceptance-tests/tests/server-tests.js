var makeRequest = require("../helpers/makeRequest").makeRequest;

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

module.exports.xp = xp;
