import * as readlineSync from "readline-sync";

function isPrime(num: number): boolean {
  if (num <= 1) return false;
  if (num <= 3) return true;
  if (num % 2 === 0 || num % 3 === 0) return false;

  for (let i = 5; i * i <= num; i += 6) {
    if (num % i === 0 || num % (i + 2) === 0) return false;
  }
  return true;
}

function getUserInput(): number {
  const input = readlineSync.question("Send a number: ");
  const number = parseInt(input);
  return number;
}

function main() {
  let continueChecking = true;

  while (continueChecking) {
    const number = getUserInput();
    if (isPrime(number)) {
      console.log(`${number} is prime.`);
    } else {
      console.log(`${number} not prime.`);
    }

    const response = readlineSync.question("Wanna send more? (yes/no): ");
    if (response.toLowerCase() !== "yes") {
      continueChecking = false;
    }
  }

  console.log("Bye !");
}

main();
