
# Create a string
first_name = "Andres"
last_name = "Parra"

# String Operations

# 1. Concatenate
full_name = first_name + " " + last_name

# 2. Indexing
text = "Python"
print(text[0])
print(text[1])
print(text[2])
print(text[3])
print(text[4])
print(text[5])


# 3. Slicing
text_slice = text[0:3]
print(text_slice) # Print "Pyth"


# 4. Length
text = "Hello, World!"
print(len(text)) # Returns 13

# 5. String Basic Methods
message = "Hello, Python!"
lower_case = message.lower() # Converts "Hello, Python!" to "hello, python!"
word_count = message.count("o") # Returns 2
words = message.split(", ") # Splits "Hello, Python!" into ["Hello", "Python!"]

# 6. Escape Sequences
message = "This is a line. \nThis is another line."
tabbed = 'First element\tSecond element'
quote = "He said, \"This is a quote.\""

print("Message: ", message)
print("--"*10)
print("Tabbed: ", tabbed)
print("--"*10)
print("Quote: ", quote)
print("--"*10)


# 7. String Formatting
name = "Arya"
age = 1

# Example with string concatenation
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

# Example with str.format()
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)



