import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    
    return random.choice(wordlist)



def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
    	if i not in lettersGuessed:
    		return False
    return True
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    secretWord1=""
    
    for i in secretWord:
    	if i in lettersGuessed:
    		secretWord1+=' '
    		secretWord1+=i
    		continue
    	secretWord1+=' _ '
    return secretWord1
    



def getAvailableLetters(lettersGuessed):
	string=""
	
	for i in range (97,123):

		if chr(i) in lettersGuessed:
			continue
		string+=chr(i)
	return string
	
    
    
    

def hangman(secretWord):

    print "\nWelcome to game, Hangman !\n"
    done=False
    lg=list()
    word=list()
    attempt=0
    exist=True

    print "I am thinking of a word that is ",len(secretWord),"letters long.\n"
    for letter in secretWord:
    		word.append(letter)
    while attempt<=7:
    	'''print "-------------"
    	print "\nYou have ",(8-attempt)," guesses left."
    	print "Available Letters :",getAvailableLetters(lg)'''
    	
    	while exist:
    		print "-------------"
    		print "\nYou have ",(8-attempt)," guesses left."
    		print "Available Letters :",getAvailableLetters(lg)
    		a=raw_input("Please guess a letter :")
    		if a not in lg:
    			break
    		print "Oops! You've already guessed that letter: ",getGuessedWord(secretWord,lg)

    			
    		

    	lg.append(a)
    	st=getGuessedWord(secretWord,lg)
    	if a in secretWord:
    		print "Good guess: ",st
    	else:
    		print "Oops! That letter is not in my word: ",st
    		attempt+=1
    	
    	done=isWordGuessed(secretWord,lg)
    	
    	if done:
    		print "Congratulations, you won!"
    		return 0
    print "Sorry, you ran out of guesses. The word was ",secretWord
    return 1

    
    # FILL IN YOUR CODE HERE...

wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
#secretWord="apple"
hangman(secretWord)










