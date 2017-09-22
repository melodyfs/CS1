import random

attempt = 8
number_of_underscore = 0
letters_guessed = []
secret_word = []


def loadWord():
   f = open('hangman_words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = random.choice(wordsList)
   return secretWord

def wordToGameMode(secretWord):
    global number_of_underscore

    for i in range(len(secretWord)):
        number_of_underscore += "_"

    return number_of_underscore

def splitWord(secretWord, lettersGuessed):
    global letters_guessed
    letters_guessed = list(lettersGuessed)
    global secret_word
    secret_word = list(secretWord)


def isWordGuessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    if secret_word == letters_guessed:
        print("You win!")
        return True
    else:
        print("You lost!")
        return False


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    lettersGuessed = input("Guess a letter: ")

    splitWord(secretWord, lettersGuessed)

    if len(lettersGuessed) > 1 :
        print("Enter one letter at a time")
        getGuessedWord(secretWord,lettersGuessed)

    else:
        for i in range(len(secretWord)):
            for j in range(len(lettersGuessed)):
                if secretWord[i] == lettersGuessed[j]:
                    secretWord[i] = secretWord
                print(secretWord[i])



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    if lettersGuessed != []:
        print("You have picked %s" % lettersGuessed)
        print("Choose other letter")
        getGuessedWord(secretWord, lettersGuessed)
    else:
        letters_guessed.append(lettersGuessed)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...

    loadWord()
    print("Number of the word: %s" % len(secretWord))
    getGuessedWord(secretWord, letters_guessed)
    isWordGuessed(secretWord, letters_guessed)
    getAvailableLetters(letters_guessed)


secretWord = loadWord()
hangman(loadWord())
