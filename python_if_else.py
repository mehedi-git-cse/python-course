a = 5
b = 4

if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")       
else:
    print("a is equal to b")

# Example with multiple conditions
if a > b and a > 0:
    print("a is greater than b and a is positive")
elif a < b or a < 0:
    print("a is less than b or a is negative")
else:
    print("a is equal to b or a is negative")

# Example with nested if statements
if a > b:
    print("a is greater than b")
    if a > 10:
        print("a is also greater than 10")
    else:
        print("a is not greater than 10")
elif a < b:
    print("a is less than b")
    if a < 0:
        print("a is negative")
    else:
        print("a is non-negative")
else:
    print("a is equal to b")
    if a == 0:
        print("a is zero")
    else:
        print("a is non-zero")

# Example with a single condition
if a > 0:
    print("a is positive")  
else:
    print("a is not positive")