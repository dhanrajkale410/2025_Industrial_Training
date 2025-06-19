"use strict";

// 3. const keyword
/* 
    - The const keyword was introduced in ES6 (2015)

    - Variables defined with const cannot be Redeclared

    - Variables defined with const cannot be Reassigned

    - Variables defined with const have Block Scope     
*/


// Declaration & Initialization of Identifier using const keyword
// Identifier using const keyword must be assigned to a fixed value when they are declared
const PI = 3.14159;
console.log(PI);

// These below 2 lines can throw an Error as Identifier Value declared using const keyword cannot be changed 
// PI = 3.14;      
// PI = PI + 10;  
// console.log(PI);

