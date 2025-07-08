"""
data_type.py
Demonstrates Python's built-in data types and related string operations.
"""

def main():
    # Numeric Types
    x = 5
    print("Type of x (int):", type(x))
    x = complex(1j)
    print("Complex number:", x)

    # Sequence Types
    x = list(("apple", "banana", "cherry"))
    print("List:", x)
    x = tuple(("apple", "banana", "cherry"))
    print("Tuple:", x)
    x = range(6)
    print("Range:", list(x))

    x = range(6, 0, -1)  # Range with start, stop, step
    print("Range with start, stop, step:", list(x))

    # Mapping Type
    x = dict(name="John", age=36)
    print("Dictionary:", x)

    # Set Types
    x = set(("apple", "banana", "cherry"))
    print("Set:", x)
    x = frozenset(("apple", "banana", "cherry"))
    print("Frozenset:", x)

    # String Slicing
    b = "Hello, World!"
    print("Slice from start (b[:5]):", b[:5])
    print("Slice with negative indices (b[-5:-2]):", b[-5:-2])

    # String Format F-Strings
    price = 59
    txt = f"The price is {price:.2f} dollars"
    print("Formatted string (f-string):", txt)

    # Escape Character in F-String
    txt = f"We are the so-called \"{price}\" from the north."
    print("Escaped character in f-string:", txt)

if __name__ == "__main__":
    main()