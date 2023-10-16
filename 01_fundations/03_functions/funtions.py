# 1. Functions def keywords
def function_name():
    # body of the function
    # Perform operations
    # Optional return a value
    print("Hello World")

# Function with parameters and default values


def describe_person(name, age=25, city="New York", *hobbies, **info):

    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"City: {city}")
    print(f"Hobbies: {', '.join(hobbies)}")
    print("Additional Info:")
    for key, value in info.items():
        print(f"{key}: {value}")


# Call the function
describe_person("Andres", 34, "Buga", "Reading", "Writing",
                "Programming", height=160, weight=65, country="Colombia")

# Explain arbitrary arguments
# Use *args


def number_of_args(*args):
    result = 0
    for number in args:
        result += number
    return result


print(number_of_args(1, 2, 3, 4, 5))  # Prints 15

# Explain arbitrary keyword arguments
# Use **kwargs


def person(**kwargs):
    newPerson = {}
    for key, value in kwargs.items():
        newPerson[key] = value
    return newPerson


# Prints Name: Andres, Age: 34, City: Buga, Country: Colombia
print(person(name="Andres", age=34, city="Buga", country="Colombia"))
