__author__ = 'paulsalvatore57'


# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton

import string
import random

WORDLIST_FILENAME = "Assignment 4 words.txt"
# FABLE = 'Assignment 4 fable.txt'

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >> is_word(wordlist, 'bat') returns
    True
    >> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")       #removes non-alphabetical characters
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("Assignment 4 fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------


# Problem 1: Encryption



def build_encoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict
    """

    lc_List_Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',\
                     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',\
                     'y', 'z', ' ']

    uc_List_Letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',\
                     'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',\
                     'Y', 'Z']

    lc_Dict_Letters = {'a': 0, 'c': 2, 'b': 1, 'e': 4, 'd': 3, 'g': 6, 'f': 5, 'i': 8,\
                  'h': 7, 'k': 10, 'j': 9, 'm': 12, 'l': 11, 'o': 14, 'n': 13, 'q': 16,\
                  'p': 15, 's': 18, 'r': 17, 'u': 20, 't': 19, 'w': 22, 'v': 21, 'y': 24,\
                  'x': 23, 'z': 25, ' ': 26}

    uc_Dict_Letters = {'A': 0, 'C': 2, 'B': 1, 'E': 4, 'D': 3, 'G': 6, 'F': 5, 'I': 8,\
                  'H': 7, 'K': 10, 'J': 9, 'M': 12, 'L': 11, 'O': 14, 'N': 13, 'Q': 16,\
                  'P': 15, 'S': 18, 'R': 17, 'U': 20, 'T': 19, 'W': 22, 'V': 21, 'Y': 24,\
                  'X': 23, 'Z': 25}

    for i in lc_Dict_Letters:
        lc_Dict_Letters[i] = lc_Dict_Letters[i] + shift
    for i in lc_Dict_Letters:
        if lc_Dict_Letters[i] <= 26:
            lc_Dict_Letters[i] = lc_List_Letters[lc_Dict_Letters[i]]
        else:
            lc_Dict_Letters[i] = abs(27 - lc_Dict_Letters[i])
            lc_Dict_Letters[i] = lc_List_Letters[lc_Dict_Letters[i]]

    for i in uc_Dict_Letters:
        uc_Dict_Letters[i] = uc_Dict_Letters[i] + shift
    for i in uc_Dict_Letters:
        if uc_Dict_Letters[i] <= 25:
            uc_Dict_Letters[i] = uc_List_Letters[uc_Dict_Letters[i]]
        else:
            uc_Dict_Letters[i] = abs(26 - uc_Dict_Letters[i])
            uc_Dict_Letters[i] = uc_List_Letters[uc_Dict_Letters[i]]

    for i in uc_Dict_Letters:
        lc_Dict_Letters[i] = uc_Dict_Letters[i]

    return lc_Dict_Letters



#Removed build_encoder(shift) because I did not see a difference between it and build_coder in terms of function.



def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands:

    >>encoder = build_encoder(shift)
    >>encrypted_text = apply_coder(plain_text, encoder)
    >>decrypted_text = apply_coder(plain_text, decoder)

    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict
    """
    decoder = build_encoder(-shift)
    return decoder



def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >> apply_coder("Hello, world!", build_encoder(3))
        'Khoor,czruog!'
    >> apply_coder("Khoor,czruog!", build_decoder(3))
        'Hello, world!'
    """
    message = ()
    message1 = ''
    for i in text:
        if i in coder:
            message = message + (coder[i],)
        else:
            message = message + (i,)
    for i in message:
        message1 = message1 + i
    return message1



def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    message = apply_coder(text, build_encoder(shift))
    return message


# -----------------------------------


# Problem 2: Decryption

#Pseudocode:
    #1 Start with shift = -26, maximum shift of 26
    #2 Create a dictionary using the build_decoder function for each shift
    #3 Attempt to decode the text
    #4 Collect words, creating new words at spaces
    #5 Check to see if the word is in the wordbank we have
    #6 Keep a running tally of how many words are associated with
        #dict[max(dict, key = dict.get)] this code will allow me to extract the highest number of word matches


# def find_best_shift(wordlist, text):
#     """
#     Decrypts the encoded text and returns the plaintext.
#     text: string
#     returns: 0 <= int 27
#     Example:     >>> s = apply_coder('Hello, world!', build_encoder(8))
#     >> s
#     'Pmttw,hdwztl!'
#     >> find_best_shift(wordlist, s) returns
#     8
#     >> apply_coder(s, build_decoder(8)) returns
#     'Hello, world!'
#     """
#
#     shift = -26
#     realwords = {}
#     while shift < 27:
#         temp = ''
#         numberwords = 1
#         word = (apply_coder(text, build_decoder(shift)).lower()) + "."
#         # print word
#         for i in word:
#             # print i
#             if i in build_encoder(0):                           #determines if it is a letter or a character
#                 if i == " ":                                    #if the character is a space, it will check to see if we have a word
#                     if temp in wordlist:
#                         realwords[shift] = numberwords          #if we do have a word, then the shift gets assigned a number in a dictionary
#                         numberwords += 1                        #if we get another word, this will increase the value in the dictionary
#                     temp = ''                                   #resets temp to prepare for next potential word
#                 else:
#                     temp = temp + i                             #this builds the words until a space is hit
#             if i not in build_encoder(0) and temp in wordlist:  #this code checks at punctation and at the end of the sentence to see if it is a real word
#                 realwords[shift] = numberwords
#                 numberwords += 1
#                 temp = ''
#         shift += 1
#     # print realwords
#     # else:
#     return max(realwords, key=realwords.get)
#
#
# text = 'does this, WOrk, at all or? is it broken!'
# encripted = apply_shift(text, 15)
# print find_best_shift(wordlist, encripted)


#HIS SOLUTION:

def find_best_shift(wordlist, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 27

    Example:
    >> s = apply_shift('Hello, world!', 8)
    >> s
    'Pmttw,hdwztl!'
    >> find_best_shift(wordlist, s)
    19
    >> apply_shift(s, 19)
    'Hello, world!'
    """
    max_num_real_words = 0
    best_shift = 0
    # Try all possible shifts
    for shift in range(27):
        # Try shifting with current shift
        shifted_text = apply_shift(text, shift)

        # Split text into potential words
        potential_words = shifted_text.split()
        # print potential_words
        num_real_words = 0
        # Count number of actual words
        for word in potential_words:
            if is_word(wordlist, word):
                num_real_words += 1
        # Best shift is determined by most number of valid words produced
        if num_real_words > max_num_real_words:
            max_num_real_words = num_real_words
            best_shift = shift
    return best_shift

# print find_best_shift(wordlist, 'Pmttw,hdwztl!')


# -----------------------------------

# Problem 3: Multi-level Encryption and Decryption

def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.
    text: A string to apply the Ceasar shifts to
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.
    returns: text after applying the shifts to the appropriate
    positions
    Example:
    >> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    temp = ''
    for i in range(len(shifts)):
        temp = text[:(shifts[i][0])]
        text = temp + apply_shift(text[(shifts[i][0]):], (shifts[i])[1])
    return text


def apply_shifts_reverse(text, shifts):
    """
    Does the same thing as apply_shifts, however in reverse, to regenerate readable text
    """
    temp = ''
    for i in range(len(shifts)):
        temp = text[:(shifts[i][0])]
        text = temp + apply_shift(text[(shifts[i][0]):], -(shifts[i])[1])
    return text






# -----------------------------------


# Problem 4: Multi-level Code-Breaking

#shifts can only change at the start of a word
#therefore if you find the correct word, the shift cannot change until there is a space
#recursion is highly recommended for this problem


#What is the basecase?
    #Think about the start parameter, what is the basecase (it is not 0)

    #When there is only one word, there is only one shift
    #I need to find the very first word, so I need to start from the left side, and try every encryption level going right until I have a word
        #This could potentially generate many shorter words that are not correct
        #But it will be followed by a space, therefore this is how we tell



#Pseudocode:
    #1 Separate the words of the sentence into a list (done by separating at spaces)
        #spaces are removed by the shift, therefore this isn't possible
    #2 Use the find_best_shift fxn to find the likely shift for the first word in the list
        #store this shift in a dictionary example of shift 1: d = {1: [1, 2, 3, 4, 5], 2: [3, 4, 5]} etc.
    #3 Next use find best shift, followed by the previous shift(s) found in part two (or earlier)
        #this is necessary to search if there is a shift at the next word
    #4 Do this for the entire sentence
    #5 After all of the most probable shifts have been found, they can be implemented


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text
    to words in wordlist, or None if there is no such key.

    ***HINT: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)***
    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)

    Examples:
    >> s = random_scrambled(wordlist, 3)
    >> s = 'eqorqukvqtbmultiform wyy ion'

    >> shifts = find_best_shifts(wordlist, s)
    >> shifts = [(0, 25), (11, 2), (21, 5)]

    >> s = apply_shifts(s, shifts)
    >> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0, 6), (3, 18), (12, 16)])
    >> s = 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'

    >> shifts = find_best_shifts(wordlist, s)
    >> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """
    n = 1
    placeholder = 0
    answer = []
    answer2 = ()
    R = None
    while n < len(text):
        if find_best_shifts_rec_rest(wordlist, text, n, R)[1] != 0:
            answer.append((placeholder, (find_best_shifts_rec_rest(wordlist, text, n, R))[1]))
            placeholder = placeholder + find_best_shifts_rec_rest(wordlist, text, n, R)[0]
            n += 1
        elif find_best_shifts_rec_rest(wordlist, text, n + 1, R)[1] == 0 and answer != []:
            answer2 = apply_shifts_reverse(text, answer).split()
            counter = 0
            for i in answer2:
                if is_word(wordlist, i) == True:
                    counter += 1
            if counter == len(answer2):
                return answer
            else:
                placeholder = placeholder - find_best_shifts_rec_rest(wordlist, text, n - 1, R)[0]
                answer.remove((placeholder, (find_best_shifts_rec_rest(wordlist, text, n - 1, R))[1]))
                R = find_best_shifts_rec_rest(wordlist, text, n - 1, R)[1]
                n -= 1
        elif find_best_shifts_rec_rest(wordlist, text, n + 1, R)[1] != 0 and answer != []:
            placeholder = placeholder + find_best_shifts_rec_rest(wordlist, text, n, R)[0]
            n +=1
        else:
            return None




def find_best_shifts_rec_rest(wordlist, text, start, restriction):
    """
    Returns the shifts that result in the encryption of segments of the code,
    and their corresponding starting point. Restrictions are added when premature words are found
    """
    text = text + "."
    if start != 0:
        for i in range(1, start):
            text = (apply_shift(text, -(find_best_shifts_rec_rest(wordlist, text, i - 4, restriction))[1]))\
                [(find_best_shifts_rec_rest(wordlist, text, i - 4, restriction))[0]:]
    shift = 0
    while shift < 27:
        if shift == restriction:
            shift += 1
        temp = ''
        word = (apply_coder(text, build_decoder(shift)).lower())
        for i in word:
            if i == ' ' or i not in build_encoder(0):
                    if temp in wordlist:
                        return (len(temp) + 1, shift)
                    else:
                        break
            else:
                temp = temp + i
        shift += 1
    return (0, 0)


####TESTING CODE

def TestHandle():
    """
    Tests a variety of different cases against my shift finding program
    """
    original = 'JufYkaolfapxRdrnzmasmSyrpfdvpmGurrb?'
    deferrals = 'd jjzsgwjrvgfltafxjksugqnglcqqyfghgttcnu'
    new1 = 'snsjxevjcsiydcutpfqypvwtpubtgogfkcdngbwsbvkhsxq'
    print 'Original:', find_best_shifts(wordlist, original)
    print 'Expected: [(0, 6), (3, 18), (12, 16)]'
    print "-----------------"
    print 'Deferalls:', find_best_shifts(wordlist, deferrals)
    print 'Expected: [(0, 18), (10, 1), (21, 6), (31, 4)]'
    print "-----------------"
    print 'New1:', find_best_shifts(wordlist, new1)
    print 'Expected: [(0, 5), (6, 11), (17, 13), (38, 8)]'
    print "-----------------"
    print 'Premature:', find_best_shifts(wordlist, 'rkjfubax ayuwpjufkuzwv')
    print 'Expected: [(0, 24), (8, 19), (14, 2)]'
    print "-----------------"
    print 'None:', find_best_shifts(wordlist, 'abcdef')
    print 'Expected: None'

# TestHandle()


def Generate_Abnormal():
    """
    Searches for non-conventional random strings, and returns the shift values, the word, and what the decrypted sentence would be
    """
    n = 1
    q = 0
    while n <= 5:
        s = random_scrambled(wordlist, n)

        if (find_best_shifts(wordlist, s)) == None:
            print "----------"
            print "String:", s
            print "----------"

        elif len(find_best_shifts(wordlist, s)) != n:
            print "----------"
            print "String:", s
            print "Shifts found:", find_best_shifts(wordlist, s)
            print 'Words generated:', apply_shifts_reverse(s, find_best_shifts(wordlist, s))
            print "----------"
        else:
            print "All good"
        q += 1
        if q % 5 == 0:
            n +=1
            print n

# Generate_Abnormal()


#It appears that the only bug I have left is finding a word prematurely which is not the intended word






# print "Incorrect:", apply_shifts_reverse(s, [(0, 6)])
# print "Correct:", apply_shifts_reverse(s, [(0, 7), (9, 10)])

#The problem is that it is possible to encounter a real word that is not the correct word, followed by a space
#My solution to this would be to prove that the shift is ideal using the find_best_shift function
#My attempts are getting there

# -----------------------------------


# Problem 5: The Moral of the Story


# fable = 'eyrzmilf,hifalykanonjmaytfduckxnjkliewvrutfetqllksan.wymjexlnstypkxaatsxpht'
# print find_best_shifts(wordlist, fable)
# print apply_shifts_reverse(fable, find_best_shifts(wordlist, fable))














###EXTRA QUESTIONS?

# # Problem 3: Recursive String Reversal
#
# def reverse_string(string):
#     """
#     Given a string, recursively returns a reversed copy of the string.
#     For example, if the string is 'abc', the function returns 'cba'.
#     The only string operations you are allowed to use are indexing,
#     slicing, and concatenation.
#
#     string: a string
#     returns: a reversed string
#     """


# Problem 4: Srinian

#basecase: if len(x) = 1 and x in word, then it is True


def x_ian(x, word):
    """
    Given a string x, returns True if all the letters in x are
    contained in word in the same order as they appear in x.

    >> x_ian('srini', 'histrionic')
    True
    >> x_ian('john', 'mahjong')
    False
    >> x_ian('dina', 'dinosaur')
    True
    >> x_ian('pangus', 'angus')
    False

    x: a string
    word: a string
    returns: True if word is x_ian, False otherwise
    """
    for i in x:
        if i not in word:
            return False
        else:
            word = word[word.index(i) + 1:]
    return True

# print x_ian('todoo', 'todooay')



# # Problem 5: Typewriter
# #
def insert_newlines(text, line_length):
    """
    Given text and a desired line length, wrap the text as a typewriter would.
    Insert a newline character ("\n") after each word that reaches or exceeds
    the desired line length.

    text: a string containing the text to wrap.
    line_length: the number of characters to include on a line before wrapping
        the next word.
    returns: a string, with newline characters inserted appropriately.
    """
    counter = 0
    line = ''
    for i in text:
        line += i
        counter += 1
        if counter == line_length:
            line += '\n'
            counter = 0
    return line


