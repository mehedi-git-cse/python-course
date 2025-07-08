"""
nested_dictionaries.py
Demonstrates the use of nested dictionaries in Python.
"""

def main():
    # Define child dictionaries
    child1 = {
        "name": "Emil",
        "year": 2004
    }
    child2 = {
        "name": "Tobias",
        "year": 2007
    }
    child3 = {
        "name": "Linus",
        "year": 2011
    }

    # Create a nested dictionary
    myfamily = {
        "child1": child1,
        "child2": child2,
        "child3": child3
    }

    # Accessing nested dictionary values
    print("Name of child2:", myfamily["child2"]["name"])

    # Iterating through nested dictionaries
    for child_key, child_info in myfamily.items():
        print(f"\n{child_key}:")
        for attr, value in child_info.items():
            print(f"  {attr}: {value}")

if __name__ == "__main__":
    main()