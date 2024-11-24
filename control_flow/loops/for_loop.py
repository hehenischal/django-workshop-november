# Example 1: Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example 2: Iterating over a string
for letter in "hello":
    print(letter)

# Example 3: Using range() function
for i in range(5):
    print(i)

# Example 4: Iterating over a dictionary
person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")

# Example 5: Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")