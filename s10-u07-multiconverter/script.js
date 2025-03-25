////
// Multiconverter
////

// Rules
//  Find at least 3 conversion formulas you want to use with your multiconverter.
//  Write a function for each formula.
//  Use the window.prompt() function to get inputs from the user as demonstrated in the Tips and Tricks subject.
//  Display the conversion results in the browser console.
//  The program should not quit as long as the user wants to continue converting values.
//  If the user chooses a conversion that is not supported, display that in the console.

// Formula 1 - Celsius to Farenheit
function cel2Far(celsius) {
    return (celsius * 9/5) + 32;
}

// Formula 2 - Liter to Gallone
function lit2Gal(liter) {
    result = liter / 3.785;
    return Math.round(result * 100) / 100;
}

// Formula 3 - Kilo to Pounds
function kil2Pou(kilo) {
    result = kilo * 2.2046226218487759;
    return Math.round(result * 100) / 100;
}

// Declare variables
var convertTrue = true;
var result = 0;
var userInput = "";

// Program is running, while user wants to convert
while (convertTrue) {

    // Check the first user input
    userInput = window.prompt("Do you want to convert a value? ( yes / no )");
    
    if (userInput == "yes" || userInput == "Yes") {

        // Ask user: which type of conversion? 
        userInput = window.prompt("Which conversion? ( celsius / liter / kilo )");

        // Check for different types of conversion
        if (userInput == "celsius" || userInput == "Celsius") {

            // Ask user for value - Formula 1 - Celsius to Farenheit
            userInput = window.prompt("Which value do you want to convert?");
            console.log(userInput + " Celsius is " + cel2Far(userInput) + " Farenheit");

        } else if (userInput == "liter" || userInput == "Liter") {

            // Ask user for value - Formula 2 - Liter to Gallone
            userInput = window.prompt("Which value do you want to convert?");
            console.log(userInput + " Liter(s) is/are " + lit2Gal(userInput) + " Gallon(s)");

        } else if (userInput == "kilo" || userInput == "Kilo") {

            // Ask user for value - Formula 3 - Kilo to Pounds
            userInput = window.prompt("Which value do you want to convert?");
            console.log(userInput + " Kilo(s) is/are " + kil2Pou(userInput) + " Pounds");

        } else {

            // User enters invalid type of conversion
            console.log("This input is not valid for conversion.");
            convertTrue = false;
        }

    } else if (userInput == "no" || userInput == "No") {
        convertTrue = false;
    } else {
        console.log("This input is not valid.");
        convertTrue = false;
    }
}

console.log("Thank you - Have a nice day");
