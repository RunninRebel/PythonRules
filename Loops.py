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
for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else: 
    print("This will never print because there's a BREAK in the loop")
    
    
#print all the even numbers in the lis in order the appear
#If you hit the number 237 stop printing and exit the loop
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if(number % 2 == 0):
        print(number)
    if(number == 237):
        break