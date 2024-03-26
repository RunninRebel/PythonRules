#Create new lists based on other lists 
# sentence = "The quick brown fox jumps over the lazy doggo"
# words = sentence.split()
# word_lengths = []
# for word in words:
#     if word != "The":
#         word_lengths.append(len(word))

# print(words)
# print(word_lengths)


# #using list comprehension we can simplify the notation
# new_sentence = "There are no new creatures in the forest to play with"
# new_words = new_sentence.split()
# new_word_lengths = [len(word) for word in new_words if word != "the"]

# print(new_words)
# print(new_word_lengths)


# #Excercise create a new list with only positive numbers as integers
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
# new_numbers = numbers.sort()
# newlist = []
# for number in numbers:
#     if number > 0:
#         newlist.insert(0, int(number))
        
# print(numbers)
# print(newlist)


#using comprehensive lists print only positive and sort before printing 
random_numbers = [34.6, -203.4, 44.9, -68.3, -12.2, -44.6, 12.7, -65.3]
new_number_list = [int(x) for x in random_numbers if x > 0]

new_number_list.sort()
print(new_number_list)