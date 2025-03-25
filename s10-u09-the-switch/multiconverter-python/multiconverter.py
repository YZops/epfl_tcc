##
# Multiconverter
##

# Rules
#   Find at least 3 conversion formulas you want to use with your multiconverter.
#   Write a function for each formula.
#   Use the window.prompt() function to get inputs from the user as demonstrated in the Tips and Tricks subject.
#   Display the conversion results in the browser console.
#   The program should not quit as long as the user wants to continue converting values.
#   If the user chooses a conversion that is not supported, display that in the console.

# Formula 1 - Celsius to Farenheit
def cel_to_far(celsius):
    return (celsius * 9/5) + 32

# Formula 2 - Liter to Gallone
def lit_to_gal(liter):
    result = liter / 3.785
    return round(result, 2)

# Formula 3 - Kilo to Pounds
def kil_to_pou(kilo):
    result = kilo * 2.2046226218487759
    return round(result, 2)

# Declare variables
convert_true = True

# Program is running, while user wants to convert
while convert_true:
    # Check the first user input
    user_input = input("Do you want to convert a value? ( yes / no ): ")

    if user_input == "yes" or user_input == "Yes":
        # Ask user: which type of conversion?
        user_input = input("Which conversion? ( celsius / liter / kilo ): ")

        # Check for different types of conversion
        if user_input == "celsius" or user_input == "Celsius":
            # Ask user for value - Formula 1 - Celsius to Farenheit
            user_input = input("Which value do you want to convert? ")
            print(user_input + " Celsius is " + str(cel_to_far(float(user_input))) + " Farenheit")

        elif user_input == "liter" or user_input == "Liter":
            # Ask user for value - Formula 2 - Liter to Gallone
            user_input = input("Which value do you want to convert? ")
            print(user_input + " Liter(s) is/are " + str(lit_to_gal(float(user_input))) + " Gallon(s)")
        
        elif user_input == "kilo" or user_input == "Kilo":
            # Ask user for value - Formula 3 - Kilo to Pounds
            user_input = input("Which value do you want to convert? ")
            print(user_input + " Kilo(s) is/are " + str(kil_to_pou(float(user_input))) + " Pounds")
        
        else:
            # User enters invalid type of conversion
            print("This input is not valid for conversion.")
            convert_true = False

    elif user_input == "no":
        convert_true = False
    else:
        print("This input is not valid.")
        convert_true = False

print("Thank you - Have a nice day")
