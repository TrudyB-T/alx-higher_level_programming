#!/usr/bin/node
const size = Number(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let t = 0; t < size; t++) {
    let row = '';
    let u = 0;
    while (u < size) {
      row += 'X';
      u++;
    }
    console.log(row);
  }
}
