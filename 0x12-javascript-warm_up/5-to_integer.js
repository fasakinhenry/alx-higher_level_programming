#!/usr/bin/node
// prints My number: <first argument converted in integer>
// Only prints if the first argument can be converted to an integer:

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
