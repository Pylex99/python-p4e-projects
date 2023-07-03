# The purpose of this program is to read the contents of the file "mbox-short.txt", search for lines starting with "From ", extract the domains from the email addresses in those lines, count the frequencies of each domain, and then print the dictionary of domain frequencies. Finally, it finds and prints the domain with the largest frequency along with its frequency.

fhand = open("mbox-short.txt")  # Open the file "mbox-short.txt"

dic = {}  # Initialize an empty dictionary to store domain frequencies
count = 0  # Initialize a variable to count the lines

for line in fhand:  # Iterate over each line in the file
    if line.startswith("From "):  # If the line starts with "From "
        line = line.rstrip().split()  # Remove trailing whitespace and split the line into words
        print(line)
        for thing in line:  # Iterate over each word in the line
            if "@" in thing:  # If the word contains a "@" symbol
                dom = thing.find("@")  # Find the index of the "@" symbol
                domain = thing[dom + 1:]  # Extract the domain from the word
            else:
                continue  # Skip to the next iteration
            dic[domain] = dic.get(domain, 0) + 1  # Increment the count of the domain in the dictionary (or initialize it to 0 if it doesn't exist)

print(dic)  # Print the dictionary containing domain frequencies

largest = 0  # Initialize a variable to store the largest frequency
em = None  # Initialize a variable to store the domain with the largest frequency

for k, v in dic.items():  # Iterate over each key-value pair in the dictionary
    if v > largest:  # If the frequency is larger than the current largest
        largest = v  # Update the largest frequency
        em = k  # Update the domain with the largest frequency

print(em, largest)  # Print the domain with the largest frequency and its frequency
