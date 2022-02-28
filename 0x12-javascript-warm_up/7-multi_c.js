#!/usr/bin/node
const x = 'C is fun';
const val = process.argv[2];
if (isNaN(val)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < val; i++) {
    console.log(x);
  }
}
