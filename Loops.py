#Learning and testing loops
primes = [1,2,3,4]
for prime in primes:
    print(prime)
    
    
#range
#prints out a new list range from 0-5
for x in range(5):
    print(x)
    
#prints out an iterator of that range
for x in range(3,6):
    print(x)
    

for x in range(3, 8, 2):
    print(x)


#while loops, loop will continue until count is greater than 5
count = 0
while count < 5:
    print(count)
    count+= 1
    
count = 0
while True: 
    print(count)
    count += 1
    if count >= 5:
        break
    
    
#prints out odd numbers 
for x in range(10):
    #check if x is even 
    if (x % 2 == 0):
        continue
    print(x)    


#else clause in loops. It does not executes if there's break in the loop
for i in range(1,10):
    if(i % 5 == 0):
        break
    print(i)
else: 
    print("This will never print because there's a BREAK in the loop")