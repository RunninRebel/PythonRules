#using lambdas
#typical way to create a def and call it later in the code
def sum (a, b):
    return a + b

a, b = 3, 5
c = sum(a, b)
print(c)


#instead we can use lambdas
#they can be called inline and do not need names so they are called anonymous functions
#Created as such 
your_function_lambda = lambda inputs : output

x, y = 3, 5
sum = lambda a, b : a + b
z = sum(x, y)
print(z)


#excersice check if the give list is odd. Print 'true' or 'false' as you check each element
l = [2, 4, 7, 3, 15, 22]
for i in l:
    odd = lambda i : (i % 2) == 1
    print(odd(i))