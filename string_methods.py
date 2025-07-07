x= "Hello, World!"

# String Methods
print(x.upper())  # Convert to uppercase
print(x.lower())  # Convert to lowercase
print(x.strip())  # Remove whitespace
print(x.split(","))  # Split into a list
print(x.replace("World", "Python"))  # Replace a substring      
print(x.startswith("Hello"))  # Check if string starts with "Hello"
print(x.endswith("!"))  # Check if string ends with "!"
print(x.find("World"))  # Find the position of "World"
print(x.count("o"))  # Count occurrences of "o"         

print(x.isalpha())  # Check if all characters are alphabetic
print(x.isdigit())  # Check if all characters are digits
print(x.isalnum())  # Check if all characters are alphanumeric
print(x.islower())  # Check if all characters are lowercase
print(x.isupper())  # Check if all characters are uppercase
print(x.isspace())  # Check if all characters are whitespace
print(x.capitalize())  # Capitalize the first character
print(x.title())  # Convert to title case

print(x.swapcase())  # Swap case of all characters
print(x.center(50, '*'))  # Center the string with '*' padding  
print(x.ljust(50, '-'))  # Left justify the string with '-' padding
print(x.rjust(50, '-'))  # Right justify the string with '-' padding
print(x.zfill(20))  # Pad the string with zeros on the left
print(x.partition("World"))  # Partition the string at "World"
print(x.rpartition("World"))  # Right partition the string at "World"
print(x.splitlines())  # Split the string into lines
print(x.join(["Start: ", " :End"]))  # Join a list with the string as a separator
print(x.removeprefix("Hello, "))  # Remove prefix "Hello, "
print(x.removesuffix("!"))  # Remove suffix "!"
print(x.casefold())  # Casefold the string for case-insensitive comparisons

# Check if the string is printable
print(x.isprintable())  # Check if all characters are printable
# Check if the string is a valid identifier
print(x.isidentifier())  # Check if the string is a valid identifier
# Check if the string is a valid ASCII string
print(x.isascii())  # Check if all characters are ASCII
# Check if the string is a valid title
print(x.istitle())  # Check if the string is in title case  
# Check if the string is a valid numeric string
print(x.isnumeric())  # Check if all characters are numeric
# Check if the string is a valid decimal string
print(x.isdecimal())  # Check if all characters are decimal