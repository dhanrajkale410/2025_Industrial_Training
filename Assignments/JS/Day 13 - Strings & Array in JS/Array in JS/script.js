// Array in JS

// Creating Array using Literals
let arr = ["BMW", "Volvo", "Audi", "Porsche"];
console.log(arr)

// Accessing Array Elements
let arr1 = arr[0];
console.log(arr1);

// Changing Value of an Element
arr[0] = "Jaguar";
console.log(arr);

// Array Methods in JS

// length()
arrLength = arr.length;
console.log(arrLength);

// pop()
arr.pop();
console.log(arr);


// push 
arr.push("Mercedes");
console.log(arr);

// concat()
let backEnd = ["Django", "Flask"];
let frontEnd = ["HTML", "CSS", "JS"];
let fullStack = frontEnd.concat(backEnd);
console.log(fullStack); 

// sort()
let arrSorted = frontEnd.sort();
console.log(frontEnd);

// shift()
arr.shift();
console.log(arr);

// unshift(element)
arr.unshift("Pajero");
console.log(arr);

// slice()
console.log(arr.slice(2,4));

// reverse()
console.log(arr.reverse());