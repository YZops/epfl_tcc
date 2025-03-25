////
// Game Guess Number
////

// Rules
//  When starting the game, a secret number between 1 and 100 is generated.
//  The game asks the user to enter a number.
//  The game will tell the user if the secret number is bigger or smaller than the guess.
//  As long as the user doesn't find the secret number, the game continues.
//  As soon as the user finds the secret number, the game stops and tells the user how many attempts it took to win.
//      - Make sure to use the right wording (attempt or attempts)
// In case the user enters anything else than a number, the game should tell that to the user and quit gracefully.

// Generate secret number
//var secretNumber = 66; //for testing - fix number
var secretNumber = Math.floor(Math.random() * 100) + 1;

// Initialization user guess
var userGuess = 0;
// Initialization user attempt(s) as counter
var counterUserAttempt = 0;
// Initialization for "attempt" or "attempts"
var wordUserAttempt = " attempts."

// While secret number not user guess
while (secretNumber != userGuess) {

    // User Input
    userGuess = window.prompt("Please enter a natural number between 1 and 100");

    // User attemt(s) counter plus 1
    counterUserAttempt += 1;

    // Number validation
    if (isNaN(userGuess)) {
        console.log("This is not a valid number. The game is ended :(");
        break;
    }

    // Check user guess with secret number
    if (secretNumber == userGuess) {
        
        console.log("Well done! " + userGuess + " is the number we were looking for.");
        
        if (counterUserAttempt == 1) {
            wordUserAttempt = " attempt.";
        }
        
        console.log("You won the game in " + counterUserAttempt + wordUserAttempt);
        
        break;
    
    } else if (secretNumber < userGuess) {
        console.log("Secret number is smaller");
    } else {
        console.log("Secret number is bigger");
    }

}
