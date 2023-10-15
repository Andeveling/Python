# Break
# break: It allows you to exit the loop prematurely, even if the loop condition is still `True.
for number in [1, 2, 3, 4, 5]:
    if number == 3:
        break
    print(number) # Prints 1, 2


# Continue
# continue: It allows you to skip the current iteration of the loop and continue with the next iteration
for number in [1, 2, 3, 4, 5]:
    if number == 3:
        continue
    print(number) # Prints 1, 2, 4, 5
