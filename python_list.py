"""
python_list.py
Demonstrates basic list operations in Python.
"""

def main():
    # Creating a list
    thislist = ["apple", "banana", "cherry"]
    print("Original list:", thislist)

    # Different types of lists
    list1 = ["apple", "banana", "cherry"]
    list2 = [1, 5, 7, 9, 3]
    list3 = [True, False, False]

    # Concatenating lists
    list4 = list1 + list2 + list3
    print("Concatenated list:", list4)

    # Repeating a list
    list5 = list1 * 2
    print("Repeated list:", list5)

if __name__ == "__main__":
    main()