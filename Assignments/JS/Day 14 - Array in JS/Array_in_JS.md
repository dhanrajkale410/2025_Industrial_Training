# Array in JavaScript
- In JavaScript, an array is an ordered list of values. 
- Each value is called an element, and each element has a numeric position in the array, known as its index. 
- Arrays in JavaScript are zero-indexed, meaning the first element is at index 0, the second at index 1, and so on.
- Array can be Created in Three Ways: 

    1. Create Array using Literal
        - Creating an array using array literal involves using square brackets [] to define and initialize the array.

                let arr = [10, 20, 30];
                console.log(arr);             // [10,20,30]

    2. Create using new Keyword (Constructor) 
        - The "Array Constructor" refers to a method of creating arrays by invoking the Array constructor function.

                let a = new Array(10, 20, 30);
                console.log(a);             // [10,20,30]

    3. Using the JavaScript Keyword new
        - The following example also creates an Array, and assigns values to it:

                const cars = new Array("BMW", "Volvo", "Audi");

> Accessing Array Elements
- You access an array element by referring to the index number:

        let cars = ["BMW", "Volvo", "Audi"];
        let car = cars[0];
        console.log(car);                   // BMW

> Changing an Array Element
- This statement changes the value of the first element in cars:

        let cars = ["BMW", "Volvo", "Audi"];
        cars[0] = "Jaguar";
        console.log(cars);                  // ["Jaguar","Volvo","Audi"]

## Array Destructing
- The destructuring assignment syntax is a JavaScript expression that makes it possible to unpack values from arrays, or properties from objects, into distinct variables.
- In Other words, Array Destructing Is :
We Unpack whole array which is huge with data & data can be values or properties from arrays or objects respectively we assign it to distinct particular variables.

> Basic Destructing Array

        const myarr = ["value1","value2"];
        let var1= myarr[0];
        let var2= myarr[1];
        console.log(var1);              //value1
        console.log(var2);              //value2

>  Other way of Destructing Array in JS.

        const myarr = ["value1","value2"];

        let[var1,var2]=myarr;

        console.log(var1);              // value1
        console.log(var2);              // value2

> In case of let var destructuring

        const myarr = ["value1","value2"];
        let[var1,var2]=myarr;
        var1 ="changing value"; 

        // Array is Destructed and stored in variables
        // and variable act similar to normal var
        
        console.log(var1);              // changing value
        console.log(var2);              // value2

> In case of const var destructuring

        const myarr = ["value1","value2"];

        const[var1,var2]=myarr;
        // var1 ="changing value"; 
        // cannot change const var acts similar to normal var

        // Array is Destructed and stored in variables
        // and variable act similar to normal var
        console.log(var1);              // value1
        console.log(var2);              // value2

> Using Spread operator

        const myarr = ["value1","value2","value3","value4","value5"];
        // with help of spread operator
        const[var1,var2,var3,...newarr]=myarr;

        // Array is Destructed and stored in variables
        // and variable act similar to normal var
        console.log(var1);              // value1
        console.log(var2);              // value2
        console.log(var3);              // value3
        console.log(newarr);            // ["value4","value5"]

## Array Methods in JavaScript 

> length
- Returns the length (size) of an array

        let cars = ["BMW", "Volvo", "Audi"];
        let size = cars.length;
        console.log(size);          // 3

> toString()
- The toString() method returns the elements of an array as a comma separated string.

        let cars = ["BMW", "Volvo", "Audi"];
        let str = cars.toString();
        console.log(str);           // BMW,Volvo,Audi

> pop()
- Removes the last element from an array.

        let cars = ["BMW", "Volvo", "Audi"];
        cars.pop();
        console.log(cars);              // ["BMW", "Volvo"]

> push()
- It adds a new element to an array (at the end):

        let cars = ["BMW", "Volvo", "Audi"];
        cars.push("Porsche");
        console.log(cars);                  // ["Porsche","BMW","Volvo","Audi"]

> concat() 
- It creates a new array by merging (concatenating) existing arrays:

        let backEnd = ["Django", "Flask"];
        let frontEnd = ["HTML", "CSS", "JS"];
        let fullStack = frontEnd.concat(backEnd);
        console.log(fullStack);            // ["HTML","CSS","JS","Django","Flask"]

> sort()
- It sorts an array alphabetically / Numerically:

        let frontEnd = ["HTML", "CSS", "JS"];
        frontEnd.sort();

> shift()
- Removes the first array element
        
        let frontEnd = ["HTML", "CSS", "JS"];
        frontEnd.shift();

> unshift()
- It adds a new element to an array (at the beginning), and "unshifts" older elements.

        let cars = ["BMW", "Volvo", "Audi"];
        cars.unshift("Porsche");

> slice()
- Slices out a part of an array

        let fullStack = ["HTML","CSS","JS","Django","Flask"];
        fullStack.slice(3,4);

> reverse()
- It reverses the elements in an array

        let arr = ["BMW", "Volvo", "Audi", "Porsche"];
        arr.reverse();
        