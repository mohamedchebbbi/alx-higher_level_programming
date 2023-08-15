#!/usr/bin/node
function factorialize (n) {
  let MyRes = 1;
  for (let i = 1; i <= n; i++) {
    MyRes *= i;
  }
  return (MyRes);
}
console.log(factorialize(parseInt(process.argv[2])));
