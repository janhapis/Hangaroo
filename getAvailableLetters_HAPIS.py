import string
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