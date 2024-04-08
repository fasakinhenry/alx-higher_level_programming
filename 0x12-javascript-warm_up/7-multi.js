#!/usr/bin/node
// Print x times "C is fun"

if (isNaN(process.argv)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index <= process.argv[2]; index++) {
    console.log('C is fun')
  }
}
