'''The program allows the user to enter a series of numbers and finds the largest and smallest numbers among them.'''

largest = None    # Variable to store the largest number
smallest = None   # Variable to store the smallest number

while True:
    num = input("Enter a number: ")  # Prompt the user to enter a number
    if num == "done":  # If the user enters "done", exit the loop
        break

    try:
        num = int(num)  # Convert the input to an integer
        if largest is None:  # If largest is not assigned yet, assign it to the first number
            largest = num
        elif largest < num:  # If the current number is larger than the largest number, update largest
            largest = num
        elif smallest is None:  # If smallest is not assigned yet, assign it to the first number
            smallest = num
        elif smallest > num:  # If the current number is smaller than the smallest number, update smallest
            smallest = num
    except:
        print("Invalid input")  # If the input cannot be converted to an integer, print an error message
        continue  # Continue to the next iteration of the loop

print("Maximum is", largest)    # Print the largest number
print("Minimum is", smallest)   # Print the smallest number