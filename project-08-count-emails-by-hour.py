# This program is about reading the contents of a file, specifically lines starting with "From ", extracting the hour of the day from those lines, and counting the occurrences of each hour. It then displays the sorted results of the hour counts.


name = input("Enter file:")  # Prompt the user to enter a file name
if len(name) < 1:  # If no input is given
    name = "mbox-short.txt"  # Set the file name to "mbox-short.txt" by default

handle = open(name)  # Open the specified file
words = dict()  # Initialize an empty dictionary to store the hour counts

for line in handle:  # Iterate over each line in the file
    if line.startswith("From "):  # If the line starts with "From "
        ln = line.split()  # Split the line into words
        ln = ln[5]  # Get the sixth word (time in the format "hh:mm:ss")
        ln = ln[:2]  # Keep only the first two characters (hour)
        words[ln] = words.get(ln, 0) + 1  # Increment the count for that hour in the dictionary
    else:
        continue  # If the line doesn't start with "From ", skip to the next line

lst = list()  # Initialize an empty list to store hour and count pairs

for val, count in words.items():  # Iterate over the items (hour, count) in the dictionary
    lst.append((val, count))  # Append the hour and count pair to the list

lst.sort()  # Sort the list in ascending order based on the hour values

for val, count in lst:  # Iterate over the sorted list
    print(val, count)  # Print the hour and count pair
