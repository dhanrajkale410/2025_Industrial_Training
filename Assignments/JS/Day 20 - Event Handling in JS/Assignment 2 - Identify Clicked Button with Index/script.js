const allButtons = document.querySelectorAll(".container button");

for (let i = 0; i < allButtons.length; i++) {
    allButtons[i].addEventListener("click", ()=> {
        const buttonText = allButtons[i].textContent;
        const index = i + 1; 
        console.log(`You clicked button ${index}: ${buttonText}`);
    });
}