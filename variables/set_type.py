# Example of set type variable in Python

# Creating a set
fruits = {"apple", "banana", "cherry"}
print(f"Original set: {fruits}")

# Adding an element to the set
fruits.add("orange")
print(f"Set after adding an element: {fruits}")

# Removing an element from the set
fruits.remove("banana")
print(f"Set after removing an element: {fruits}")

# Checking if an element is in the set
print(f"Is 'apple' in the set? {'apple' in fruits}")

# Iterating through the set
print("Iterating through the set:")
for fruit in fruits:
    print(fruit)

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)
print(f"Union of set1 and set2: {union_set}")

# Intersection
intersection_set = set1.intersection(set2)
print(f"Intersection of set1 and set2: {intersection_set}")

# Difference
difference_set = set1.difference(set2)
print(f"Difference of set1 and set2: {difference_set}")