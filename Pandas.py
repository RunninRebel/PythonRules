#Panda's a high level data manipulation tool. Built on the Numpy packages and key data structure call DataFrame. DataFrames allow you to store and manipulate tabular data

#several ways to create DataFrames. One way is to use dictionaries
dict = {"Country": ["Brazil", "Russia", "India", "China", "North Korea"],
        "Capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pyongyang"], 
        "Area": [8.516, 17.10, 3.286, 9.597, 1.221], 
        "Population": [200.4, 143.5, 1252, 1357, 24.2]}

#import pandas and use it as pd
import pandas as pd
brics = pd.DataFrame(dict)
#print(brics)

#you can set a different index value, you can set it this way
brics.index = ["BR", "RU", "IN", "CH", "NK"]

#print(brics)

#you can also create DataFrames by importing cvs files
people = pd.read_csv('/home/jc/Documents/Python/PythonRules/people.csv', index_col= 0)

#print(people)

#Different ways of indexing DataFrames. Simplest way is to use brackets but using two brackets  will output Pandas DataFrame

#print out job title column as Panda Series
#print(people['Job Title'])

#print out job title as Panda DataFrame
#print(people[['Job Title']])

#print out DataFrame with Lastname and Sex
#print(people[['Last Name', 'Sex']])

#square brackets can also be used to access observations
#prints out the first four observations
#print(people[0:4])

#print out fifth and sixth observation
#print(people[4:6])

#you can also use 'loc' and 'iloc' to perform about any data selection operation. 'loc' is label-based, which means that you have to specify rows and columns based on their rows and columns. 'iloc'is interger based, you have to specify rows and columns by their integer index 
print(people.iloc[2]) 


#This one does not work, need to read up on printing observations
#print(people.loc[['Shelby', 'Phillip']])
