// Objects in JS

// 1. Creation of Object

let object1 = {
    "Name": "Dhanraj",
    "Role" : "Full Stack Web Developer",
    "Age" : 18
}

console.log(object1);
console.log(typeof object1);

// 2. Accesing Key Value Pairs of Objects   

// let age = object1.Age;
let age = object1["Age"];
console.log("Age : "+age)

// 3. Adding Key Value Pair 

object1["gender"] = "Male";
// object1.gender = "Male";
console.log(object1);

// 4. Iterations of Objects

    // Two Ways To Iterate Through Objects ::
    // ###  1. for in loop

    for(let key in object1){
        console.log(key," : " ,object1[key]);
    }

    // ### 2. Objects.keys
    
    // Objects.keys(person);

    console.log(Object.keys(object1));
    // Gives Array of Keys
    console.log(Object.values(object1));
    // Gives Array of Values


// 5. Object Destructing
    
    let{Name,...rest} = object1;
    console.log(Name);
    console.log(rest);


// 6. Objects Inside Array
    const users = [
        {
        userid : 1,
        user_name: "Dhanraj",
        gender : "male"},
        {
        userid : 2,
        user_name: "Kunal",
        gender : "male"},
        {
        userid : 3,
        user_name: "Uday",
        gender : "male"},

    ]

    console.log(users);

    // Iterating it :

    for(let user of users){
        console.log(user);
        console.log(user.user_name);
        console.log(user.userid);
    }


