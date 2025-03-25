# Celsius zu Rankine (℃ zu ºR)
# Formula: Rankine = (Celsius * 1.8) + 491.67
# Testinput to check
# 0 degrees Celsius are 491.67 Rankine.
# 2 degrees Celsius are 495.27 Rankine.
# 16.5 degrees Celsius are 521.37 Rankine.
# -20 degrees Celsius are 455.67 Rankine.

# 13. Exercise: Upgrading your converter. Again.

def celsius_to_rankine(celsius):
    # Statment if it's hot
    if user_input > 38:
        print("It's really hot. T-Shirt weather and a lot of water.")
    # Statment if it's very cold
    if user_input < 0:
        print("Don't forget your jacket.")
    
    # Calculation Celsius to Rankine
    result_rankine = (celsius * 1.8) + 491.67
    msg_01 = " degrees Celsius are "
    msg_02 = " Rankine."
    return str(celsius) + msg_01 + str(round(result_rankine, 2)) + msg_02

# User Input for Celsius
user_input = float(input("Enter a temperature in degrees Celsius: "))

# Calculation in Rankine
print(celsius_to_rankine(user_input))
