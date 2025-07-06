function greet(name) {
    console.log("Hello, " + name);
}

function processUserInput(callback) {
    const name = "Dhanraj";
    callback(name);
}

processUserInput(greet);

// Waiting for Interval
function HelloInterval() {
        console.log("Hello!");
}
setInterval(HelloInterval, 1000); // Calls HelloInterval() every 1 second

// Waiting for TimeOut
function HelloTimeOut() {
    console.log("Hello, world!");
}

setTimeout(HelloTimeOut, 1000); // Executes HelloTimeOut after delay 1 second only One While Loading of WebPage