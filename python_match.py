"""
python_match.py
Demonstrates the use of match-case (structural pattern matching) in Python to select a day based on user input.
"""

def main():
    try:
        day = int(input("Enter a day number (1-7): "))
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 7.")
        return

    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Invalid day number. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()