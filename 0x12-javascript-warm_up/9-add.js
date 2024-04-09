#!/usr/bin/node
// Prints the addition of 2 integers

function add (a, b) {
  console.log(a + b);
}

let a = parseInt(process.argv[2]);
let b = parseInt(process.argv[3]);

add(a, b);
