##
# Game Guess Number
##

# Rules
#   When starting the game, a secret number between 1 and 100 is generated.
#   The game asks the user to enter a number.
#   The game will tell the user if the secret number is bigger or smaller than the guess.
#   As long as the user doesn't find the secret number, the game continues.
#   As soon as the user finds the secret number, the game stops and tells the user how many attempts it took to win.
#       - Make sure to use the right wording (attempt or attempts)
#   In case the user enters anything else than a number, the game should tell that to the user and quit gracefully.

# Imports
import random

# Generate secret number
#secret_number = 66 #for testing - fix number
secret_number = random.randint(1, 100)

# Initialization user guess
user_guess = 0
# Initialization user attempt(s) as counter
counter_user_attempt = 0
# Initialization for "attempt" or "attempts"
word_user_attempt = " attempts."

# While secret number not user guess
while secret_number != user_guess:
    # User Input
    user_guess = input("Please enter a natural number between 1 and 100: ")

    # User attemt(s) counter plus 1
    counter_user_attempt += 1

    # Number validation
    try:
        user_guess = int(user_guess)
    except:
        print("This is not a valid number. The game is ended :(")
        quit()

    # Check user guess with secret number
    if secret_number == user_guess:
        print("Well done! " + str(user_guess) + " is the number we were looking for.")
        if counter_user_attempt == 1:
            word_user_attempt = " attempt."
        print("You won the game in " + str(counter_user_attempt) + word_user_attempt)
        quit()
    elif secret_number < user_guess:
        print("Secret number is smaller")
    else:
        print("Secret number is bigger") 

print("You cheated :)")
