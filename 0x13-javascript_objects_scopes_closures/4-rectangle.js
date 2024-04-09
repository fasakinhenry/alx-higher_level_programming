#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (parseInt(w) > 0 && parseInt(h) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }

  rotate () {
    const tempHeight = this.height;
    this.height = this.width;
    this.width = tempHeight;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
