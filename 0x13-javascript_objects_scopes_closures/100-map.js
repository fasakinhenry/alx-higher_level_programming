#!/usr/bin/node

// Importing the list array from 100-data.js
const {list} = require('./100-data');

// Using map to compute a new array where each value is the original value multiplied by its index
const mappedList = list.map((value, index) => value * index);

// Printing the initial list
console.log(list);

// Printing the new list
console.log(mappedList);


