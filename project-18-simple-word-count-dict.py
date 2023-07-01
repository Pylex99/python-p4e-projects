# The purpose of this program is to read the contents of the file "words.txt", count the frequencies of each word in the file, and store the word frequencies in a dictionary. Finally, it prints the dictionary, where the keys represent the unique words and the values represent their respective frequencies in the file.

fhand = open("words.txt")  # Open the file "words.txt"

d = {}  # Initialize an empty dictionary to store word frequencies

for line in fhand:  # Iterate over each line in the file
    word = line.split()  # Split the line into words
    #print(word)
    for wd in word:  # Iterate over each word in the line
        d[wd] = d.get(wd, 0) + 1  # Increment the count of the word in the dictionary (or initialize it to 0 if it doesn't exist)

print(d)  # Print the dictionary containing word frequencies
