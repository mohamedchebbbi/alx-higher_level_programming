#!/usr/bin/node
module.exports = class Rectangle {
  constructor (a, b) {
    if (a > 0 && b > 0) {
      this.width = a;
      this.height = b;
    }
  }

  print () {
    let B = '';
    for (let i = 0; i < this.width; i++) {
      B += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(B);
    }
  }
};
