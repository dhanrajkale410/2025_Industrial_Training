# JavaScript 
- JavaScript is core language for web development, enabling dynamic and interactive features in websites with fewer lines of code.
- It is highly in demand, offering many job opportunities in Frontend, Backend (Node.js), and Full Stack Development.
- JavaScript supports powerful frameworks and libraries like React, Angular, Vue.js, Node.js, and Express.js, widely used in modern web applications.
- JavaScript is an object-oriented and event-driven language, ideal for building scalable and responsive applications.
- It is cross-platform and runs directly in all modern web browsers without the need for installation.
Major companies like Google, Facebook, and Amazon use JavaScript in their tech stacks.

# History of JavaScript
> 1995 NetScape Navigator 
- Netscape Navigator was a web browser created in 1994 by Netscape Communications Corporation. 
- It is the first commercially successful web browser with a graphical user interface that renders images in line with the text. 
- The browser was free and usable for non-commercial purposes.

> Mocha Invention
- The Language Called Mocha Was then Build to make the Website Interactive.
- This Language was Named as Mocha.
- The name Mocha was chosen by Marc Andreessen, a Netscape founder.
- Mocha was later renamed to Livescript, and finally it became known as Javascript.
- Named after popular Language at that time Java.

> JavaScript 
- JavaScript launched in May 1995 by Brendan Eich, who used to work at Netscape.
- Created within 10 Days as said so By Brendan Eich.
- Interactive Website made with help Of NetScape Navigator.

> Brenden Eich
- Brendan Eich is an American computer programmer and technology executive. 
- He created the JavaScript programming language and co-founded the Mozilla project, the Mozilla Foundation, and the Mozilla Corporation.

> Invention of JScript 
- At Same Time Frame Looking at the Hype of JavaScript
- Internet Explorer  Created JScript in 1996.
- They Named it JScript looking at Java name hype.

> ECMA Standardization 
- ECMA stands for European Computer Manufacturers Association.
- Decides Standards such as : 
    - ES1 : 1997 - First Specification
    -  ES5 -(Lot of New Features.) - 2009.
    -  ES6 -(Biggest Update in History of JS.) - 2015.
    - Members of Technical Community 39. (tc39) decides New Features and Updates in ES.
- Checks:
     - Allow input into specification
     - Identify Potential Challenges /Shape of Solution
     - Precisely Describe the Syntax and Semantics using formal spec language.
     - Indicate that further refinement will require feedback from implementations and users.
     - Indicate that the addition is ready for inclusion in the Formal EcmaScript Standard.
- More Versions of JS
    - ES6 : ES2015
    - ES7 : ES2016
    - ES8 : ES2017

# Introduction to JavaScript
> JavaScript 
- JavaScript is core language for web development, enabling dynamic and interactive features in websites with fewer lines of code.
- It is highly in demand, offering many job opportunities in Frontend, Backend (Node.js), and Full Stack Development.
- It supports powerful frameworks and libraries like React, Angular, Vue.js, Node.js, and Express.js, widely used in modern web applications.
- It is an object-oriented and event-driven language, ideal for building scalable and responsive applications.
- It is cross-platform and runs directly in all modern web browsers without the need for installation.
Major companies like Google, Facebook, and Amazon use JavaScript in their tech stacks.
- It is case-sensitive and uses the Unicode character set.
- It is a lightweight interpreted (or just-in-time compiled) programming language with first-class functions. 

> Additional Information about JavaScript
- JavaScript contains a standard library of objects, such as Array, Map, and Math, and a core set of language elements such as operators, control structures, and statements. 
- Core JavaScript can be extended for a variety of purposes by supplementing it with additional objects; for example:

    - Client-side JavaScript extends the core language by supplying objects to control a browser and its Document Object Model (DOM). For example, client-side extensions allow an application to place elements on an HTML form and respond to user events such as mouse clicks, form input, and page navigation.
    - Server-side JavaScript extends the core language by supplying objects relevant to running JavaScript on a server. For example, server-side extensions allow an application to communicate with a database, provide continuity of information from one invocation to another of the application, or perform file manipulations on a server.

- This means that in the browser, JavaScript can change the way the webpage (DOM) looks. And, likewise, Node.js JavaScript on the server can respond to custom requests sent by code executed in the browser.

> Features of JavaScript
- Client-Side Scripting
    - JavaScript runs on the user's browser, so has a faster response time without needing to communicate with the server.
- Versatile 
    - JavaScript can be used for a wide range of tasks, from simple calculations to complex server-side applications.
- Event-Driven 
    - JavaScript can respond to user actions (clicks, keystrokes) in real-time.
- Asynchronous 
    - JavaScript can handle tasks like fetching data from servers without freezing the user interface.
- Rich Ecosystem 
    - There are numerous libraries and frameworks built on JavaScript, such as React, Angular, and Vue.js, which make development faster and more efficient.

> Application of JavaScript 

- Web Development
- Web Applications
- Server Applications
- Game Development
- Smartwatches

# Comments in JavaScript
- The syntax of comments is the same as in C++ and in many other languages:
- Types of Comments 

    - Single Line Comment

            // a one line comment

    - Multi-Line Comment

            /* this is a longer,
               multi-line comment
            */

# Hello World Program in JS
- We can also print the "Hello World" program directly into the console terminal without embedded it into HTML. Create an index.js file and add the code to it.

        console.log("Hello World");

- In this Example :
    console.log() 
        - The console.log() method is used to print messages to the browser's developer console.

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

         
