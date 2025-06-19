# Variables in JavaScript
- A variable is like a container that holds data that can be reused or updated later in the program. 
- In JavaScript, variables are declared using the keywords 
    - var
    - let
    - const.

> var keyword
- The var keyword is used to declare a variable. 
- It has a function-scoped or globally-scoped behaviour.

        var fname = "Dhanraj";
        console.log(fname);
        var fname = "Raj";      // reassigning is allowed
        console.log(fname);     // OUTPUT : Raj

> let keyword 
- The let keyword is introduced in ES6 
- It has block scope and cannot be re-declared in the same scope.

        let  n= 10;
        n = 20;                 // Value can be updated
        // let n = 15;          //cannot redeclared
        console.log(n)          // OUTPUT : 20

> const keyword
- The const keyword declares variables that cannot be reassigned. 
- It's block-scoped as well.

        const n = 100;
        // n = 200; This will throw an error
        console.log(n)         // OUTPUT : 100
