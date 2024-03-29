'''Program calculates overall pay combining base hourly salary rate and overtime'''

def computepay(h, r):
    # Check if the number of hours worked is less than or equal to 40.
    if h <= 40:
        # If true, calculate the payment by multiplying the hours worked by the hourly rate.
        print(h * r)
    else:
        # If the number of hours worked is greater than 40, calculate the payment using the formula for overtime.
        return (r * 40 + (r * 1.5) * (h - 40))

# Prompt the user to enter the number of hours worked and convert it to float.
hrs = input("Enter hours: ")
h = float(hrs)

# Prompt the user to enter the hourly rate and convert it to float.
rate = input("Enter Rate: ")
r = float(rate)

# Call the function.
p = computepay(h, r)

# Print the calculated payment.
print("Pay", p)