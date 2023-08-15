#!/usr/bin/node
let a = 0;
process.argv.forEach((v, i) => {
  a++;
  if (i === 2) {
    console.log(`${v}`);
  }
});
if (a <= 2) {
  console.log('No argument');
}
