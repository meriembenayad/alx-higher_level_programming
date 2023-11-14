#!/usr/bin/node
exports.esrever = function (list) {
  const reversedStr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversedStr.push(list[i]);
  }
  return reversedStr;
};
