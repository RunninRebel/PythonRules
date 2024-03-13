#define basic class looks like this 
class MyClass:
    var = "blah"
    
    def fuction(self):
        print("This is a message inside this class")
    
#access the object this way    
myobjectx = MyClass()

#call the object
print(myobjectx.var)

#new string but same object
myobjecty = MyClass()
myobjecty.var = "seconds yuck"

print(myobjecty.var)

#access function this way
myobjectx.fuction()

# _init_() is a function that is call when your class is being you initiated. It is used for assigning values in a class 
class NumberHolder:
    def __init__(self, number):
        self.number = number
        
    def returnNumber(self):
        return self.number
    
var = NumberHolder(7)
print(var.returnNumber()) #prints 7

#create a vehicles class. With two new vehicles 
#here we define the class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00 
    #function that cretes a string of the objects 
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
        
        
#creating two random cars by initilizing the class
car1 = Vehicle()
#then assigning the values to each object
car1.name = "Fast"
car1.kind = "Corvette"
car1.color = "Red"
car1.value = 100000.00

#repeat for car two 
car2 = Vehicle()
#then assigning the values to each object
car2.name = "Starter"
car2.kind = "Celica"
car2.color = "White"
car2.value = 35000.00

print(car1.description())
print(car2.description())