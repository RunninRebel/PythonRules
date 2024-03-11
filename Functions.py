#Writing functions 
#block_head:
#  1st block line
#  2nd block line
#  ....
#examples
def my_function():
    print("Hello from my first function!")
    
def my_function_with_args(username, greetings):
    print("Hello, %s. From My Function! Hope you %s" % (username, greetings))

    
#returning values
def sum_two_numbers(a, b):
    return a + b


#How to call functions. Write the functions name, followed by () and any arguments required inside the parenthesis 
my_function()

my_function_with_args("Kelsey Sellmann", "have a great day!")

x = sum_two_numbers(4,3)
print(x)


def list_benefits():
    return["More organized code", "More readable code", "Easier code to use", "Allowing programmers to share and connect code together"]

def build_sentence(benefit):
    return "%s, is a benefit of functions!" % benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
        
name_the_benefits_of_functions()