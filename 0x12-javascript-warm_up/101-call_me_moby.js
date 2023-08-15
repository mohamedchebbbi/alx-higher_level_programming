#!/usr/bin/node
exports.callMeMoby = function (n, theFunction) {
  for (let i = 0; i < n; i++) {
    theFunction();
  }
};
