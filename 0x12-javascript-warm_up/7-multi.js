#!/usr/bin/node
// Print x times "C is fun"

const textOutput = 'C is fun';

if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < parseInt(process.argv[2]); index++) {
    console.log(textOutput);
  }
}
