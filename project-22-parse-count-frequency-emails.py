# The purpose of this program is to read the contents of the file "mbox-short.txt", search for lines starting with "From ", extract the email addresses from those lines, count the frequencies of each email address, and then print the email address with the highest frequency along with its frequency.

fhand = open("mbox-short.txt")  # Open the file "mbox-short.txt"

dic = {}  # Initialize an empty dictionary to store email frequencies

for line in fhand:  # Iterate over each line in the file
    if line.startswith("From "):  # If the line starts with "From "
        line = line.rstrip().split()  # Remove trailing whitespace and split the line into words
        line = line[1]  # Get the second word (email address)
    else:
        continue  # Skip to the next iteration
    dic[line] = dic.get(line, 0) + 1  # Increment the count of the email address in the dictionary (or initialize it to 0 if it doesn't exist)

#print(dic)  # Print the dictionary containing email frequencies

lst = list()  # Initialize an empty list to store (frequency, email) tuples

for k, v in dic.items():  # Iterate over each key-value pair in the dictionary
    lst.append((v, k))  # Append the (frequency, email) tuple to the list

lst.sort(reverse=True)  # Sort the list in descending order based on the frequency

for k, v in lst[:1]:  # Iterate over the first element in the sorted list (highest frequency)
    print(v, k)  # Print the email address and its frequency
