# Example of built-in functions in Python

# Using the `len()` function to get the length of a list
my_list = [1, 2, 3, 4, 5]
print("Length of my_list:", len(my_list))

# Using the `max()` function to get the maximum value in a list
print("Maximum value in my_list:", max(my_list))

# Using the `min()` function to get the minimum value in a list
print("Minimum value in my_list:", min(my_list))

# Using the `sum()` function to get the sum of all elements in a list
print("Sum of all elements in my_list:", sum(my_list))

# Using the `sorted()` function to get a sorted version of a list
print("Sorted my_list:", sorted(my_list))

# Using the `abs()` function to get the absolute value of a number
negative_number = -10
print("Absolute value of negative_number:", abs(negative_number))

# Using the `round()` function to round a floating point number
floating_number = 3.14159
print("Rounded floating_number:", round(floating_number, 2))

# Using the `type()` function to get the type of an object
print("Type of my_list:", type(my_list) == list)

# Using the `isinstance()` function to check if an object is an instance of a class
print("Is my_list an instance of list?", isinstance(my_list, list))

# Using the `zip()` function to combine two lists into a list of tuples
list1 = [1, 2, 3,]
list2 = ['a', 'b', 'c']
print("Zipped list1 and list2:", list(zip(list1, list2)))