#!/usr/bin/node
const dataObject = require('./101-data').dict;
const newDict = {};

for (const key in dataObject) {
  if (typeof newDict[dataObject[key]] === 'undefined') {
    newDict[dataObject[key]] = [];
  }
  newDict[dataObject[key]].push(key);
}

console.log(newDict);
