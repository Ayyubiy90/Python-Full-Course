# Rules for Naming a Variable

# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (age, Age, and AGE are three different variables)

my_name = input ("my_name is? ")
your_age = input ("your_age is? ")
your_address = input ("your_address is? ")

print("Your name is:", my_name)
print("Your age is:", your_age)
print("Your address is:", your_address)

# Multiple variable in one line 
x,y,z = "I love python", "I love programming", "I love coding"

print(x)
print(y)
print(z)

# Assigning multiple value to variable 
x = y = z = "I love python"

print(x)
print(y)
print(z)