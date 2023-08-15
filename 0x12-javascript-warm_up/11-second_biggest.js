#!/usr/bin/node
function nextBiggest (arr) {
  let max = 0; let result = 0;

  for (const value of arr) {
    const n = Number(value);

    if (n > max) {
      [result, max] = [max, n];
    } else if (n < max && n > result) {
      result = n;
    }
  }

  return result;
}

console.log(nextBiggest(process.argv));
