# Example of mapping type variable in Python

# Creating a dictionary (mapping type)
person = {
    "name": "John",
    "age": 30,
    "city": "New York",
}

# Accessing values using keys
print(person["name"])  # Output: John
print(person["age"])   # Output: 30
print(person["city"])  # Output: New York

# Adding a new key-value pair
person["email"] = "john@example.com"
print(person)

# Updating an existing key-value pair
person["age"] = 31
print(person)

# Removing a key-value pair
del person["city"]
print(person)

# Iterating over keys
for key in person:
    print(key, person[key])

# Iterating over values
for value in person.values():
    print(value)

# Iterating over key-value pairs
for key, value in person.items():
    print(key, value)