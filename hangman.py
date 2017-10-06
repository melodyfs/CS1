import random

letters_guessed = []
secret_word = []
secretWord = ""
attempt = 5


def loadWord():
   f = open('hangman_words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   global secretWord
   secretWord = random.choice(wordsList)
   return secretWord

# def wordToGameMode(secretWord):
#     global number_of_underscore
#
#     for i in range(len(secretWord)):
#         number_of_underscore += "_"
#     return number_of_underscore

def splitWord():
    secret_word = list(secretWord)


def isWordGuessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    global attempt

    if secret_word == letters_guessed:
        print("You win!")
        return True
    elif checkLetters is False:
        attempt -= 1
        if attempt > 0:
            hangman(secretWord)
        else:
            print("You lost! The word is %s" % secretWord )
        return False


def checkLetters():

    game_word = []

    if letters_guessed in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == letters_guessed:
                game_word = ''.join(game_word)
                print("%s" % game_word)
                return True
    else:
        print("Try again!")
        return False

def getGuessedWord():
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.

    '''
    splitWord()
    print("Number of the word: %s" % len(secretWord))


    # if letters_guessed != []:
    #     print("You have picked %s" % letters_guessed)
    #     print("Choose other letter")

    lettersGuessed = input("Guess a letter: ")

    if len(lettersGuessed) > 1 :
        print("Enter one letter at a time")
        getGuessedWord()
    else:
        if lettersGuessed in letters_guessed:
            print("You have picked %s" % lettersGuessed)
            print("Choose other letter")
            getGuessedWord()
        else:
            letters_guessed.append(lettersGuessed)
            return lettersGuessed


def hangman(secretWord):
    getGuessedWord()
    guessed_letter = getGuessedWord()
    check_result = checkLetters()
    isWordGuessed(check_result, guessed_letter)


secretWord = loadWord()
hangman(secretWord)
