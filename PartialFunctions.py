#can create partial functions by using partial functool
#partial funcs allow one to derive a func with x parameters to a func with fewer parameters and fixed values set for the more limited func
from functools import partial

#this code will return 8
def multiply(x,y):
    return x * y
    
#create a new func that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))

#note: the default values will start replacing variables from the left. The 2 replaces x. Y will equal 4 when dbl(4) us called. It does not make a difference in this example but it does in the example below

#edit the func below, call partial and replace the first 3 variables. Then print with the new func using only on input var so that the out put is 60
def func(u, v, w, x):
    return u*4 + v*3 + w*2 + x

increment = partial(func, 5, 6, 7)
print(increment(8))