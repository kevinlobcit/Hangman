import random
import hangmanascii

#word dictionary from https://github.com/Xethron/Hangman/blob/master/words.txt
#hangman ascii art from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c

#loads the word list
def loadworddic(dicarray):
    f = open("words.txt", "r")
    for word in f:
        dicarray.append(word.strip())
        
#randomly picks a word from dictionary array
def pickword(dicarray):
    pick = round(random.random() * len(dicarray))
    return dicarray[pick]

#replaces a character in cesnored
def spotreplace(letter, censored, index):
    return censored[:index] + letter + censored[index+1:]
    
def search(letter, word):
    #print("searching")
    positions = []
    for i in range(len(word)):
        if(word[i] == letter):
            #print("match at ", i)
            positions.append(i)
    return positions

#finds the position for letters in the word and replaces it in censored
#returns the new censored and the positions of the replaced
def checkreplace(letter, word, censored):
    positions = search(letter, word)
    for i in range(len(positions)):
        censored = spotreplace(letter, censored, positions[i])
        #print(censored)
    return censored,positions

#gets user input for letter
def getletter():
    gotLetter = False
    while(True):
        letter = input("Enter a Letter: ")
        if(len(letter) != 1):
            print("Invalid input")
        if(letter.isdigit()):
            print("Is a number")
        else:
            return letter

def userloop():
    #save the words in an array 
    dictionary = []
    loadworddic(dictionary)
    tries = 0

    #pick a word from the array
    word = pickword(dictionary)
    #create censored word
    censored = '_'*len(word)

    print("Current progress: " + censored)
    print(hangmanascii.HANGMANPICS[tries])
    while(word != censored):
        letter = getletter()
        censored, positions = checkreplace(letter, word, censored)
        
        #if no matches +1 on tries
        if(len(positions) == 0):
            tries += 1
            
        print("Current progress: " + censored)
        print(hangmanascii.HANGMANPICS[tries])

userloop()
