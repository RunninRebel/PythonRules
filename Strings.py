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


astring = "Hello World!"
print(len(astring)) # 12
print(astring.index("o")) #4
print(astring.count("l")) # 3
print(astring[3:7]) #lo w  
print(astring[3:7:2]) #l
print(astring[-3]) #3rd char from end = l
print(astring[::-1]) #reverse a string 
print(astring.upper())
print(astring.lower())
print(astring.startswith("Hell"))
print(astring.endswith("lol"))
print(astring.split(" "));

s = "Strings are Awesome!"
print("Length of s = %d" % len(s))
print("The first occurence of the letter a = %d" % s.index("a"))
print("a occurs %d" % s.count("a"))
print("The first five characters are '%s'" % s[:5])
print("The next five charaters are '%s'" % s[5:10])
print("The thirteenth character is '%s'" % s[12])
print("The charaters with odd index are '%s'" % s[1::2])
print("The last five charaters are '%s'" % s[-5:])

if s.startswith("Str"):
    print("String starts with 'Str'. Great!")

if s.endswith("ome!"):
    print("String ends with 'ome!. Great!")

print("Split the words of the string: %s" % s.split(" "))
