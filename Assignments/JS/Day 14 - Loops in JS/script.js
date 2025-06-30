// JS Loops
let i = 0;
// 1. for loop
    console.log("For Loop")
    for (let i = 0; i < 10; i++) {
        console.log(i);
    }


// 2. while loop
    console.log("While Loop")
    while(i!=10) {
        console.log(i);
        i++;
    }

// 3. do-while loop
    let a = 0;
    console.log("Do-While Loop")
    do {
        console.log(a);
        a++;
    }while(a<10)


// 4. for-in loop
    let obj = {
        "Name" : "Dhanraj",
        "Role" : "Web Dev",
    }

    for(const key in obj) {
        const element = obj[key];
        console.log(element);
    }

// 5. for-of loop
    for(const c of "Dhanraj"){
        console.log(c);
    }