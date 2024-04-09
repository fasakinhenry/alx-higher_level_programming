#!/usr/bin/node
// Searches the second biggest integer in the list of arguments

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(parseInt(list.reverse()[1]));
}
