import json #importing library to get a better output of dictionary items

#use dictionaries to initialize and store lists
phonebook = {}
phonebook["Kels"] = 8675309
phonebook["Jason"] = 8675308
phonebook["Susie"] = 8675307

print(json.dumps(phonebook, indent = 3))

#you can also initilize it this way 
phonebook1 = {
    "Maria" : 4958334,
    "Julio" : 5684953,
    "Ella" : 4859634
}

print(json.dumps(phonebook1, indent = 3))

#Iterating over dictionaries
for name, number in phonebook1.items():
    print("Phone number of %s is %d" % (name, number))
    

#deleting at a specified index. Two Methods
#1 index
del phonebook1["Ella"]
print(json.dumps(phonebook1, indent = 3))

#2 pop method
phonebook1.pop("Maria")
print(json.dumps(phonebook1, indent = 3))


#Add a new member name and nuber to the dictionary and remove then remove one member from the dict
phonenumbers = {
    "Tim" : 3458676,
    "Erin" : 3458694,
    "Chris" : 3458654
}

phonenumbers["Sue"] = 3458639
phonenumbers.pop("Tim")

#Testing code
if "Sue" in phonenumbers:
    print("Sue is listed in the phonebook.")
    
if "Tim" not in phonenumbers:
    print("Tim is not listed in the phonebook")