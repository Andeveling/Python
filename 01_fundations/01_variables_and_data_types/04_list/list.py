""" 
Lists in a Nutshell

    -Lists are ordered collections of elements.
    -They are mutable, allowing you to modify, add, or remove elements.
    -Lists can hold a mix of different data types.
    -You can access elements by their index, and Python uses zero-based indexing.
    -Lists support various operations for manipulation and data processing.

 Lists are a fundamental data structure in Python and are widely used for storing, 
 processing, and organizing data in various applications and scenarios. Understanding 
 lists is crucial for Python developers, as they form the building blocks for more 
 complex data structures and algorithms.
"""
# List in Python

# Creating a list
numbers = [1, 2, 3]
family = ['Arya', 'Angelo', 'Marcela', 'Andres']
# also
children = list(['Arya', 'Angelo'])

# Accessing list elements
print(numbers[0]) # Prints 1
print(family[0]) # Prints Arya

# Modifying list elements
numbers[0] = 5
print(numbers[0]) # Prints 5

# List operations
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2  # Concatenation
sliced_list = combined_list[1:4]  # Slicing
list_length = len(sliced_list)  # Length
combined_list.sort()  # Sorting in ascending order

# List comprehensions
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]  # List comprehension to square each number

# List methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # Append
numbers.insert(0, 0)  # Insert
numbers.pop()  # Pop
numbers.remove(2)  # Remove
numbers.reverse()  # Reverse
numbers.sort()  # Sort