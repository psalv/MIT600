__author__ = 'paulsalvatore57'


### 4 HANGMAN WONRDGAME



### HELPER CODE, DON'T NEED TO UNDERSTAND

import random
import string

WORDLIST_FILENAME = "Assignment 3 words.txt"

def load_words():
    """Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish."""
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """wordlist (list): list of words (strings)
    Returns a word from wordlist at random"""
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program

wordlist = load_words()

# your code begins here!


def checkguess(guess):
    """Returns true if the given string is present in a tuple.
    input: string one character long
    output: True if present, false if it is not"""
    length = 0
    while length < len(question):
        if guess == str(question[length]):
            return True
        else:
            length += 1
    return False


def remaining(word):
    """Returns a list with altered elements to reflect correctly guessed letters
    input: string one character long
    output: list with the character appropriately inserted"""
    length = 0
    while length < len(question):
        if guess == str(question[length]):
            guessedcorrect[length] = word
            length += 1
        else:
            length += 1
    return guessedcorrect


def cnter(word):
    """Returns the number the given letter appears in the unknown word
    input: string one character long
    output: int of how many times the character appears in the word"""
    length = 0
    number = 0
    while length < len(question):
        if guess == str(question[length]):
            length += 1
            number += 1
        else:
            length += 1
    return float(number)


def checkletter(guess):
    """Returns true if the character chosen is in the english alphabet
    input: string
    output: True if the string is one letter in the english alphabet"""
    for i in xrange(len(letters)):
        if guess == letters[i]:
            return True
    return False


def checkdouble(guess):
    """Returns true if the guessed letter has not already been guessed
    input: string
    output: True if the string is not in the list guessedletters"""
    if len(guessedletters) == 0:
        return True
    length = 0
    while length <= len(guessedletters):
        if guess == guessedletters[length - 1]:
            return False
        length += 1
    return True


question = choose_word(wordlist)
# print question

print "----------"
print "Hello welcome to hangman!"
print "Your word is", len(question), "letters long."
print "----------"
nguesses = int(raw_input('How many guesses would you like to play with (recommended 6)?'))        #this will determine when the games ends
print "----------"
letters = ('abcdefghijklmnopqrstuvwxyz')
counter = 0.0                                                                     #this will be the win condition, to get this to the number of letters
guessedcorrect = []                                                               #sets the blanks
for i in xrange(len(question)):
        guessedcorrect = guessedcorrect + ['_',]
guessedletters = []
while counter < len(question) and nguesses > 0:
    print "You have", nguesses, "guess(es) remaining."
    print "You have already guessed:", guessedletters
    guess = (raw_input('Guess a letter:')).lower()
    if checkletter(guess) is True and checkdouble(guess) is True:
        guessedletters = guessedletters + [guess,]
        if checkguess(guess) is True:
            counter += cnter(guess)
            if counter < len(question):
                print "Correct"
                print "Current progress:", remaining(guess)
                print "----------"
            else:
                break
        else:
            nguesses -= 1
            print "Nope."
            print "Current progress:", remaining(guess)
            print "----------"
    else:
        print "Invalid input."
        print "----------"
if counter == len(question):
    print "You're a bitch, the word was", question
else:
    print "You have lost, you're a big bitch. The word was", question, "."


















### HIS SOLUTION:

#He extensively used the for..in and if...in commands which eased checking the different elements of the lists he created
#I had forgotten that thes exist and had to work around it by implementing unnecessary functions

# def partial_word(secret_word, guessed_letters):
#     """
#     Return the secret_word in user-visible format, with underscores used
#     to replace characters that have not yet been guessed.
#     """
#     result = ''                             #scan correct letters and places either them, or a _ to form the partial word
#     for letter in secret_word:
#         if letter in guessed_letters:
#             result = result + letter
#         else:
#             result = result + '_'
#     return result
#
# def hangman():
#     """
#     Runs the hangman game.
#     """
#     print 'Welcome to the game, Hangman!'
#     secret_word = choose_word(wordlist)
#     print 'I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.'
#     num_guesses = 8
#     word_guessed = False
#     guessed_letters = ''
#     available_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
#                          'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
#                          's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     # Letter-guessing loop. Ask the user to guess a letter and respond to the
#     # user based on whether the word has yet been correctly guessed.
#     while num_guesses > 0 and not word_guessed:                 #his win condition was a switch crom the word_guessed variable (don't need to track doubles this way)
#         print '-------------'
#         print 'You have ' + str(num_guesses) + ' guesses left.'
#         print 'Available letters: ' + ''.join(available_letters)
#         guess = raw_input('Please guess a letter:')
#         if guess not in available_letters:                      #took away elements from a list to track which had been guessed
#             print 'Oops! You\'ve already guessed that letter: ' + partial_word(secret_word, guessed_letters)
#         elif guess not in secret_word:
#             num_guesses -= 1
#             available_letters.remove(guess)                     #ability to remove elements, I over looked using this
#             print 'Oops! That letter is not in my word: ' + partial_word(secret_word, guessed_letters)
#         else:
#             available_letters.remove(guess)
#             guessed_letters += guess                            #puts ocrrectly guessed letters in a tuple
#             print 'Good guess: ' + partial_word(secret_word, guessed_letters)
#         if secret_word == partial_word(secret_word, guessed_letters):
#             word_guessed = True                                 #when these are equivalent word_guess = True exits this while loop
#     if word_guessed:
#         print 'Congratulations, you're a bitch!'
#     else:                                                       #another option is number of guesses reaching 0 w/o guess true, bringing us here
#         print 'You lost, you're a bitch.'
