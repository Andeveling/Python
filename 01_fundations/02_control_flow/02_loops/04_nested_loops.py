""" 
In this example:

We define the range for the multiplication table, from 1 to 10 (inclusive) in this case.

An outer for loop iterates through the rows, from start to end.

Inside the outer loop, there's an inner for loop that iterates through the columns, again from start to end.

Within the inner loop, we calculate the product of the current row and column values (i * j) and print the result using the print() function. The end="\t" argument is used to separate the printed values with a tab character.

After each row is completed (when the inner loop finishes), we use print() with no arguments to move to the next line for the next row.
"""

# Define the range for the multiplication table (e.g., 1 to 10)
start = 1
end = 10

# Outer loop for rows
for i in range(start, end + 1):
    # Inner loop for columns
    for j in range(start, end + 1):
        # Calculate and print the product
        product = i * j
        print(f"{i} x {j} = {product}", end="\t")  # Use '\t' for tab spacing
    # Move to the next line for the next row
    print()
