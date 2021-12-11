# 1)--------help()--------------------------------
"The help function is possibly most impartant Python funstion you can learn"
# Ex:
help(round)
""" round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

    if ndigits = -1 rounds to nearest 10 ( 338,424    becomes  338,000   ndigits = -3 )
    if ndigits = -2 round to nearest 100 ( 2,166,086  becomes  2,166,000 ndigits = -3 )
    """


# 2)-----------Common pitfall---------------------------------
help(round(-2.01))
""" When you're looking up a function, remember to pass in the name of the function itself, and not the 
    result of calling that function.
    Python evaluates an expression like this from the inside out.
    First it calculates the value of round(-2.01), then it provides help on the output of that expression.
"""


# 3)---------Function and Docstring----------------------
def least_difference(a,b,c):
    """Return the smallest difference b/w any two numbers among a,b and c
    >>> least_difference(1,5,-5)
        4
    """
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    return min(diff1,diff2,diff3)

print(least_difference(1,10,100),least_difference(1,10,10),least_difference(5,6,7))         # 9 0 1
help(least_difference)

""" def    -> Keyword
    :      -> denotes next line block of def
    return -> keyword uniquely associated with functions exits the function immediately, and passes the
    value on the right hand side to the calling context.
"""


# 4)--------------Function that don't return--------------------------
def Least_Difference(a,b,c):
    """Return the smallest difference b/w, any two numbers amon a,b,c"""
    diff1 = abs(a-b)
    diff2 = abs(b-c)
    diff3 = abs(a-c)
    min(diff1,diff2,diff3)
print(Least_Difference(1,10,100),Least_Difference(1,10,10),Least_Difference(5,6,7))    #None None None

"""
-> The result of calling them is the special value None i.e. NULL "
-> Without a return statement, function is completely pointless.
-> print(),help() don't return anything.
"""
mystery = print()
print(mystery)          # None


# 5)---------------Default Arguments-------------------------------
print(1,2,3, sep = '<')         # 1<2<3
" sep='' : has default value a single space "
print(1,2,3)        # 1 2 3

"""Optional arguments with default values to the function"""
def greet(who = "colin"):
    print("Hello,",who)
greet()
greet(who = "kaggle") # We don't need to specify the name of the arguments
greet("world")

""" Output:
    Hello, colin
    Hello, kaggle
    Hello, world
"""
"""If no second argument is provided, it should assume default argument."""
def to_smash(total_candies, friend =3):
    return total_candies%friend
to_smash(10,2)      # fr =2
to_smash(10)        # fr =3


# 6)------------------Higher-order function--------------------
"""Function that operate on other function are called "Higher-order function"""
# Ex: 1)
def mult_by_five(x):
    return 5*x
def call(fn,arg):
    """Call fn on arg"""
    return fn(arg)
def squared_call(fn,arg):
    """Call fn on the result of calling fn on arg"""
    return fn(fn(arg))
print(call(mult_by_five,1),squared_call(mult_by_five,1), sep ='\n')
"""Output:
    5
    25
"""
# Ex: 2) max() ->Built-in function
def mod_5(x):
    """Return the remainder of x after dividing by 5"""
    return x%5
print("Which number is biggest?",
    max(100,51,14),"Which number is biggest modulo 5?",
    max(100,51,14, key=mod_5), sep='\n')
"""Output:
    Which number is biggest?
    100
    Which number is biggest modulo 5?
    14
"""

# 7)------------------------pass-----------------------------
"""It does nothing. We used it as a placeholder bacause after we begin a code block,
   Python requires at least one line of code"""