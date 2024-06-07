#decorators allow you to modify a fun, method, or class
#Syntax
# @decorator
# def function(arg):
#     return "value"

# #is equivalent to 
# def funtion(arg):
#     return "Value"
# function = decorator(function) # this passes the function to the decorator, and reassigns it to the functions

#Another example
def repeater(old_func):
    def new_func(*args, **kwds): # See learnpython.org/en/Multiple%20Function%20Arguments for how *args and **kwds works
        old_func(*args, **kwds) # we run the old function
        old_func(*args, **kwds) # we do it twice
    return new_func # we have to return the new_function, or it wouldn't reassign it to the value

#this owuld make the func repeat twice
@repeater
def multiply(num1, num2):
    print(num1 * num2)
    
#can also change the output 
def double_out(old_func):
    def new_func(*args, **kwds):
        return 2 * old_func(*args, **kwds) #mofily the return value
    
    
    
#change input
def double_Input(old_func):
    def new_func(arg): #only works if the old func has one argument
        return old_func(arg * 2) #modify the argpassed
    return new_func

#checking
def check(old_func):
    def new_func(arg):
        if arg < 0: (ValueError, "Negative Argument") #his causes an error, which is better than it doing the wrong thing
        old_func(arg)
    return new_func

#to multiply the output by a specific amount you'd do 
def multiply(multiplier):
    def multiply_generator(old_func):
        def new_func(*args, **kwds):
            return multiplier * old_func(*args, **kwds)
        return new_func
    return multiply_generator #returns the new generator

#usage
@multiply(3) #multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

#now return_num is decorated and reassigned into itself
return_num(5) # should retunr 15


#create a func to check if the phrase is correct, if not then prompt error
def type_check(correct_type):
    def type_checker(old_func):
        def new_func(arg):
            if(isinstance(arg, correct_type)):
                return old_func(arg)
            else:
                print("Bad type")
        return new_func
    return type_checker

@type_check(int)
def times2(num):
    return num * 2

print(times2(4))
times2('Not A Number')

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter("Draco"))
first_letter(['Not', 'A', 'Sring'])

@type_check(str)
def Third_letter(word):
    return word[2]

print(Third_letter("Spring"))
first_letter(['Not', 'A', 'Sring'])