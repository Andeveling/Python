""" 
In this example:

We have a list called numbers containing five integers.
We initialize a variable sum_of_numbers to store the sum of the numbers.
We use a for loop to iterate through the numbers list.
Inside the loop, we add each number to the sum_of_numbers variable using the += operator.
After the loop, we print the result, which is the sum of the numbers in the list.
"""
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Initialize a variable to store the sum
sum_of_numbers = 0

# Use a for loop to iterate through the list and calculate the sum
for number in numbers:
    sum_of_numbers += number

# Print the result
print(f"The sum of numbers in the list is: {sum_of_numbers}") # Prints 15
