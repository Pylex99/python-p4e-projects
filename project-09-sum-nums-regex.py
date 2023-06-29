#This program calculates the sum of all the numbers found in a file specified by the user or a default file, using regular expressions to extract the numbers from each line.


import re  # Import the regular expression module

name = input("Enter file:")  # Prompt the user to enter a file name
if len(name) < 1:  # If no input is given
    name = "Actual data.txt"  # Set the file name to "Actual data.txt" by default

hand = open(name)  # Open the specified file
tot = list()  # Initialize an empty list to store numbers
sum = 0  # Initialize a variable to keep track of the sum of numbers

for line in hand:  # Iterate over each line in the file
    ln = line.rstrip()  # Remove any trailing whitespace from the line
    nums = re.findall("[0-9]+", ln)  # Find all numbers in the line using regular expression
    #print(nums)  # Uncomment this line to print the found numbers

    for num in nums:  # Iterate over each found number
        sum = sum + int(num)  # Add the number to the running sum

print(sum)  # Print the final sum of all the numbers
