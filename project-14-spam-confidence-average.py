# The purpose of this program is to read a file specified by the user, search for lines that start with "X-DSPAM-Confidence:", extract the numerical values from those lines, calculate the average of those values, and display the average on the console.

count = 0  # Initialize a variable to count the occurrences
total = 0  # Initialize a variable to store the total sum

name = input("Enter file:")  # Prompt the user to enter a file name
if len(name) < 1:  # If no file name is provided
    name = "mbox-short.txt"  # Assign a default file name

try:
    fhand = open(name)  # Try to open the specified file
except:
    print("File not found:", name)  # If the file is not found, print an error message
    quit()  # Terminate the program

for line in fhand:  # Iterate over each line in the file
    if line.startswith("X-DSPAM-Confidence:"):  # If the line starts with "X-DSPAM-Confidence:"
        count += 1  # Increment the count
        atpos = line.find(":")  # Find the position of the colon
        num = line[atpos + 1:]  # Extract the number part of the line
        num = float(num)  # Convert the number to a float
        total = total + num  # Add the number to the total sum

print("Average is:", total/count)  # Print the average by dividing the total sum by the count
