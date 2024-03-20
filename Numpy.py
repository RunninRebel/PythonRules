#Learning to use Numpy Arrays
#creating two new lists 
height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 92.25, 92.98, 86.18, 88.45]

import numpy as np

#creating 2 numpy arrays from previously created lists
np_height = np.array(height)
np_weight = np.array(weight)

print(np_height)

#element wise calculations are what numpy are best known for. 
#calculate bmi
bmi = np_weight / np_height ** 2

#print result
print(bmi)

#using subsets from boolean logic
bmi > 27
print(bmi > 27)

#to observations 
bmi[bmi > 25]
print(bmi[bmi > 25])

#exercise: convert kg to lbs
#create kg array 
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

#create numpy array from weight_kg
np_weight_kg = np.array(weight_kg)

# Create np_weight_lbs from np_weight_kg
pound = 2.205
np_weight_lbs = np_weight_kg * pound

#print out lbs
print("converted %dkg to %dlbs" % (np_weight_kg, np_weight_lbs))