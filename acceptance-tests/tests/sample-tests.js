/**
 * Example tests.
 */
function Hi() {
    this.setEcho = function (str) {
        this.echo = str;
    }

    this.sayHi = function () {
        return "Hi! " + this.echo;
    }
}

var eg = {
    Division: function () {
        var num;
        var denom;

        this.setNumerator = function (n) {
            num = n;
        }
        this.setDenominator = function (n) {
            denom = n;
        }
        this.quotient = function () {
            return num / denom;
        }
    }
};

var exec = require('child_process').exec;
function child_process() {
    this.exec = function (cmd) {
        return {
            then: function (fulfill, reject) {
                exec(cmd, function (err, stdout, stderr) {
                    if (err)
                        return reject(err);

                    fulfill(stdout.trim());
                });
            }
        }
    }
}

module.exports.child_process = child_process;
module.exports.eg = eg;
module.exports.Hi = Hi;
