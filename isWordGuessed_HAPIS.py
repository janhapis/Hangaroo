def isWordGuessed(secretWord, lettersGuessed):
    update = 0
    for i, character in enumerate(secretWord):
    	if character in lettersGuessed:
    		update += 1
    if update == len(secretWord):
    	return True
    else:
    	return False