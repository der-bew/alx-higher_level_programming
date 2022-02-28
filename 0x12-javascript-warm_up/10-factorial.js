#!/usr/bin/node
const val = process.argv[2];
let fact = 1;
if (isNaN(val)) {
  console.log(fact);
} else {
  for (let i = parseInt(val); i > 0; i--) {
    fact *= i;
  }
  console.log(fact);
}
