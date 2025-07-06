
// let myPromise = new Promise(function (myResolve, myReject) {
//     // "Producing Code" (May take some time)

//     myResolve(); // when successful
//     myReject();  // when error
// });

// // "Consuming Code" (Must wait for a fulfilled Promise)
// myPromise.then(
//     function (value) { /* code if successful */ },
//     function (error) { /* code if some error */ }
// );

// Basic Code of Promise Using then & catch Methods 

function loadData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const success = true;

            if (success) {
                resolve("✅ Data loaded successfully!");
            } else {
                reject("❌ Failed to load data.");
            }
        }, 2000);
    });
}

console.log("⏳ Loading data...");

loadData()
    .then((message) => {
        console.log(message); // when resolved
    })
    .catch((error) => {
        console.error(error); // when rejected
    });


// Code of Promise using async & await 

/*
function loadData2() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Data Loaded Successfully!");
    }, 2000);
  });
}

async function displayData() {
  console.log("Loading data...");
  const result = await loadData2();
  console.log(result);
}

displayData();
*/