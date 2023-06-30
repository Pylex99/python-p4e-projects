# The purpose of this program is to read a file specified by the user, extract all unique words from the file, store them in a list, sort the list alphabetically, and display the count of unique words and the sorted list on the console.

fhand = open(input("Enter file name: "))  # Prompt the user to enter a file name and open the file

words = list()  # Initialize an empty list to store unique words

for line in fhand:  # Iterate over each line in the file
    word = line.rstrip().split()  # Remove trailing whitespace and split the line into words
    for item in word:  # Iterate over each word in the line
        if item in words:  # If the word is already in the list
            continue  # Skip to the next iteration
        words.append(item)  # Add the word to the list

words.sort()  # Sort the list of words alphabetically

print(len(words))  # Print the number of unique words
print(words)  # Print the list of unique words
