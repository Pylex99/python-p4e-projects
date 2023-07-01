# The purpose of this program is to read a file specified by the user, search for lines that start with "From ", extract the second word from those lines, count the number of lines that meet the criteria, and display the extracted word and the count of lines on the console.

name = input("Enter file: ")  # Prompt the user to enter a file name
if len(name) < 1:  # If no file name is provided
    name = "mbox-short.txt"  # Assign a default file name

fhand = open(name)  # Open the specified file
count = 0  # Initialize a variable to count the lines

for line in fhand:  # Iterate over each line in the file
    word = line.split()  # Split the line into words
    if line.startswith("From "):  # If the line starts with "From "
        word = word[1]  # Extract the second word (index 1)
        count += 1  # Increment the count
    else:
        continue  # Skip to the next iteration

    print(word)  # Print the second word
print("There were", count, "lines")  # Print the count of lines

