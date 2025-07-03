// Task 2 : Display a greeting message after a 3-second delay.
userName = prompt("Enter Your Name : ");

const greetMsg = document.querySelector("h3");

setTimeout(() => {
    greetMsg.textContent = "Hello " + userName + " 👋";
}, 3000);