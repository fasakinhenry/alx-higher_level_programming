#!/usr/bin/node
exports.converter = function (base) {
  return input => input.toString(base);
};
