/* 
Datatypes in JavaScript
JavaScript supports various datatypes, which can be broadly categorized into primitive and non-primitive types.

1. Primitive DataTypes
    - Number
    - String
    - Boolean 
    - BigInt 
    - Null
    - Undefined
    - Symbol

2. Non-Primitive DataTypes / Reference DataTypes
    - Object
    - Function
    - Array
    - Date Object
    - Regular Expression
*/

// Primitive DataTypes

// - Number
    let n = 18;
    console.log(n);
    console.log(typeof n);

// - String 
    let fname = "Dhanraj";
    console.log(fname);
    console.log(typeof fname);

// - Boolean 
    let bool = true;
    console.log(bool);
    console.log(typeof bool);

// - BigInt
    let phoneNumber = 12345678901234567890n;
    console.log(phoneNumber);
    console.log(typeof phoneNumber);

// - Undefined
    let unAssigned;
    console.log(unAssigned);
    console.log(typeof unAssigned);

// - Null 
    let empty = null;
    console.log(empty);
    console.log(typeof empty);

// - Symbol
    let sym = Symbol('unique');
    console.log(sym);
    console.log(typeof sym);