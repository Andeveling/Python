"""
In this example:

The user is prompted to enter a number, which is then converted to an integer using the int() function.

We initialize the factorial variable to 1 to store the result and the current_number variable to 1 as the starting point.

A while loop is used to calculate the factorial. It iterates as long as current_number is less than or equal to the entered number.

Inside the loop, the factorial is updated by multiplying it with the current_number, and current_number is incremented by 1 in each iteration.

After the loop, the program prints the result, which is the factorial of the entered number.
"""
# Input: A number for which to calculate the factorial
number = int(input("Enter a number: "))

# Initialize variables
factorial = 1
current_number = 1

# Calculate the factorial using a while loop
while current_number <= number:
    factorial *= current_number
    current_number += 1

# Print the result
print(f"The factorial of {number} is {factorial}") 
