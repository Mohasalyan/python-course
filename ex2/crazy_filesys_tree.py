# String Operations & Slicing - Practice & Review

# 1. String Functions
s = "Hello, World!"

print("Original string:", s)

# Length of the string
print("Length:", len(s))

# Convert to uppercase
print("Uppercase:", s.upper())

# Convert to lowercase
print("Lowercase:", s.lower())

# Check start and end
print("Starts with 'Hello'?", s.startswith("Hello"))
print("Ends with 'World!'?", s.endswith("World!"))

# Find a substring
print("Index of 'World':", s.find("World"))

# Replace substring
print("Replace 'World' with 'Python':", s.replace("World", "Python"))

# Splitting and joining
words = s.split(", ")
print("Splitted:", words)
print("Joined with '-':", "-".join(words))

print("\n" + "="*30 + "\n")  # Separator for readability

# 2. String Slicing
t = "Python Programming"

print("Original string:", t)

# Extracting substrings
print("First 6 chars:", t[:6])
print("Substring from index 7:", t[7:])
print("Last 3 chars:", t[-3:])

# Skipping characters
print("Every second character:", t[::2])
print("Reversed:", t[::-1])

print("\n" + "="*30 + "\n")  # Separator for readability

# 3. Practice Exercises
print("Practice Exercises:")
print("1. Extract the word 'Programming' using slicing.")
print("2. Reverse the string 'abcdef'.")
print("3. Extract every third character from 'PythonIsAwesome!'.")
print("4. Replace 'bad' with 'good' in 'This is a bad idea'.")
print("5. Check if 'racecar' is a palindrome using slicing.")
