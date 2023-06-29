#   The program determines and displays the number of lines containing the word "Subject" in a file specified by the user with the hidden Easter Egg.

fname = input('Enter the file name: ')  # Prompt the user to enter a file name
try:
    if fname == 'na na boo boo':  # If the entered file name is 'na na boo boo'
        print('NA NA BOO BOO TO YOU - You have been punk\'d!')  # Print a specific message
        exit()  # Exit the program
    fhand = open(fname)  # Open the specified file
except FileNotFoundError:  # If the file is not found
    print('File cannot be opened:', fname)  # Print an error message
    exit()  # Exit the program

count = 0  # Initialize a variable to count the occurrences of subject lines

for line in fhand:  # Iterate over each line in the file
    if "Subject" in line:  # If the line contains the substring "Subject"
        count += 1  # Increment the count

print("There were:", count, "subject lines in", fname)  # Print the final count of subject lines
