'''The program calculates corresponding grade based on the score provided by the user.'''

score = input("Enter Score: ")  # Prompt the user to enter a score
try:
    sr = float(score)  # Convert the input to a floating-point number

    if sr >= 0.9:  # Check if the score is greater than or equal to 0.9
        print("A")  # If true, print "A"
    elif sr >= 0.8:  # Check if the score is greater than or equal to 0.8
        print("B")  # If true, print "B"
    elif sr >= 0.7:  # Check if the score is greater than or equal to 0.7
        print("C")  # If true, print "C"
    elif sr >= 0.6:  # Check if the score is greater than or equal to 0.6
        print("D")  # If true, print "D"
    else:
        print("F")  # If none of the above conditions are met, print "F"
except ValueError:
    print("Invalid input. Please enter a valid score.")  # If a ValueError occurs during float conversion, print an error message