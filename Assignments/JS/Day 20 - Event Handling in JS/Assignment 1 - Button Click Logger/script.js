const allButtons = document.querySelectorAll("button");

for(let i = 0 ; i < allButtons.length ; i++) {
    allButtons[i].addEventListener("click",function() {
        console.log(this);
        console.log(this.textContent);
    });
}