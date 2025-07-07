"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""

x = 5
print(type(x))
x = complex(1j)
print(x)

x = list(("apple", "banana", "cherry"))
print(x)
x = tuple(("apple", "banana", "cherry"))
print(x)

x = range(6)
print(x)

x = dict(name="John", age=36)
print(x)

x = set(("apple", "banana", "cherry"))
print(x)
x = frozenset(("apple", "banana", "cherry"))
print(x)    

 #Slice From the Start
b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[-5:-2])

# String Format F-Strings
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)