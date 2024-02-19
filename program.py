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
    
def search(letter, word):
    print("searching")
    positions = []
    for i in range(len(word)):
        if(word[i] == letter):
            print("match at ", i)
            positions.append(i)
    return positions

def checkreplace(letter, word, censored):
    positions = search(letter, word)
    for i in range(len(positions)):
        censored = spotreplace(letter, censored, positions[i])
        print(censored)

#save the words in an array 
dictionary = []
loadworddic(dictionary)

#pick a word from the array
word = pickword(dictionary)
word = "abcadefga"

#create censored word
censored = '_'*len(word)

print(word)
print(censored)
print(spotreplace("x", censored, 1))

letter = "a"
checkreplace(letter, word, censored)
#positions = search(letter, word)
#for i in range(len(positions)):
#    censored = spotreplace(letter, censored, positions[i])
#    print(censored)