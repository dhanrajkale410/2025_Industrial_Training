# Strings in JavaScript
- Strings are for storing text
- Strings are written with quotes

        Example 
        
        let str = "Dhanraj Kale";

> String Indexing 
- String Indexing in JavaScript is same as C++/Java.
- In JavaScript It Starts from 0th Index to n-1 index.
- While Accessing a single alphabet from a String we uses its Index Number

        let str = "Dhanraj";
        
        /* Indexing
        D   h   a   n   r   a   j 
        0   1   2   3   4   5   6 */

        console.log("Indexing")
        console.log(str[0]);
        console.log(str[1]);
        console.log(str[2]);
        console.log(str[3]);
        console.log(str[4]);
        console.log(str[5]);
        console.log(str[6]);
        
        OUTPUT : D h a n r a j

> String Length
- Every String has its own Length till which it extends.
- In JavaScript we uses the length keyword to find the length of any String.

        let str = "Dhanraj";
        console.log(str.length);    // OUTPUT : 7

>  String Concatenation 
- Strings Concatenation in JavaScript can be done by using + operator 

        let str1 = "Dhanraj";
        let str2 = "Kale";
        let full_name = str1 + " " + str2;
        console.log(full_name);     // Dhanraj Kale


# String Templates

> Back-Tics Syntax
- Template Strings use back-ticks (``) rather than the quotes ("") to define a string:

        let text = `Hello World!`;

> Quotes Inside Strings
- Template Strings allow both single and double quotes inside a string:

        let text = `He's often called "Johnny"`;

> Multiline Strings
- Template Strings allow multiline strings:

    
        let text = 
                    `The quick
                    brown fox
                    jumps over
                    the lazy dog`;

> Interpolation
- Template String provide an easy way to interpolate variables and expressions into strings.
- The method is called string interpolation.

        ${...}

> Variable Substitutions
- Template Strings allow variables in strings:

        let firstName = "Dhanraj";
        let lastName = "Kale";
        let text = `Welcome ${firstName}, ${lastName}!`;
        console.log(text);          // Welcome Dhanraj, Kale!

# String Methods in JavaScript

> slice()
- slice() extracts a part of a string and returns the extracted part in a new string.
- The method takes 2 parameters: start position, and end position (end not included).

        let str = "Dhanraj";
        let sliceString = str.slice(4);
        console.log(sliceString);     // raj

> trim()
- The trim() method in Java String is a built-in function that eliminates leading and trailing spaces.

        let fName = "Dhanraj            ";
        let trimName = fName.trim();
        console.log(trimName);        // Dhanraj

> toUpperCase()
- A string is converted to upper case with toUpperCase().

        let str = "dhanraj";
        let upperStr = str.toUpperCase();
        console.log(upperStr);        // DHANRAJ

> toLowerCase
- A string is converted to lower case with toLowerCase().

        let str = "DHANRAJ";
        let lowerStr = str.toLowerCase();
        console.log(lowerStr);        // dhanraj

> concat()
- It is used to Concatenate Two Strings instead of using + operator.

        let text1 = "Hello";
        let text2 = "World";
        let text3 = text1.concat(" ", text2);
        console.log(text3);             // Hello World

> charAt(index)
- It returns the character at a specified index (position) in a string:

        let text = "HELLO WORLD";
        let char = text.charAt(0);
        console.log(char);              // H 

> replace(text)
- It replaces a specified value with another value in a string:

        let text = "Hello World";
        let newText = text.replace("World", "User");
        console.log(newText);           // Hello User
