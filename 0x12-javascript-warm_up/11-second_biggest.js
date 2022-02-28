#!/usr/bin/node

const arr = process.argv.slice(2);
if (arr.length > 1) {
  arr.sort();
  const n = arr[arr.length - 2];
  console.log(n);
} else {
  console.log('0');
}
