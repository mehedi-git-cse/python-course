"""
for.py
Demonstrates a for loop in Python and prints a triangle (trivuj) of stars.
"""

def main():
    fruits = ["apple", "banana", "cherry"]
    print("Fruits in the list:")
    for x in fruits:
        print(x)

    n = 10
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))

if __name__ == "__main__":
    main()