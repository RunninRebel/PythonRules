#Serialization : to encode and decode JSON
import json


#there are 2 formats for JSON data, in a string or object datastructure. In DS, consists of lists and dictionaries nested inside each other/ DS allows python methods to add, list, search, and remove elements from the DS. The string format is main used to pass data into another program or load into a DS

#print(json.loads(json_string))

json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)


#you can use deserialization method call pickle
import pickle
pickled_string = pickle.dumps(["From Pickle", 1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))


#print out JSON string with added key-value pair "Me" : 800
#the code
#func that adds given name and salary pair to json
def add_employee(salaries_json, name, salary):
    #add key-value pair 
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    return json.dumps(salaries)


# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])