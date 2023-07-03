# The purpose of this program is to read the contents of the file "mbox-short.txt", search for lines starting with "From ", extract the hour from the time in those lines, count the frequencies of each hour, and then print the hours and their frequencies in sorted order.

fhand = open("mbox-short.txt")  # Open the file "mbox-short.txt"

d = {}  # Initialize an empty dictionary to store hour frequencies

for line in fhand:  # Iterate over each line in the file
    if line.startswith("From "):  # If the line starts with "From "
        line = line.rstrip().split()  # Remove trailing whitespace and split the line into words
        line = line[5]  # Get the sixth word (time)
        for hr in line:  # Iterate over each character in the time
            hr = line.split(":")  # Split the time at the colon
            hr = hr[0]  # Get the first element (hour)
        d[hr] = d.get(hr, 0) + 1  # Increment the count of the hour in the dictionary (or initialize it to 0 if it doesn't exist)

#print(d)  # Print the dictionary containing hour frequencies

lst = list()  # Initialize an empty list to store (hour, frequency) tuples

for k, v in sorted(d.items()):  # Iterate over each key-value pair in the sorted dictionary
    print(k, v)  # Print the hour and its frequency
