__author__ = 'paulsalvatore57'


### 1 IMPLIMENT THE 'evalute_poly' FXN:
#
def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # TO DO ...

    list = []
    length = int(len(poly))
    while length > 0:
        if length >= 1:
            multiplier = float(poly[length - 1])            #finds the a value in: aB^c, must be a float
            ans1 = multiplier * x ** (length - 1)               #computes aB^c
            list = list + [ans1, ]                           #collects each answer in a tuple
            length -= 1                                     #moves the loop along to the next set of values
    length = int(len(poly))                                 #resets the length variable to be used in the next part
    answer = 0.0
    while length > 0:
        answer = float(answer) + float(list[length - 1])    #this adds all of the values in the list
        length -= 1                                         #when length counts down to 0, the loop will be exited
    return float(answer)
#
# print 'Solution: ', evaluate_poly((2.2, -7, 0.4, 3), 2.1)

# This solution works for every possible combination that I can think of


### HIS SOLUTION:
#def evaluate_poly(poly, x):
    # total = 0.0
    # for i in xrange(len(poly)):           #this ensures that only the correct number of values are calculated
    #     total += poly[i] * (x ** i)       #adding them as they are computed to the total
    # return total












### 2 IMPLEMENT THE 'compute_deriv' FXN:


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 + 0.0x - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # TO DO ...

    #x^4 + 3x^3 + 17.5x^2 - 13.39

    # 4x^3 + 9x^2 + 35^x

    Lans = ()
    Tans = ()
    length = 0
    while length < len(poly):
        multiplier = float(poly[length])
        value = multiplier*length
        Lans = Lans + (value,)              #Lans represents a tuple of every derivative, however we must remove the first for proper formating
        length += 1
    length = 1                              #starting at length 1 will ensure that the first value, which will always be 0.0, is omitted
    while length < len(poly):
        Tans = Tans + (Lans[length],)
        length += 1
        # print Tans
    return Tans
#
# print 'Derivative:', compute_deriv((2, 13, 3.3837, -4))
#



### HIS SOLUTION:
# def compute_deriv(poly):
#     poly_deriv = []
#     if len(poly) < 2:
#         return [0.0]
#     for j in xrange(1, len(poly)):                  #used the range function to just skip position 1 all together
#         poly_deriv.append(float(j * poly[j]))       #we know at position 1, will be x^1, so can use this, don't need to count up\
#                                                     #again he actually appends the values as they are made rather than first caching them in an unecessary list
#     return poly_deriv









### 3 IMPLEMENTING THE 'compute_root' FXN USING NEWTON'S SUCCESSIVE APPROXIMATION METHOD:



def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # TO DO ...

    #want to find a value of x that when evaluated with the given polynomial expression is equal to 0

    guesses = 0
    answer = ()
    while abs(evaluate_poly(poly, x_0)) > epsilon:
        x_0 = x_0 - evaluate_poly(poly, x_0)/evaluate_poly(compute_deriv(poly), x_0)
        guesses += 1
    answer = answer + (x_0,) + (guesses,)
    return answer

print "Root and number of guesses:", compute_root((-13.39, 0.0, 17.5, 3.0, 1.0), 0.1, 0.0001)


# print evaluate_poly((-13.39, 0.0, 17.5, 3.0, 1.0), 0.80679)





### HIS SOLUTION:
# def compute_root(poly, x_0, epsilon):
#     root = x_0
#     counter = 1
#     while abs(evaluate_poly(poly, root)) >= epsilon:
#         root = (root - evaluate_poly(poly, root) /
#                 evaluate_poly(compute_deriv(poly), root))
#         counter += 1
#     return [root, counter]                  #I didn't think to do this, this is a much smarter idea for returning the answer


