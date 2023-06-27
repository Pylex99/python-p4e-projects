'''The program reads a file and prints each line in uppercase.'''

# Use words.txt as the file name
# Prompt the user to enter the name of the file to be processed
fname = input("Enter file name: ")

# Open the file using the provided filename
fh = open(fname)

# Read the contents of the file and store it in the variable 'text'
text = fh.read()

# Iterate over each line in the file
for line in fh:
    # Remove any trailing whitespace from the line
    i = line.rstrip()
    
    # Print the line in uppercase
    print(i.upper())