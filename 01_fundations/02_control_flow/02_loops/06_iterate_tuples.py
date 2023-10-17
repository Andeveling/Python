animals: tuple[str] = ("dog", "cat", "bird", "horse")
numbers: tuple[int] = (1, 2, 3, 4)


# Iterate a list
for animal in animals:
    print("I love: ", animal)

# Iterate a list
for number in numbers:
    result = number * 2
    print(result)

# Iterate two lists at the same time
for numbers, animals in zip(numbers, animals):
    print(numbers, animals)

# Iterate num in range()
for num in range(1, 10+1):
    print(num)

numbers: list[int] = [1, 2, 3, 4]

# Iterate nums with enumerate
for num in enumerate(numbers):
    print(num)
    # else:
    #     print("Done!")
    
    
# Iterate over the list using a list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]

# Iterate over the list using a list map function
square_numbers = list(map(lambda num: num ** 2, numbers))
print(square_numbers)

# Iterate over the list using a list iterator
my_list_iterator = iter(numbers)
while True:
    try:
        element = next(my_list_iterator)
        print(element)
    except StopIteration:
        break