// Assignment 2: Button Click Counter
// Goal: Use multiple addEventListeners on one button.

// Tasks:
// One button: “Count Clicks”
// First listener: increase a visible counter (<span>)
// Second listener: log event.type, event.timeStamp, and this.tagName

// One button: “Count Clicks”
const ClickBtn = document.getElementById("btn");
const counterSpan = document.getElementById("counter");
let count = 0;

// First listener: increase a visible counter (<span>)
ClickBtn.addEventListener("click", function () {
  count++;
  counterSpan.textContent = count;
});

// Second listener: log event.type, event.timeStamp, and this.tagName
ClickBtn.addEventListener("click", function(event){
    console.log("Event Type : "+event.type)
    console.log("Event TimeStamp : "+event.timeStamp)
    console.log("Event Tag Name : "+ this.tagName)
});