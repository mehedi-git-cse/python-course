#This is a comment
print("Hello, World!")

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#Creating Variables
x = 5
y = "John"
print(x)
print(y)

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Global Variables

x = "awesome"

def myfunc11():
  print("Python is " + x)

myfunc11()

def myfunc2():
  x = "fantastic"
  print("Python is " + x)

myfunc2()

print("Python is " + x)