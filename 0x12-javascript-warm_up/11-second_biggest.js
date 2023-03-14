#!/usr/bin/node
let number = process.argv[2];

number = parseInt(number);

if (isNaN(process.argv[2]) || number === 1) {
  number = 0;
}

let ans = number;

for (let i = 3; i < process.argv.length; i++) {
  const compare = parseInt(process.argv[i]);

  if (number < compare) {
    ans = number;
    number = compare;
  }
}
console.log(ans);
