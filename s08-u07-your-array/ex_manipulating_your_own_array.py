# Pick up favorite song array
favorite_songs = ["Jolene",
                  "Like a Rolling Stone",
                  "Imagine",
                  "What's Going On"]

# Sort it by alphabetical order.
favorite_songs.sort()
#print(favorite_songs) # For testing

# Display each song in it on its own line in the terminal.
print(favorite_songs[0])
print(favorite_songs[1])
print(favorite_songs[2])
print(favorite_songs[3])

# Add a 5th song at the end of the array.
favorite_songs.append("Respect")
#print(favorite_songs) # For testing

# Display how many songs are in the array inside a sentence such as "There are x songs in the array."
arr_num_songs = len(favorite_songs)
print("There are " + str(arr_num_songs) + " songs in the array.")

# Remove the 3rd song in the array.
favorite_songs.pop(2)
#print(favorite_songs) # For testing

# Display the content of the array on one line.
print(favorite_songs)

# Display the length of the array.
print(len(favorite_songs))
