// Task 1 : Create a countdown timer that starts from 10 and decrements every second until it reaches 0.

let timerSecond = document.querySelector("h3");

let count = 10;
const countdown = setInterval(() => {
    timerSecond.textContent = count;
    count--;

    if (count < 0) {
        clearInterval(countdown);
    }
}, 1000); 

