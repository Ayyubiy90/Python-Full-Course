# Printing a string 

print("My name is Abdullah")
print('I`m AYB, currently learning python') # back-tik is used for a statement when shortining word, that's when you use single string for a statement
# Note: single string or double string can be used in python

# Assigning string to variable
a = "Hello"
b = """This is
a multiline 
string"""

text = "Hello, World!"

# Extract the substring "Hello"
hello = text[0:5]  # or simply text[:5]

# Extract the substring "World"
world = text[7:12]  # or simply text[7:]

# Extract every second character from the string
every_second_char = text[::2]  # This will give you "Hlo ol!"

text = "Hello, World!"

# Extracting a substring from index 0 to index 5 (excluding index 5)
substring = text[0:5]
print(substring)  # Output: Hello

text = "Hello, World!"

# Extracting a substring from index 7 to the end of the string
substring = text[7:]
print(substring)  # Output: World!

# Extracting a substring from the beginning of the string to index 5 (excluding index 5)
substring = text[:5]
print(substring)  # Output: Hello

text = "Python"

substring = text[1:4]

text = "Python"

# Extract the substring "Pto"
substring = text[0:5:2]

# String slicing
mystr = "I am a string"
print(len(mystr))  # 13
print(mystr[0])  # 'I'
print(mystr[1])  # ' '  blank space
print(mystr[0:len(mystr)])  # full string
print(mystr[:])  # here python automatically assigns 0 and
                 # value of length of string
print(mystr[-2:-1])  # 'n'
print(mystr[-14:-1])  # full string excluding 'g'
print(mystr[:100])  # full string (no errors)

x = "2"
y = "4"
print("12.3" + "34.6")  # string concatenation
print(x + y)  # string concatenation
print(int(x) + int(y))  # simple addition

# Comma in print() statement
name = "John"
age = 25
print("My name is", name, "and I am", age, "years old.")

print("This name is", "Harry")
print("My roll number is", 21)

# “end” inside print() statement

print("Hello, ", end="")
print("World!")
# output: Hello, World!

# format() method

name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)

# Fast String

name = "Harry"
age = 30
print(f"Name:{name} and age:{age}")
print(f"Addition:{5+4}")
print(f"Multiplication:{eval('1+2//4-20*9')}")
''' eval() is a built-in function
    used to calculate a string 
    which contains some arithematic
    calculations of numbers'''
    
# lower() method
mystring = "I Am A String"
print(mystring.lower())     # this method will return the string having all letters in lowercase

# upper() method
mystring = "I Am A String"
print(mystring.upper())     # then this method will return the string with all letters to uppercase.

# replace() method
mystring = "I Am A String"
print(mystring.replace("I", "This"))    # This method is used to replace a string or letters with another string.

# Escape Characters

# '\': Single quote character.
# "\": Double quote character.
# \\: Backslash character.
# \n: Newline character. Inserts a line break.
# \t: Tab character. Inserts a horizontal tab.
# \r: Carriage return. Moves the cursor to the beginning of the line.
# \b: Backspace. Deletes the previous character.
# \f: Form feed. Advances to the next line and starts at the leftmost position.
# \v: Vertical tab. Inserts a vertical tab.

print("This is a string with a single quote: \'Hello, world!\'")
print("This is a string with a double quote: \"Hello, world!\"")
print("This is a string with a backslash: \\path\\to\\file")
print("This is a string with a newline:\nHello\nWorld")
print("This is a string with a tab:\tColumn 1\tColumn 2")

print("I am \"a\" String")
print("Printing in \nNew Line")
print("Printing with a \ttab space")
print("Printing a single quote\'")
