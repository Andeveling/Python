# Create a set
fruits = {"apple", "banana", "cherry"}
colors = set(["red", "green", "blue"])

# Adding elements to a set
fruits.add("orange")
colors.add("orange")

# Removing elements from a set
fruits.remove("orange")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5}
union_result = set1 | set2  # Union
intersection_result = set1 & set2  # Intersection
difference_result = set1 - set2  # Difference
is_subset = set1.issubset(set2)  # Subset check
is_superset = set1.issuperset(set2)  # Superset check

print(is_subset)
print(is_superset)
