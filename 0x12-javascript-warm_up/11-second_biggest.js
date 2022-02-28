#!/usr/bin/node

let n = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  n = args[args.length - 2];
} else {
  console.log(n);
}
