# an exceptionis basically an error
#print(a) # a is not defined so this will throw an exception

#you want to iterate through a list of items but the user needs to iput that list. If you want ten items but the user only sets 5, you want the unentered values set to zero
def count_the_number(n):
    print(n)
    
def catch_this():
    the_list = (1, 2, 3, 4, 5)
    
    for i in range(10):
        try:
            count_the_number(the_list[i])
        except IndexError: #Raised when accessing a non existing index 
            count_the_number(0)
            
catch_this()

#More exception handling in docs
# https://docs.python.org/3/tutorial/errors.html#handling-exceptions

#print out the last name in the exception
actor = {"name": "Kelsey Sellmann", "rank": "Alpha Predator"}

#function 
def get_rank():
    return actor["rank"].split()[0]        
    #return actor["rank"].split()[1]
    
def get_lastname():
    return actor["name"].split()[1]
    #return actor["rank"].split()[0]



#test code
get_rank()
get_lastname()
print("All exceptions caught! Good Job")
print("The actor's rank is %s" % get_rank())
print("The actor's last name is %s" % get_lastname())

