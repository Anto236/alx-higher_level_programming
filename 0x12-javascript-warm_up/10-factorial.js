#!/usr/bin/node
// script that computes and prints a factorial

function factorial (a) {
  if ((isNaN(a)) || (a === 1) || (a === 0)) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(parseInt(process.argv[2])));
