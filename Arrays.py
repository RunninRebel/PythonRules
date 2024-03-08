#Lists
myList = []
myList.append(1)
myList.append(2)
myList.append(3)

print("Printing array zero: %a" %myList[0]) #prints 1
print("Printing array zero: %a" %myList[1])
print("Printing array zero: %a" %myList[2])

# loop that prints out 1,2,3
for x in myList:
    print(x)
    

#joing lists
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers

print("Prints Joined List: %a" %all_numbers)
print("Prints Sorted List: %a" %sorted(all_numbers))

#supports repeating lists
print([1,2,3] * 3)
print(sorted([1,2,3] * 3))

#create two lists w/ 10 repeating objects and concat the two lists into one
x = object()
y = object()

list_x = [x] * 10
list_y = [y] * 10
big_list = list_x + list_y
print("big_list constains %d objects" % len(big_list))