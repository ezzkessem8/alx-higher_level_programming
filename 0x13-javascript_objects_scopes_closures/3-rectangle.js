#!/usr/bin/node

class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
      // Create an empty object if w or h is equal to 0 or not a positive integer
      return {};
    } else {
      // Otherwise, initialize the instance attributes width and height
      this.width = w;
      this.height = h;
    }
  }

  print() {
    // Print the rectangle using the character X
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;

