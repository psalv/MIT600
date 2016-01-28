__author__ = 'paulsalvatore57'






# 6.00 Problem Set 4
#
# Part 1 - HAIL CAESAR!
#
# Name          : Solutions
# Collaborators : <your collaborators>
# Time spent    : <total time>


import string
import random
# import numbers

WORDLIST_FILENAME = "Assignment 4 words.txt"

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
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
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

def get_story_string():
    """
    Returns a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story


# (end of helper code)
# -----------------------------------



















#
# Problem 1: Encryption
#
def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers. The empty space counts as the 27th letter
    of the alphabet, so spaces should be mapped to a lowercase letter as
    appropriate.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    assert shift >= 0 and shift < 27, 'shift %s is not between 0 and 27' % shift
    #numbers.Integral used in case of long integers
    # assert isinstance(shift, numbers.Integral), 'shift is not an integer'

    coder = {}

    lowercase_and_space = string.ascii_lowercase + ' '
    uppercase_and_space = string.ascii_uppercase + ' '

    # Shift letters over shift places
    shifted_lowercase_and_space = lowercase_and_space[shift:] + lowercase_and_space[:shift]
    shifted_uppercase_and_space = uppercase_and_space[shift:] + uppercase_and_space[:shift]

    # Construct Caesar cipher dictionary
    # Add uppercase letters first so ' ' will be overwritten to point to lowercase letter
    for i in range(len(uppercase_and_space)):
        coder[uppercase_and_space[i]] = shifted_uppercase_and_space[i]

    for i in range(len(lowercase_and_space)):
        coder[lowercase_and_space[i]] = shifted_lowercase_and_space[i]

    return coder

# print build_coder(26)

def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >> apply_coder("Hello, world!", build_coder(3))
    'Khoor,czruog!'
    >> apply_coder("Khoor,czruog!", build_coder(24))
    'Hello, world!'
    """
    encoded_text = ''
    #For each letter added encoded value
    for letter in text:
        if letter in coder:
            encoded_text += coder[letter]
        #Not a letter or space. e.g. ',' so use the character as is.
        else:
            encoded_text += letter
    return encoded_text


def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 27)
    returns: text after being shifted by specified amount.

    Example:
    >> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    >> apply_shift('Apq hq hiham a.', 19)
    'This is a test.'
    """
    assert shift >= 0 and shift < 27, 'shift %s is not between 0 and 27' % shift
    return apply_coder(text, build_coder(shift))


#
# Problem 2: Decryption
#
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
        print potential_words
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










# def decrypt_story():
#     """
#     Using the methods you created in this problem set,
#     decrypt the story given by the function get_story_string().
#     Once you decrypt the message, be sure to include as a comment
#     at the end of this problem set your decryption of the story.
#
#     returns: string - story in plain text
#     """
#     story = get_story_string()
#     best_shift = find_best_shift(wordlist, story)
#     return apply_shift(story, best_shift)
#
#
#
# #What is the decrypted story?
# #
# ##Jack Florey is a mythical character created on the spur of a moment
# ##to help cover an insufficiently planned hack. He has been registered
# ##for classes at MIT twice before, but has reportedly never passed a
# ##class. It has been the tradition of the residents of East Campus to
# ##become Jack Florey for a few nights each year to educate incoming
# ##students in the ways, means, and ethics of hacking.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# 6.00 Problem Set 4
#
# Part 2 - RECURSION
#
# Name          : Solutions
# Collaborators : <your collaborators>
# Time spent    : <total time>

#
# Problem 3: Recursive String Reversal
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
#     if string == "":
#         return ""
#     else:
#         return string[-1] + reverse_string(string[:-1])
#
#
# #
# # Problem 4: Srinian
# #
# def x_ian(x, word):
#     """
#     Given a string x, returns True if all the letters in x are
#     contained in word in the same order as they appear in x.
#
#     >>> x_ian('srini', 'histrionic')
#     True
#     >>> x_ian('john', 'mahjong')
#     False
#     >>> x_ian('dina', 'dinosaur')
#     True
#     >>> x_ian('pangus', 'angus')
#     False
#
#     x: a string
#     word: a string
#     returns: True if word is x_ian, False otherwise
#     """
#     if len(x) == 0:
#         return True
#     elif len(word) == 0:
#         return False
#     elif x[0] == word[0]:
#         return x_ian(x[1:], word[1:])
#     else:
#         return x_ian(x, word[1:])
#
#
# #
# # Problem 5: Typewriter
# #
# def insert_newlines(text, line_length):
#     """
#     Given text and a desired line length, wrap the text as a typewriter would.
#     Insert a newline character ("\n") after each word that reaches or exceeds
#     the desired line length.
#
#     text: a string containing the text to wrap.
#     line_length: the number of characters to include on a line before wrapping
#         the next word.
#     returns: a string, with newline characters inserted appropriately.
#     """
#     return insert_newlines_rec(text, line_length, line_length-1)
#
#
# def insert_newlines_rec(text, line_length, rem_length):
#     if text == '':
#         return ''
#     elif text[0] == ' ' and rem_length <= 0:
#         return '\n' + insert_newlines_rec(text[1:], line_length, line_length-1)
#     else:
#         return text[0] + insert_newlines_rec(text[1:], line_length, rem_length-1)
