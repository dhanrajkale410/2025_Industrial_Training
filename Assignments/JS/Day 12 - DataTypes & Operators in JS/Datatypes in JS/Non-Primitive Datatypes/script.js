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
*/

// Non-Primitive Datatypes

// - Object
    let obj = {
            name: "Dhanraj",
            age: 18
        };
    
        console.log(obj);
        console.log(typeof obj);

// - Function 
    function hello(Fname) {
            return "Hello," + Fname;
        }
    console.log(hello("Dhanraj"));

// - Array 
    let a1 = [1, 2, 3, 4, 5];
    console.log(a1);
    console.log(typeof a1);

// - Date Object 
    let currentDate = new Date();
    // Displaying the current date and time
    console.log(currentDate);
    console.log(typeof currentDate);