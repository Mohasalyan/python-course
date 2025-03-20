# Integer
num = 10
print("Integer before change:", num)
num = 25
print("Integer after change:", num)

# Conditional statement with integer
if num > 20:
    print("The number is greater than 20")
else:
    print("The number is 20 or less")

# Float
pi = 3.14
print("\nFloat before change:", pi)
pi = 2.718
print("Float after change:", pi)

# Conditional with float
if pi < 3:
    print("pi is less than 3")
else:
    print("pi is greater than or equal to 3")

# String
text = "Hello, World!"
print("\nString before change:", text)
text = "Python is fun!"
print("String after change:", text)

# Checking string length
if len(text) > 10:
    print("The text is longer than 10 characters")

# Boolean
is_valid = True
print("\nBoolean before change:", is_valid)
is_valid = False
print("Boolean after change:", is_valid)

# Using boolean in an if statement
if is_valid:
    print("The value is True")
else:
    print("The value is False")

# List
numbers = [1, 2, 3, 4, 5]
print("\nList before change:", numbers)
numbers.append(6)
print("List after change:", numbers)

# Looping through list
print("\nLooping through list:")
for num in numbers:
    print(num, end=" ")  # Print numbers in one line
print()

# Tuple (Immutable)
coordinates = (10, 20)
print("\nTuple:", coordinates)  # Tuples can't be changed

# Dictionary
person = {"name": "Alice", "age": 30}
print("\nDictionary before change:", person)
person["age"] = 31
print("Dictionary after change:", person)

# Looping through dictionary
print("\nLooping through dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# Set
fruits = {"apple", "banana", "cherry"}
print("\nSet before change:", fruits)
fruits.add("orange")
print("Set after change:", fruits)

# Looping through set
print("\nLooping through set:")
for fruit in fruits:
    print(fruit)

# Using a while loop
count = 5
print("\nUsing a while loop:")
while count > 0:
    print("Countdown:", count)
    count -= 1

print("Done!")
