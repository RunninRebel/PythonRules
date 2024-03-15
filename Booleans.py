#Working on how Booleans work
name = "Kels"
age = 34

if name == "Kels" and age == 34:
    print("Your name is %s, and your are is %d" % (name, age))


if name == "Rick" or name == "Kels":
    print("Hello")
    
if name in ["Chef", "Kels"]:
    print("Your name is either Chef or Kels")
    

statement = False
another_statement = True
if statement is True:
    pass
elif another_statement is True:
    pass
else:
    pass

#the "is" operator does not match the values of the variables,
#but the instance themselves
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)

t = "T"
r = "T"
print(t is r)

#use "not" instead of "!"
print(not False)
print(not False) == (False)

number = 18
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("6")

if first_array:
    print("5")
    
if len(second_array) == 2:
    print("4")
    
if len(first_array) + len(second_array) == 5:
    print("3")

if first_array and second_array[0] == 1:
    print("2")
    
if not second_number:
    print("1")