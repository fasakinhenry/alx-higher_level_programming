#!/usr/bin/node
// Function that increments and call a function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(number + 1);
};
