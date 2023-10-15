""" 
In this example:

The user is prompted to enter a number, which is then converted to an integer using the int() function.

The program checks if the entered number is even or odd by using the modulo operator (%). If number % 2 results in 0, the number is even; otherwise, it's odd.

Based on the result of the if condition, the program prints a message indicating whether the number is even or odd.
"""

# Input: A number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

