import random

#loads the word list
def loadworddic(dicarray):
    f = open("words_alpha.txt", "r")
    for word in f:
        dicarray.append(word.strip())
        
#randomly picks a word from dictionary array
def pickword(dicarray):
    pick = round(random.random() * len(dictionary))
    return dicarray[pick]

#replaces a character in cesnored
def spotreplace(letter, censored, index):
    return censored[:index] + letter + censored[index+1:]
    

#save the words in an array 
dictionary = []
loadworddic(dictionary)

#pick a word from the array
word = pickword(dictionary)
word = "abcdefg"

censored = '_'*len(word)

print(word)
print(censored)

print(spotreplace("x", censored, 1))
