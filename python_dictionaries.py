"""
python_dictionaries.py
Demonstrates basic dictionary operations in Python.
"""

def main():
    # Creating a dictionary
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print("model1:", thisdict["model"])   # Access using key
    print("model (using get):", thisdict.get("model"))

    # Accessing Dictionary Keys
    car = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    x = car.keys()
    print("Type of keys:", type(x))
    car["color"] = "white"
    print("Keys after adding 'color':", list(x))

    # Accessing Dictionary Values
    x = car.values()
    print("Values before change:", list(x))
    car["year"] = 2020
    print("Values after change:", list(x))

    # Check if Key Exists
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    print("Type of thisdict:", type(thisdict))
    if "model" in thisdict:
        print("Yes, 'model' is one of the keys in the thisdict dictionary")

    # Updating Items
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    thisdict.update({"year": 2020})
    print("Updated dictionary:", thisdict)

    # Removing an Item
    thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
    removed = thisdict.pop("model")
    print("Dictionary after removing 'model':", thisdict)
    print("Removed value:", removed)

    # Iterating through dictionary keys
    print("Dictionary keys:")
    for key in thisdict:
        print(key)

    # Iterating through dictionary values (by key)
    print("Dictionary values (by key):")
    for key in thisdict:
        print(thisdict[key])

    # Iterating through dictionary values (using .values())
    print("Dictionary values (using .values()):")
    for value in thisdict.values():
        print(value)

    # Iterating through dictionary keys (using .keys())
    print("Dictionary keys (using .keys()):")
    for key in thisdict.keys():
        print(key)

    # Iterating through dictionary items
    print("Dictionary items (key-value pairs):")
    for key, value in thisdict.items():
        print(key, value)

if __name__ == "__main__":
    main()