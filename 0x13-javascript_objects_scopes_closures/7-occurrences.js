#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let A = 0;

  for (let i = 0; i <= list.length; i++) {
    if (list[i] === searchElement) {
      A++;
    }
  }
  return A;
};
