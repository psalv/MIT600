__author__ = 'paulsalvatore57'

#These are necessary for the commands to work
import string
import random

                    ###1 - build_encoder

#Get a string of all the letters in the alphabet:
Uletters = string.ascii_uppercase

#He used [shift:] + [:shift] to perform the shift, since each letter will be assigned a new location

#This piece of code then assigned the original letter as a key to the new letter in a dictionary
coder[uppercase_and_space[i]] = shifted_uppercase_and_space[i]

#When assigning the code, he





                    ###2 - apply_coder

#I forget that you can use the += command for adding strings onto the end of a string, this would save a few lines





                    ###3 - Find best shift

#I keep forgetting to use the 'in range' command, opting for unnecessary while loops
#My code was a little different, it looked for the shift that was done to create the given message, and then required a decoder function
#His code is smarter, it looks for the number of shifts between 0 and 27 that are necessary to get back to that starting point

#Essentially I was working backwards, he was working forwards.


#This code is interesting, it splits a string into a list, different elements representing parts of the string seperated by a space:
potential_words = shifted_text.split()

#He does this for every shift possibility, and checks if all of the elements are in the wordlist, this way every element must be present

#Instead of finding the highest index in a dictionary, he keeps a running total of the highest number of real words, and which shift was responsible:

if num_real_words > max_num_real_words:     #Ff current number of real words is the biggest\
    max_num_real_words = num_real_words         #There is a new max/
    best_shift = shift                              #And it came from this shift, best shift will be returned






                    ###Beyond

#He didn't include solutions for find_best_shifts, which is the actually hard part of the assignment
#Rather there are answers for other questions that I will do
#This is still annoying, but I feel I did a good job on the assignment
#I may continue to tinker with the current bug I am working on:
    #How do I get around a word (that was not in the original message) arising before the current shift is found,\
    #and a different shift being assigned.
        #I was thinking that using the find_best_shift function to always ensure the best shift is found would be feasible
        #I may repeat this, however using his find_best_shift function since I like it much more than my own