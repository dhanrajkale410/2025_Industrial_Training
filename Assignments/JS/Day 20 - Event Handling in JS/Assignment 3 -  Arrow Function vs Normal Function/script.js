const allButtons = document.querySelectorAll(".container button");

// Using Arrow Function
allButtons.forEach((button, index) => {
  button.addEventListener("click", (e) => {
    console.log(e.target);
    console.log(`You clicked button ${index + 1}: ${e.target.innerText}`);
  });
});
