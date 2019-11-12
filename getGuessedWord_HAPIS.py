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