#A closures is a function object that remembers values in enclosing scopes even if they are not present in memory 

#A nested function is function defined within another function. Important to note that the nested funcs can access the variables of the enclosing scope. However, they are readonly. One can use the nonlocal keyword explicitlywith these varaibles in order to modify them 
def transmit_to_space(message):
    "This is the enclosing function"
    def data_transmitter():
        "The nested function"
        print(message)
        
    data_transmitter()
print(transmit_to_space("Test message"))

func2 = transmit_to_space("Burn the Sun!")
func2()

# def print_msg(number):
#     def printer():
#         "Here we are using the nonlocal keyword"
#         nonlocal number
#         number = 3
#         print(number)
#     printer()
#     print(number)
    
# print(print_msg(9))


