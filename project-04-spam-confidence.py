'''Program calculates the average spam confidence from a text file.'''

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

# Open the file using the provided filename
fh = open(fname)

# Initialize variables
tot = 0     # Total spam confidence
num = 0     # Current confidence value
count = 0   # Number of lines processed
av = 0      # Average spam confidence

# Iterate over each line in the file
for line in fh:
    # Check if the line does not start with "X-DSPAM-Confidence:"
    if not line.startswith("X-DSPAM-Confidence:"):
        continue  # Skip to the next line

    # Remove trailing whitespace from the line
    line = line.rstrip()

    # Find the index of the first occurrence of "0" in the line
    pos = line.find("0")

    # Extract the substring starting from "0" until the end of the line and convert it to a float
    num = float(line[pos:])

    # Increment the count variable by 1
    count = count + 1

    # Add the value of num to the total
    tot += num

    # Calculate the average spam confidence
    av = tot / count

# Print the average spam confidence
print("Average spam confidence:", av)