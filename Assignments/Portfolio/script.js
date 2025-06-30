document.addEventListener("DOMContentLoaded", () => {
    const toggle = document.getElementById("menu-toggle");
    const navTabs = document.getElementById("nav-tabs");

    toggle.addEventListener("click", () => {
        navTabs.classList.toggle("active");
    });
});
