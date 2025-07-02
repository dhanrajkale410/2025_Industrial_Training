/* 
Event Flow
    1. Event Bubbling / Event Propogation.
    2. Event Capturing.
    3. Event Delegation.
*/

// Event Capturing

/* 
Hierarchy if true and vice versa
    1. Body
    2. Grandparent 
    3. Parent 
    4. Child
*/

const grandparent = document.querySelector(".grandparent");

const parent = document.querySelector(".parent");
const child = document.querySelector(".child");

child.addEventListener("click",()=>{
    console.log("Child Clicked!");
},true);


parent.addEventListener("click",()=>{
    console.log("Parent Clicked!");
},true);


grandparent.addEventListener("click",()=>{
    console.log("Grandparent Clicked!");
},true);


document.body.addEventListener("click",()=>{
    console.log("Body Clicked!");
},true);
