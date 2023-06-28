# This program analyzes a text file and counts the number of lines that start with "From " while extracting and printing the corresponding email addresses.

# Prompt the user to enter a file name
fname = input("Enter file name: ")

# Open the file with the provided name
fh = open(fname)

# Initialize a variable to keep track of the count
count = 0

# Iterate over each line in the file
for line in fh:
    # Check if the line does not start with "From "
    if not line.startswith("From "):
        # Skip to the next iteration if it doesn't start with "From "
        continue
    else:
        # Remove trailing whitespace from the line
        line = line.rstrip()
        
        # Split the line into a list of words
        ln = line.split()
        
        # Extract the email address from the second element of the list
        eml = ln[1]
        
        # Increment the count by 1
        count += 1
        
        # Print the email address
        print(eml)

# Print the total count of lines starting with "From "
print("There were", count, "lines in the file with From as the first word")