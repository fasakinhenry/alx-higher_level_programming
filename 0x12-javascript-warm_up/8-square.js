#!/usr/bin/node
// Prints a square

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let index = 0; index < parseInt(process.argv[2]); index++) {
    let row = '';

    for (let index2 = 0; index2 < parseInt(process.argv[2]); index2++) {
      row += 'X';
    }
    console.log(row);
  }
}
