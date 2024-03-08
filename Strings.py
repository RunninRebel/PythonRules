#Argument Specifiers
# %s - String (or any object with a string representation, like numbers)

# %d - Integers

# %f - Floating point numbers

# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

# %x/%X - Integers in hex representation (lowercase/uppercase)
#hard coded variables
myString = "Hello"
myFloat = float(34)
myInt = 12

#testing code
if myString == "Hello":
    print("This String = %s" %myString)
if isinstance(myFloat, float) and myFloat == float(34):
    print("The Current Float = %f" %myFloat)
if isinstance(myInt, int) and myInt == 12:
    print("The Integer is = %d" %myInt)
    
    
#using Tuples
name = "Juan"
age = 28
print("%s is %d years old" % (name, age))

#reformat the string to print out data
data = ("Kels", "Sells", 53.55)
format_string = "Hello %s %s. Your current balance is $%f"

print(format_string % data)