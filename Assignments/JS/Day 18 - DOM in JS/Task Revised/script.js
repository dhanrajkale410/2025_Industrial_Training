// ID Card using JS DOM 

// Create and append style
const style = document.createElement("style");
style.textContent = `
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: skyblue;
            font-family:Arial, Helvetica, sans-serif;
            box-sizing: border-box;
            min-height: 100vh;
        }

        .id-card {
            display: flex;
            flex-direction : column;
            align-items: center;
            justify-content: center;
            background-color: blanchedalmond;
            width: 20rem;
            height: 30rem;
            border-radius : 1rem;
            border : 2px solid blue;
        }

        .company-logo {
            width : 6rem;
            height : 6rem;
            margin-top : 2rem

        }

        .profile-image {
            margin-top : 1rem;
            width : 8rem;
            height : 8rem;
            border-radius : 1rem;
        }

        h2 {
            color : dark blue;
            font-size : 1.3rem;
            font-weight : bolder;
        }

        h3 {
            font-size : 1rem
        }
        `;
document.head.appendChild(style);

const card = document.createElement("div");
card.className = "id-card";

const logo = document.createElement("img");
logo.className = "company-logo";
logo.src = "rich-logo.png";

const profile = document.createElement("img");
profile.className = "profile-image";
profile.src = "profile-image.png";

const Name = document.createElement("h2");
Name.textContent = "Name : Dhanraj Hemant Kale";

const roll = document.createElement("h3");
roll.textContent = "Role : Full Stack Web Developer Intern";

const idNumber = document.createElement("p");
idNumber.textContent = "ID : RICH2025FSD07";

const email = document.createElement("p");
email.textContent = "Email : dhanrajkale999@gmail.com";

card.appendChild(logo);
card.appendChild(profile);
card.appendChild(Name);
card.appendChild(roll);
card.appendChild(idNumber);
card.appendChild(email);

document.body.appendChild(card);
