__author__ = 'paulsalvatore57'


            ###Concepts that will be useful and may be confusing.


#1----------------------------------------------------------------------------------------------------------------------

    #One of the first concepts we learned involved EPSILON. This was a useful tool for approximations.
        #You pick an epsilon value that represents and acceptable degree of error for our problems to fall within,
        #Then subsequent guesses are narrowed until the desired answer is found.

        #The example given in Class 4 was finding square roots by this method.

#2----------------------------------------------------------------------------------------------------------------------

    #The next concept was called RECURSION, a useful tool for breaking complicated problems into their substeps.
        #Recursion has the fundamental principle of the basecase: the simplest form a problem can be.

        #For instance, in Finonacci numbers we know that when i <= 1, n = 1, so this is the basecase,
        #Meaning that an algorithm that reduces i to this base case and adds the results will be correct.

        #When sorting this concept will appear again since we know that any list of length one is trivially sorted.

#3----------------------------------------------------------------------------------------------------------------------

    #An important concept I have been spoiled by having made for me is a TEST HARNESS.
        #This is a tool we write to help debug our programs; it should consider the various cases that can go wrong,
        #And tested them with helpful readouts for debugging.
        #Writing a test harness will be worth the time saved troubleshooting and is a valuable repeatable experiment.

#4----------------------------------------------------------------------------------------------------------------------

    #How long a program will take to run is defined by ORDER OF GROWTH.
        #This depends on how many iterations through various cycles the program must perform,
        #However anything beyond log linger - O(n log n) - should be avoided, especially when the program may be scaled.

        #The log n order will appear many times due to it's involvement in a binary search,
        #Wherein the search options are shortened as the search continue.

#5----------------------------------------------------------------------------------------------------------------------

    #A sorting technique widely used in computing is DIVIDE AND CONQUER.
        #This technique follows the same principles as recursion by breaking the problem into smaller, workable pieces.

        #This technique is specifically used in sorting functions,
        #Such that each sorting iteration does not require iteration through the entire list.



#STOPPED ON LECTURE 11, I BELIEVE INHERITANCE SHOULD BE NEXT.