#code introspection is the ability to examine classes, funcs and keywords to know what they are, what they do and what they know

#python provides several funcs and utilities for code introspection
help()
dir()
hasattr()
id()
type()
repr()
callable()
issubclass()
isinstance()
__doc__
__name__

#use the help func to see what each func does
#delete this when done
help(dir)
help(hasattr)
help(id)

#define the vehicle class
class Vehicle:
    name =""
    