#!/usr/bin/node
const add = function (a, b) {
  return a + b;
};

console.log(add(Number(process.argv[2]), Number(process.argv[3])));
