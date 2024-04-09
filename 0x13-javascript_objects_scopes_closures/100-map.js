#!/usr/bin/node
const listToMap = require("./100-data").list;
let newList =[];
listToMap.map((index, element) => {
  newList.push(element * index);
});

console.log(listToMap);
console.log(newList);

