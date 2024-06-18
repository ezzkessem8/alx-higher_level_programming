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
}

module.exports = Rectangle;

