#!/usr/bin/node
const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let k = 0; k < this.width; k++) {
        row += c;
      }
      console.log(row);
    }
  }
}
module.exports = Square;
