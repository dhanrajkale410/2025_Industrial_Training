# setInterval() Method in JS

- The setInterval() method calls a function at specified intervals (in milliseconds).

- It continues calling the function until clearInterval() is called, or the window is closed.

- 1 second = 1000 milliseconds.

## Syntax 

    setInterval(function, delay, param1, param2, ...)

- function: The function to be executed.

- delay: The time interval between each call (in milliseconds).

- param1, param2, ...: Optional parameters passed to the function.

## Basic Example

    setInterval(() => {
        console.log("This message appears every 2 seconds");
    }, 2000);

## Using Named Function

    function greet() {
        console.log("Hello!");
    }

    setInterval(greet, 1000); // Calls greet every 1 second

## Stopping the Interval

- To stop a setInterval() loop, use clearInterval() with the interval ID returned by setInterval().

        let count = 0;
        const intervalId = setInterval(() => {
            count++;
            console.log("Count:", count);
            if (count === 5) {
                clearInterval(intervalId);
                console.log("Interval stopped");
            }
        }, 1000);

# Use Cases
- Live clocks or countdown timers

- Periodic data polling (e.g., fetching API data)

- Repeated animations or UI updates