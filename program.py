import random

#loads the word list
def loadworddic(dicarray):
    f = open("words_alpha.txt", "r")
    for word in f:
        dicarray.append(word.strip())

#save the words in an array 
dictionary = []
loadworddic(dictionary)

#pick a word from the array
pick = round(random.random() * len(dictionary))
#print(dictionary)

print(pick) 
