#sets are lists with no duplicate entries
print(set("My name is Juan and Juan is my name".split()))

#sets are powerful tool that can calculate differences and intersections between other sets
a = set(["Kelsey", "Jones", "Dinah"])
print(a)
b = set(["Jones", "Jill"])
print(b)

#use intersection to find out which member is in the event
print(a.intersection(b))
print(b.intersection(a))

#use symmetric_difference to find out which member attended one event
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

#use differnce to see who attended only one event
print(a.difference(b))
print(b.difference(a))

#to get a list from all participants use union 
print(a.union(b))


#create a set and print it out from the list given

#list
a = ["Circle", "Square", "Triangle"]
b = ["Square", "Oval"]

#create set
x = set(a)
y = set(b)

#print out patterns that do not appear in B from A
print(x.difference(y))