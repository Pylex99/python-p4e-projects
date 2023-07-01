# The purpose of this program is to prompt the user to enter a series of numbers, store them in a list, and then find and print the maximum and minimum values from the entered numbers. The program continues to prompt for numbers until the user enters "done" to signal the end of input.

lst = list()  # Initialize an empty list to store numbers

while True:
    inp = input("Enter any number: ")  # Prompt the user to enter a number
    if inp == "done":  # If the user enters "done"
        break  # Exit the loop
    else:
        lst.append(inp)  # Add the entered number to the list

print("Maximum: ", float(max(lst)))  # Print the maximum value in the list after converting it to float
print("Minimum: ", min(lst))  # Print the minimum value in the list
