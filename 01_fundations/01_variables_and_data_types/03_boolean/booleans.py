# Boolean data types
# Boolean values
# True
# False

# Comparisons and Bolean Expressions

print(1 < 2) # Less than
print(1 > 2) # Greater than 
print(1 == 2) # Equal to
print(1 != 2) # Not equal
print(1 <= 2) # Less than or equal
print(1 >= 2) # Greater than or equal

# Boolean Operators
# Example
x = 10
y = 20
z = 10

print(x < y) # Evaluates to True
print(x > y) # Evaluates to False
print(x == z) # Evaluates to True
print(x != y) # Evaluates to True
print(x <= y) # Evaluates to True


is_sunny = True
is_warm = True

if is_sunny and is_warm:
    print("It's a great day for outdoor sports. Go outside!")


# Truthiness and Falsiness
value = 0
if value:
    print("Value is Truthy")
else:
    print("Value is Falsy")