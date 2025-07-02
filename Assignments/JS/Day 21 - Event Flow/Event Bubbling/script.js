/* 
By Default Hierarchy
    1. Child
    2. Parent
    3. GrandParent 
    4. Body
*/


const grandparent = document.querySelector(".grandparent");
const parent = document.querySelector(".parent");
const child = document.querySelector(".child");

child.addEventListener("click",()=>{
    console.log("Bubble Child !!");
})

parent.addEventListener("click",()=>{
    console.log("Bubble parent !!");
})

grandparent.addEventListener("click",()=>{
    console.log("Bubble grandparent !!");
})

document.body.addEventListener("click",()=>{
    console.log("Bubble body !!");
})
