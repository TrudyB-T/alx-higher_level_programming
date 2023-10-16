#!/usr/bin/node
const x = Number(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let count = 0;
  while (count < x) {
    console.log('C is fun');
    count++;
  }
}
