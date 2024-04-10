#!/usr/bin/node
const data = require('./100-data').list;

const arr = data.map(x => x * data.indexOf(x));
console.log(data);
console.log(arr);

