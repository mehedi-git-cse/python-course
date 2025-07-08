"""
string_methods.py
Demonstrates various string methods in Python with examples and explanations.
"""

def main():
    x = "Hello, World!"
    print(f"Original string: {x}\n")

    # Basic string transformations
    print("Uppercase:", x.upper())
    print("Lowercase:", x.lower())
    print("Stripped:", x.strip())
    print("Split by comma:", x.split(","))
    print("Replace 'World' with 'Python':", x.replace("World", "Python"))
    print("Starts with 'Hello':", x.startswith("Hello"))
    print("Ends with '!':", x.endswith("!"))
    print("Find 'World':", x.find("World"))
    print("Count of 'o':", x.count("o"))

    # String property checks
    print("Is alpha:", x.isalpha())
    print("Is digit:", x.isdigit())
    print("Is alphanumeric:", x.isalnum())
    print("Is lowercase:", x.islower())
    print("Is uppercase:", x.isupper())
    print("Is whitespace:", x.isspace())
    print("Capitalize:", x.capitalize())
    print("Title case:", x.title())
    print("Swap case:", x.swapcase())
    print("Center (width 50, '*'):", x.center(50, '*'))
    print("Left justify (width 50, '-'):", x.ljust(50, '-'))
    print("Right justify (width 50, '-'):", x.rjust(50, '-'))
    print("Zero fill (width 20):", x.zfill(20))
    print("Partition at 'World':", x.partition("World"))
    print("Right partition at 'World':", x.rpartition("World"))
    print("Split lines:", x.splitlines())
    print("Join with separator:", x.join(["Start: ", " :End"]))
    print("Remove prefix 'Hello, ':", x.removeprefix("Hello, "))
    print("Remove suffix '!':", x.removesuffix("!"))
    print("Casefold:", x.casefold())
    print("Is printable:", x.isprintable())
    print("Is identifier:", x.isidentifier())
    print("Is ASCII:", x.isascii())
    print("Is title:", x.istitle())
    print("Is numeric:", x.isnumeric())
    print("Is decimal:", x.isdecimal())

if __name__ == "__main__":
    main()