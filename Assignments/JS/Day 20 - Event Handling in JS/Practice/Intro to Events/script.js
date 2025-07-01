const btn = document.getElementById("click-btn");

const body = document.querySelector("body");

btn.addEventListener("click", (e)=> {
    body.style.backgroundColor = "skyblue";
    e.target.style.backgroundColor = "lightgreen";
});