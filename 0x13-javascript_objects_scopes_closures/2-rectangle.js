#!/usr/bin/node
module.exports = class Rectangle {
  constructor (a, b) {
    if (a > 0 && b > 0) {
      this.width = a;
      this.height = b;
    }
  }
};
