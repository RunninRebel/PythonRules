#Generators are simple functions which return an iterable set of items, one at a time, in a special way 
#*** Pay attention to indentation!
#Seems to be a random value generator
import random

def lottery():
    #return 6 numbers in range of 1 - 39
    for i in range(6):
        yield random.randint(1, 40)
        
    #returns a random int between 1 - 15    
    yield random.randint(1, 15)
    

for random_number in lottery():
    print("And the next number is... %d!" % random_number)
        


#exercise: return a fibinacci sequence
def fib():
    a, b = 1 , 1
    while 1:
        yield a
        a, b = b, a + b
        
#test code
import types
if type(fib()) == types.GeneratorType:
    print("Good, the fib function i a generator.")
    
    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break