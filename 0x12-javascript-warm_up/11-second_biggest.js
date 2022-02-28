#!/usr/bin/node
let n = 0;
const arr = process.argv.slice(2);
if (arr.length > 1) {
  arr.sort();
  n = arr[arr.length - 2];
}
console.log(n);
