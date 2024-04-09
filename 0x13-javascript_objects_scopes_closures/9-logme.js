#!/usr/bin/node
exports.logMe = function (item) {
  if (!this.counter) {
    this.counter = 0;
  }
  console.log(`${this.counter}: ${item}`);
  this.counter++;
};
