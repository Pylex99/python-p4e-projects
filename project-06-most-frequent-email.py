# Program analyzes a text file containing email data and identifies the email address that appears most frequently.


# Prompt the user to enter a file name
name = input("Enter file name: ")

# If no name is provided, set the default file name to "mbox-short.txt"
if len(name) < 1:
    name = "mbox-short.txt"

# Open the file with the provided or default name
handle = open(name)

# Create an empty dictionary to store email addresses and their occurrence count
eml = dict()

# Iterate over each line in the file
for line in handle:
    # Check if the line starts with "From "
    if line.startswith("From "):
        # Remove trailing whitespace and split the line into a list of words
        ln = line.rstrip().split()
        
        # Extract the email address from the second element of the list
        emails = ln[1]
        
        # Increment the count for the email address in the dictionary,
        # or add it to the dictionary with a count of 1 if it doesn't exist
        eml[emails] = eml.get(emails, 0) + 1

# Initialize variables to store the email address with the highest count
bigword = None
bigcount = None

# Iterate over each email address and count in the dictionary
for emails, count in eml.items():
    # Check if the current count is higher than the previous highest count
    if bigcount is None or count > bigcount:
        # Update the variables with the current email address and count
        bigword = emails
        bigcount = count

# Print the email address with the highest count
print(bigword, bigcount)