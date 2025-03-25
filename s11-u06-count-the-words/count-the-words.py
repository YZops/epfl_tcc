# Count the words from file
file = open("zen_of_python.txt")
zen_content = file.read().strip() # Strip - Remove unwanted spaces
file.close()

# Remove special characters from text
zen_parsed = zen_content.replace("'", "").replace("*", "").replace("-", "").replace(",", "").replace(".", "").replace("!", "").replace("\n", " ")

# Print count of words
print("Word Count: " + str(len(zen_parsed.split())))

# Replace every word "is" with "should be"
zen_content = zen_content.replace("is", "should be")

# Transform into uppercase
zen_content = zen_content.upper()

# Display text with modifications including punctuation and special characters
print(zen_content)
