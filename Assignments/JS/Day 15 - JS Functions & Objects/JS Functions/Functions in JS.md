# JS Functions
- A JavaScript function is a block of code designed to perform a particular task.
- A JavaScript function is executed when "something" invokes it (calls it).

        // Function to compute the product of p1 and p2
        function myFunction(p1, p2) {
        return p1 * p2;
        }

## JavaScript Function Syntax
- A JavaScript function is defined with the function keyword, followed by a name, followed by parentheses ().
- Function names can contain letters, digits, underscores, and dollar signs (same rules as variables).
- The parentheses may include parameter names separated by commas:
(parameter1, parameter2, ...)
- The code to be executed, by the function, is placed inside curly brackets: {}

        function name(parameter1, parameter2, parameter3) {
        // code to be executed
        }

- Function parameters are listed inside the parentheses () in the function definition.
- Function arguments are the values received by the function when it is invoked.
- Inside the function, the arguments (the parameters) behave as local variables.


## Function Invocation
- The code inside the function will execute when "something" invokes (calls) the function:
    - When an event occurs (when a user clicks a button)
    - When it is invoked (called) from JavaScript code
    - Automatically (self invoked)

## Function Return
- When JavaScript reaches a return statement, the function will stop executing.
- If the function was invoked from a statement, JavaScript will "return" to execute the code after the invoking statement.
- Functions often compute a return value. The return value is "returned" back to the "caller":

        // Function is called, the return value will end up in x
        let x = myFunction(4, 3);

        function myFunction(a, b) {
        // Function returns the product of a and b
        return a * b;
        }


# Function Program

        Example 
        
        function facto(n) {
            if(n==0 || n==1) {
                return 1;
            }
            else {
                return (n*(facto(n-1)));
            }
        }

        facto(5);