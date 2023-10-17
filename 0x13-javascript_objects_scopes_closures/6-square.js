#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let t = 0; t < this.height; t++) console.log(c.repeat(this.width));
    }
  }
};
