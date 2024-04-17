#every func in Python receives a predefined number of arguments, define like this:
def myfunction(first, second, third):
    #do something with 3 variables
    ...
    
#it's possible to declare funcs which receive a var number of arguments, using the following syntax:
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))
    
foo(1, 2, 3, 4, 5)

#can also send func arguments by keywords and order does not matter
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is %d" %(first + second + third))
        
        if options.get("number") == "first":
            return first
        
result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))


#example and exercise
#print count of additional args
def receivemultipleargs(a, b, c, *extras):
    return len(extras)

def booleanargs(a, b, c, **magicnumber):
    return magicnumber["num"] == 8


#test code
if receivemultipleargs(1,2,3,4,5,6) == 3:
    print("Nice!")
if receivemultipleargs(1,2,3,4,5,6,7,8) == 5:
    print("Wow!")
if booleanargs(1,2,3, num = 5) == False:
    print("Okay!")
if booleanargs(1,2,3, num = 8) == True:
    print("True!")