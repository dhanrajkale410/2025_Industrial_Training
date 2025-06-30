// JS Filter Function
let arr = [1,2,3,4,5];

console.log(arr.filter((e) => {
    if (e%2==0) {
        return true
    } else {
        return false
    }
}))