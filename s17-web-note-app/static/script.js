// Selecting variables from html file
const welcomeMessageDiv = document.getElementById("welcomeMessageDiv");
const setUsernameDiv = document.getElementById("setUsernameDiv");
const setUsernameError = document.getElementById("setUsernameError");
const fieldSetUsername = document.getElementById("fieldSetUsername");
const butSetUsername = document.getElementById("butSetUsername");

// Declare variables
let visitCount;

// Prepare localStorage
if (localStorage.getItem("username") === null && localStorage.getItem("visitCount") === null) {
    // Set empty localStorage
    localStorage.setItem("username", "");
    localStorage.setItem("visitCount", "0")
}

// Create Empty Storage "itemList" if not exist and show welcome message
function setUsername() {
    // Check field username has a value
    if (fieldSetUsername.value == "") {
        setUsernameError.className = "displayBlock error"
    } else {
        // Set localStorage "username"
        localStorage.setItem("username", fieldSetUsername.value);

        // Create User Welcome Screen
        createWelcomeScreen();
    }
}

// Create User Welcome Screen
function createWelcomeScreen() {
        // Create welcome message
        const welcomeMessageInner = document.createElement("h2");
        welcomeMessageInner.className = "welcomeUsername";

        // Create text for welcome message
        if (localStorage.getItem("visitCount") == "0") {
            welcomeMessageInner.innerText = "Welcome " + localStorage.getItem("username");
            // Set localStorage "visitCount" + 1
            visitCount = Number(localStorage.getItem("visitCount")) + 1;
            localStorage.setItem("visitCount", visitCount);
        } else {
            welcomeMessageInner.innerText = "Welcome back " + localStorage.getItem("username");
        }

        // Append paragraph to html content
        welcomeMessageDiv.appendChild(welcomeMessageInner); 

        // Username is set - No need Username fields anymore
        setUsernameDiv.className = "displayNone";
        // Username is set - Show Navigation
        welcomeNavigation.className = "displayBlock";
}

if (localStorage.getItem("visitCount") == "1") {
    createWelcomeScreen();
}

// Button functions from html file
butSetUsername.addEventListener("click", setUsername);
