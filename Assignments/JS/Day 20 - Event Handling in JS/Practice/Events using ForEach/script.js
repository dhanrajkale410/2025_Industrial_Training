const container = document.querySelectorAll(".container button");
console.log(container);

const body = document.querySelector("body");

container.forEach((button) => {
    button.addEventListener("click", (e) => {
        e.target.style.backgroundColor = "skyblue";
        e.target.style.color = "brown";
        body.style.backgroundColor = "orange";
    });
});