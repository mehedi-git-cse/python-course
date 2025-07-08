"""
basic.py
Demonstrates basic Python syntax, comments, variables, and scope.
"""

def main():
    # Single-line comment
    print("Hello, World!")

    # Multi-line comment
    """
    This is a comment
    written in
    more than just one line
    """
    print("Hello, World!")

    # Creating Variables
    x = 5
    y = "John"
    print("x:", x)
    print("y:", y)

    # Assigning multiple values to multiple variables
    x, y, z = "Orange", "Banana", "Cherry"
    print("x:", x)
    print("y:", y)
    print("z:", z)

    # Assigning one value to multiple variables
    x = y = z = "Orange"
    print("x:", x)
    print("y:", y)
    print("z:", z)

    # Unpacking a list
    fruits = ["apple", "banana", "cherry"]
    x, y, z = fruits
    print("x:", x)
    print("y:", y)
    print("z:", z)

    # Global and local variables
    x = "awesome"
    def myfunc11():
        print("Python is " + x)
    myfunc11()

    def myfunc2():
        x = "fantastic"
        print("Python is " + x)
    myfunc2()

    print("Python is " + x)

if __name__ == "__main__":
    main()