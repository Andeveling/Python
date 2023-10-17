# Create a set
my_set = {"apple", "banana", "cherry"}

# Iterate over the set using a for loop
for fruit in my_set:
    print(fruit)

# Iterate over the set using a list comprehension
fruits = [fruit for fruit in my_set]
print(fruits)

# Iterate over the set using a map function
fruit_lengths = map(len, my_set)
print(fruit_lengths)

# Iterate over the set using a set iterator
my_set_iterator = iter(my_set)
while True:
    try:
        fruit = next(my_set_iterator)
        print(fruit)
    except StopIteration:
        break
