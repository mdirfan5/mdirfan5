# Python - Python was named for the British comedy troupe Monty Python.

spam_amount = 0
print(spam_amount)                               # 0
spam_amount = spam_amount + 4
if spam_amount >0:
    print("But I don't want Any spam!")          # But I don't want Any spam!
viking_song = "Spam " * spam_amount              # Spam Spam Spam Spam 
print(viking_song)

"""
1) Variable Assignment
    -> "=" called Assignment operator.
    -> We don't need to "declare" spam_amount before assigning to it.    
    -> In fact, we can reassign(different type like string, boolean e.t.c)

2) Function Calls
    -> print() is a function that display value passed to it on the screen.

3) Comment
    -> comments begin with the # symbol.
    -> spam_amount = spam_amount + 4
        Python evaluates the expression the expression first who on the right hand-side and then assign to variable.

4) if condition :
    -> :(colon) at the end of the 'if' line indicates that a new code block is starting.
    -> Subsequent lines which are intended are part of the code block.

5) String
    Strings can be marked either by double or single quotation marks.

6) * Operator
    -> multiply two numbers (3*3)=9
    -> multiply string by a number, that's been repeated that many times.

7) type function
    -> type(5) tells its type "int"
    -> It's very useful to be able to ask Python "What kind of thing is this?"
"""


#       Operator        Name                Discription
"""     a + b           Addition            Sum
        a - b           Subtraction         Difference
        a * b           Multiplication      Product
        a / b           True Division       Quetient 
        a // b          Floor Division      Quetient, removing fuctional part
        a % b           Modulus             Integer reminder after Division
        a ** b          Exponentiation      a raise to the power of b
        - a             Negation            The nagation of a
"""

# Ex :
print(5/2, 6/2, "Float value")          # 2.5 3.0 Float value
print(5//2, 6//2, "Int value")          # 2 3 Int value

""" Order of operation:
    Some people remember this by amnemonic such as 
    "PEMDAS" -> Parantheses, Exponet, Multiplication/Division, Addition/Subtraction
    "BADMAS"
"""
#--------------------How tall am I, when wearing my hat?(in meters)--------------------
hat_height_cm = 25
my_height_cm = 190
total_hight_meters = (hat_height_cm + my_height_cm)/100     # Insteed of "hat_height_cm + my_height_cm/100"
print(total_hight_meters)


#-------------max(), min()-------------------------------------
""" Return the maximum and minimum of their arguments """
print(max(1,2,3,4,5))
print(min(1,2,3,4,5))

#-------------abs()-----------------------------------
""" Return the absolute value of an argument"""
print(abs(32),abs(-32))

#-----------------Typecasting----------------------------------
""" int(),float() can also called as functions which covert their argument to the corresponding type """
print(float(10))
print(int(3.33))
print(int('807')+ 1)