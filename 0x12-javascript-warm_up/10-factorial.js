#!/usr/bin/node
function factorial(n) {
  if (n === 0) {
    return (1);
  }
  return (n * factorial(n - 1));
}
let x = Number(process.argv[2]);
if (!x) {
  console.log(1);
} else {
  console.log(factorial(x));
}
