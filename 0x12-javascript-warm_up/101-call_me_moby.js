#!/usr/bin/node
// Executes x times a function
exports.callMeMoby = function (x, theFunction) {
  while (x-- > 0) {
    theFunction();
  }
};
