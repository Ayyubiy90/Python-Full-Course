x = 2
y = "copyassignment.com"
z = ["list", 1]

print(type(x))
print(type(y))
print(type(z))


var1 = 20.3
var2 = int(var1)    # to int type
var3 = complex(var1)    # to complex type
var4 = str(var1)    # to str type

print(var1, "Type is", type(var1))
print(var2, "Type is", type(var2))
print(var3, "Type is", type(var3))
print(var4, "Type is", type(var4))

# Note;
# Integer = value in decimal point 
# Float = value in whole number

# Integer to float
x = 10
y = float(x)
print(y)

# Float to integer
x = 3.5
y = int(x)
print(y)

# String to integer or float
x = "25"
y = int(x)
z = float(x)
print(y)
print(z)

# Integer to string 
x = 42
y = str(x)
print(y)

# Numeric Data-types
x = 12
y = 12.3
z = 12j  # we use "j" to represant complex numbers
print(type(x))
print(type(y))
print(type(z))

# Int
x = 1227348742474
y = -12234353546
z = 0
print(type(x))
print(type(y))
print(type(z))

# Float
x = 122734.8742474
y = -12234.353546
z = 0.2032
print(type(x))
print(type(y))
print(type(z))

# Complex
x = 12 + 3j
y = -12 - 0.4j # we use "j" to represant complex numbers
z = 4j
print(type(x))
print(type(y))
print(type(z))