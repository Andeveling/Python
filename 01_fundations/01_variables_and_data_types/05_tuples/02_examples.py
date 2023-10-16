# 1. Represent 2d and 3d points
point2D = (3, 4)  # Represents a point in 2D space with x=3 and y=4
point3D = (1, 2, 3)  # Represents a point in 3D space with x=1, y=2, and z=3

# 2. Define configuration settings as key-value pairs in a tuple
config_settings = (
    ("server", "example.com"),
    ("port", 8080),
    ("debug_mode", False),
    ("max_connections", 100),
)

# 3. Returning multiple values from a function


def calculate_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


area, perimeter = calculate_area_and_perimeter(4, 5)
# print("Area:", area)
# print("Perimeter:", perimeter)


def calculate_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    return minimum, maximum, total, average


minimum, maximum, total, average = calculate_stats(
    [1, 2, 3, 4, 5, 100, -23, 0])

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Total:", total)
print("Average:", average)
