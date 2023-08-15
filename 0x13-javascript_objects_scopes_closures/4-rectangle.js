#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
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

  rotate () {
    const x = this.height;
    this.height = this.width;
    this.width = x;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
