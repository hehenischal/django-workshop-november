# Example of nested-if control structure

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You are allowed to drive.")
    else:
        print("You need a driving license to drive.")
else:
    print("You are not old enough to drive.")