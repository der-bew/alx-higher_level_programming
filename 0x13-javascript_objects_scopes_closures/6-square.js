#!/usr/bin/node
const SquareP = require('./5-square.js');

module.exports = class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    }
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
