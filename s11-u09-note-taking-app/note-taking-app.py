# Note App Start with user Input
user_input = input("What do you want you want to do?\nPress 1 for adding a note\nPress 2 for searching your notes\nPress 3 to quit\n: ")

if user_input == "1":
    # File open with attach
    file = open("note.txt", "a")
    # Get user input and write in note file
    user_input = input("Write your note\n: ")
    file.write(user_input + "\n")
elif user_input == "2":
    # File open
    file = open("note.txt")
    user_input = input("Enter the text to search\n: ")
    # Define variables
    search_result = ""
    # Loop over each line and check for search string
    for text_line in file:
        # Check line for no case sensitive with .lower()
        if text_line.lower().find(user_input.lower()) != -1: # -1 -> no string in note found
            search_result += "---\n" + text_line
    # Print Search result
    if search_result != "":
        print(search_result)
    else:
        print("No note found")
elif user_input == "3":
    print("Program has ended")
    quit()
else:
    print("Entry invalid. Program ended")
    quit()

file.close()
