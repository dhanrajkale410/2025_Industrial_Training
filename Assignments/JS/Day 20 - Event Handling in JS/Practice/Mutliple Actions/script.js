const btn1 = document.getElementById("one");
const btn2 = document.getElementById("two");
const btn3 = document.getElementById("three");

const body = document.querySelector("body");

btn1.addEventListener("click",(e) => {
    e.target.style.backgroundColor = "lightgreen";
    body.style.backgroundColor = "skyblue";
});

btn2.addEventListener("click",(e) => {
    e.target.style.backgroundColor = "#E67514";
    body.style.backgroundColor = "#212121";
});

btn3.addEventListener("click",(e) => {
    e.target.style.backgroundColor = "#123458";
    body.style.backgroundColor = "#F1EFEC";
});