#!/usr/bin/node
const val = process.argv[2];
if (isNaN(val)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < val; i++) {
    console.log('X'.repeat(val));
  }
}
