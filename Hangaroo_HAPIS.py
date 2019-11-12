import random
import string
import time

words = ['apple', 'orange', 'mango', 'cherry']
secretWord = random.choice(words)
lettersGuessed = []

def isWordGuessed(secretWord, lettersGuessed):
    update = 0
    for i, character in enumerate(secretWord):
    	if character in lettersGuessed:
    		update += 1
    if update == len(secretWord):
    	return True
    else:
    	return False

def getGuessedWord(secretWord, lettersGuessed):
    update = 0
    underScore = ['_'] * len(secretWord)

    for i, character in enumerate(secretWord):
        if character in lettersGuessed:
            update += 1
            underScore.insert(update-1,character)
            underScore.pop(update)
            if update == len(secretWord):
                return ''.join(str(w) for w in underScore)
        else:
            update += 1
            underScore.insert(update-1,'_')
            underScore.pop(update)
            if update == len(secretWord):
                return ''.join(str(w) for w in underScore)
        
def getAvailableLetters(lettersGuessed):
    availableLetters = list(string.ascii_lowercase)
    availableLetters2 = availableLetters[:]

    def removeLetters(L, l):
        LetterStart = L[:]
        for w in L:
            if w in LetterStart:
                l.remove(w)
        return ''.join(str(w) for w in l)

    return removeLetters(lettersGuessed, availableLetters2)

def Hangaroo(secretWord):
    begin = (len(secretWord))
    guess = str
    mistakesMade = 4
    wordGuessed = False
    
    print ('Welcome to Hanagaroo!')
    while True:
        n = input("What is your Name? ").strip()
        if n == '':
            print("Invalid Input")
        else: break
    print("Hello, " + n, "let's play Hangaroo!!!")
    time.sleep(1)
    print ('There are ', begin, ' letters you will need to guess.')
    time.sleep(0.5)
    print("Start guessing...")

    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print (('You have ') + str(mistakesMade) + (' more guesses.'))
        print (('Letters left: ') + getAvailableLetters(lettersGuessed))
        guess = input('Guess a letter: \n').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print (("You've already guessed the letter!!! Mr. Kangaroo is mad ") + getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guess)
                print (("You've guessed a letter!!! That's a relief ") + getGuessedWord(secretWord, lettersGuessed))
        else:
            if guess in lettersGuessed:
                print (("You've already guessed the letter!!! Mr. Kangaroo is mad ") + getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print (('Wrong letter!!! Poor Mr. Kangaroo ') + getGuessedWord(secretWord, lettersGuessed))

    if wordGuessed == True:
        print('CONGRATULATIONS, you won!')
    elif mistakesMade == 0:
        print ('GAME OVER!!! The secret word was: ' + secretWord)
        
Hangaroo(secretWord)