// Tasks:
// Create 3 buttons: “Way 1”, “Way 2”, “Way 3”
// Use:
// Inline HTML onclick=""
// JS: element.onclick
// JS: element.addEventListener("click", ...)
// On click: log message + change background to green (then revert)


// Way 1 : Using Inline HTML onclick attribute

function way1Click(btn) {
    console.log("Way 1 Clicked");
    btn.style.backgroundColor = "skyblue";
}

// Way 2 : using element.onclick

const way2Btn = document.getElementById("way2")
way2Btn.onclick = function() {
    console.log("Way 2 Clicked");
    this.style.backgroundColor = "lightgreen";
}

// Way 3 : Using element.addEventListener method

const way3Btn = document.getElementById("way3");
way3Btn.addEventListener("click", function() {
    console.log("Way 3 Clicked");
    this.style.backgroundColor = "yellow";
});