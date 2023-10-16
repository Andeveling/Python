# Creating a tuple
fruits = ('apple', 'banana', 'cherry')

# Accessing tuple elements
print(fruits[0]) # Prints apple

# Immutability
# fruits[0] = 'orange' # TypeError: 'tuple' object does not support item assignment

# Tuple Operations
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined_tuple = tuple1 + tuple2  # Concatenation
sliced_tuple = combined_tuple[1:4]  # Slicing
tuple_length = len(sliced_tuple)  # Length 

# Tuple unpacking

personOne = ('Marcela', 28)
personTwo = ('Andres', 34)
personFour = ('Angelo', 7)
personThree = ('Arya', 1)

newTuple = (personOne, personTwo, personThree, personFour)

a,b,c,d = newTuple

print(a)
