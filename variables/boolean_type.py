# boolean_type.py

# Boolean variables
is_sunny = True
is_raining = False

# Using boolean variables in conditions
if is_sunny:
    print("It's a sunny day!")
else:
    print("It's not sunny today.")

if is_raining:
    print("Don't forget your umbrella!")
else:
    print("No need for an umbrella today.")

# Boolean expressions
is_weekend = True
is_holiday = False

# Combining boolean expressions
if is_weekend and not is_holiday:
    print("It's the weekend, but not a holiday.")
elif is_weekend and is_holiday:
    print("It's a holiday weekend!")
else:
    print("It's a regular weekday.")