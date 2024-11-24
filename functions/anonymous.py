# Example of using lambda functions in Python

# A simple lambda function to add 10 to a number
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

# A lambda function to multiply two numbers
multiply = lambda x, y: x * y
print(multiply(2, 3))  # Output: 6

# Using lambda function with the built-in sorted() function
points = [(1, 2), (4, 1), (5, -1), (3, 3)]
sorted_points = sorted(points, key=lambda point: point[1])
print(sorted_points)  # Output: [(5, -1), (4, 1), (1, 2), (3, 3)]

# Using lambda function with the built-in map() function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Using lambda function with the built-in filter() function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]