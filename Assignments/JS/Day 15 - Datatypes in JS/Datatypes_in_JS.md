# Datatypes in JavaScript
JavaScript supports various datatypes, which can be broadly categorized into **primitive and non-primitive types**.

## Primitive Datatypes
- Primitive datatypes represent **single values** and are **immutable**.
    
> Number 
- Represents numeric values (integers and decimals).

        let n = 42;
        let pi = 3.14;
    
> String 
- Represents text enclosed in single or double quotes.
    
        let s = "Hello, World!";

> Boolean 
- Represents a logical value (true or false).

        let bool= true;

> Undefined
- A variable that has been declared but not assigned a value.

        let notAssigned;
        console.log(notAssigned);           // undefined
    
> Null 
- Represents an intentional absence of any value.

        let empty = null;

> Symbol
- Represents unique and immutable values, often used as object keys.

        let sym = Symbol('unique');

> BigInt 
- Represents integers larger than Number.MAX_SAFE_INTEGER.

        let bigNumber = 123456789012345678901234567890n;

## Non-Primitive Datatypes
- Non-primitive types are objects and can store collections of data or more complex entities.

> Object        
- Represents key-value pairs.

        let obj = {
            name: "Dhanraj",
            age: 18
        };

> Array 
- Represents an ordered list of values.

        let a = ["red", "green", "blue"];

> Function 
- Represents reusable blocks of code.

        function hello() {
            console.log("Hello JavaScript");
        }

> Date Object
- The Date object in JavaScript is used to work with dates and times, allowing for date creation, manipulation, and formatting.

        // Creating a new Date object for the current date and time
        let currentDate = new Date();
        // Displaying the current date and time
        console.log(currentDate);