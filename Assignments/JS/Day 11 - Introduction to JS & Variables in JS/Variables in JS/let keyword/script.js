"use strict";

// 2. let keyword

/* The let keyword was introduced in ES6 (2015)

Variables declared with let have Block Scope

Variables declared with let must be Declared before use

Variables declared with let cannot be Redeclared in the same scope */

// Declaration and Value Assigning of Variable / Identifier using let keyword
let firstName = "Dhanraj";
console.log(firstName);

// Reassigning Value / Changing Value of Variable or Identifier
firstName = "Raj";
console.log(firstName);

// Using let keyword we cannot redeclared the same identifier / Variable in Same Block of Scope
// let firstName = "Dhanraja";
// console.log(firstName);