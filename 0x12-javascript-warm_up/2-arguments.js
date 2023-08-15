#!/usr/bin/node
let a = 0;
process.argv.forEach((_v, _i) => {
a++;
});
if (a <= 2) {
console.log('No argument');
} else if (a === 3) {
console.log('Argument found');
} else {
console.log('Arguments found');
}
