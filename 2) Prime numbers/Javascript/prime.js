"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readlineSync = require("readline-sync");
function isPrime(num) {
    if (num <= 1)
        return false;
    if (num <= 3)
        return true;
    if (num % 2 === 0 || num % 3 === 0)
        return false;
    for (var i = 5; i * i <= num; i += 6) {
        if (num % i === 0 || num % (i + 2) === 0)
            return false;
    }
    return true;
}
function getUserInput() {
    var input = readlineSync.question("Send a number: ");
    var number = parseInt(input);
    return number;
}
function main() {
    var continueChecking = true;
    while (continueChecking) {
        var number = getUserInput();
        if (isPrime(number)) {
            console.log("".concat(number, " is prime."));
        }
        else {
            console.log("".concat(number, " not prime."));
        }
        var response = readlineSync.question("Wanna send more? (yes/no): ");
        if (response.toLowerCase() !== "yes") {
            continueChecking = false;
        }
    }
    console.log("Bye !");
}
main();
