#!/usr/bin/node
// script that prints x times “C is fun”

let i = 0;
const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
