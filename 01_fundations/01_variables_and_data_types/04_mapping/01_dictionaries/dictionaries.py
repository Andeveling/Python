# Creating a dictionary
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A",
}

# Accessing dictionary elements
print(student["name"])  # Prints Alice
print(student["age"])  # Prints 25

# Modifying dictionary elements
student["grade"] = "B"
print(student["grade"])  # Prints B

# Adding dictionary elements
student["city"] = "New York"
student["isSingle"] = True
print(student)

# Removing dictionary elements
del student["isSingle"]
print(student)

# Dictionaries Operations
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A",
    "city": "New York",
    "isSingle": True,
    "roommates": ["Bob", "Charlie", "David", "Eve"],
}

# Checking if a key exists
print("name" in student)  # Prints True
print("inmigrant" in student)  # Prints False

# Getting a list of keys
print(student.keys())  # Prints ['name', 'age', 'grade', 'city', 'isSingle', 'roommates']
 
# Getting a list of values
print(student.values())  # Prints ['Alice', 25, 'A', 'New York', True, ['Bob', 'Charlie', 'David', 'Eve']]

# Copying a dictionary
new_student = student.copy()
print(new_student)  # Prints {'name': 'Alice', 'age': 25, 'grade': 'A', 'city': 'New York', 'isSingle': True, 'roommates': ['Bob', 'Charlie', 'David', 'Eve']}

# Iterating over a dictionary
for key in student:
    print(key)  # Prints name, age, grade, city, isSingle, roommates

# Dictionary unpacking
personOne = {'name': 'Alice', 'age': 25} # Create a dictionary
personTwo = {'name': 'Bob', 'age': 30} # Create a dictionary
personThree = {'name': 'Charlie', 'age': 35} # Create a dictionary

newDictionary = {'personOne': personOne, 'personTwo': personTwo, 'personThree': personThree} # Create a dictionary

a, b, c = newDictionary

# Dictionary comprehension to create a dictionary of squares
numbers = [1, 2, 3, 4, 5]
squares = {num: num ** 2 for num in numbers}
print(squares)