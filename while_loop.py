"""
while_loop.py
Demonstrates various while loop patterns and control flow in Python.
"""

def main():
    # Simple while loop
    print("Simple while loop from 1 to 6:")
    i = 1
    while i <= 6:
        print(i)
        i += 1

    # While loop with break and nested if
    print("\nWhile loop from 44 to 65, break at 55 and print if even:")
    i = 44
    while i < 66:
        print(i)
        if i == 55:
            if i % 5 == 0:
                print("Even number", i)
            break
        i += 1

    # While loop with continue
    print("\nWhile loop with continue (skip 3):")
    i = 0
    while i < 6:
        i += 1
        if i == 3:
            continue
        print(i)

if __name__ == "__main__":
    main()