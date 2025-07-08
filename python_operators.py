"""
python_operators.py
Demonstrates Python's arithmetic, comparison, logical, identity, membership, bitwise, and assignment operators with examples.
"""

def main():
    # Arithmetic Operators
    print("Addition:", 10 + 5)
    print("Subtraction:", 10 - 5)
    print("Multiplication:", 10 * 5)
    print("Division:", 10 / 5)
    print("Floor Division:", 10 // 5)
    print("Modulus:", 10 % 5)
    print("Exponentiation:", 10 ** 5)
    print("Operator precedence (10 + 5 * 2):", 10 + 5 * 2)
    print("Parentheses change precedence ((10 + 5) * 2):", (10 + 5) * 2)
    print("Mixed operations (10 + 5 - 2 * 3):", 10 + 5 - 2 * 3)

    # Complex expressions with parentheses
    print("10 + 5 * (2 - 3):", 10 + 5 * (2 - 3))
    print("10 + 5 * 2 - 3:", 10 + 5 * 2 - 3)
    print("10 + (5 * 2) - 3:", 10 + (5 * 2) - 3)
    print("10 + 5 * 2 - (3 + 1):", 10 + 5 * 2 - (3 + 1))
    print("10 + 5 * (2 - (3 + 1)):", 10 + 5 * (2 - (3 + 1)))
    print("10 + (5 * 2) - (3 + 1):", 10 + (5 * 2) - (3 + 1))
    print("10 + 5 * 2 - (3 + (1 - 2)):", 10 + 5 * 2 - (3 + (1 - 2)))
    print("10 + (5 * 2) - (3 + (1 - 2)):", 10 + (5 * 2) - (3 + (1 - 2)))
    print("10 + 5 * (2 - (3 + (1 - 2))):", 10 + 5 * (2 - (3 + (1 - 2))))

    # Comparison Operators
    print("10 == 5:", 10 == 5)
    print("10 != 5:", 10 != 5)
    print("10 > 5:", 10 > 5)
    print("10 < 5:", 10 < 5)
    print("10 >= 5:", 10 >= 5)
    print("10 <= 5:", 10 <= 5)

    # Logical Operators
    print("10 > 5 and 5 < 10:", 10 > 5 and 5 < 10)
    print("10 > 5 or 5 < 10:", 10 > 5 or 5 < 10)
    print("not(10 > 5):", not(10 > 5))

    # Identity Operators
    x = [1, 2, 3]
    y = [1, 2, 3]
    print("x is y:", x is y)
    print("x is not y:", x is not y)

    # Membership Operators
    print("1 in x:", 1 in x)
    print("4 not in x:", 4 not in x)

    # Bitwise Operators
    x = 5  # 0101 in binary
    y = 3  # 0011 in binary
    print("Bitwise AND (x & y):", x & y)
    print("Bitwise OR (x | y):", x | y)
    print("Bitwise XOR (x ^ y):", x ^ y)
    print("Bitwise NOT (~x):", ~x)
    print("Bitwise left shift (x << 1):", x << 1)
    print("Bitwise right shift (x >> 1):", x >> 1)

    # Assignment Operators
    x = 5
    x += 3
    print("x after x += 3:", x)
    x -= 2
    print("x after x -= 2:", x)
    x *= 2
    print("x after x *= 2:", x)
    x /= 3
    print("x after x /= 3:", x)

if __name__ == "__main__":
    main()

