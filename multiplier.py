'''
Adapt the code from one of the functions above to create a new function called 'multiplier'.
The user should be able to input two numbers that are stored in variables.
The function should multiply the two variables together and return the result to a variable in the main program.
The main program should output the variable containing the result returned from the function.
'''
def multiplier():
    x= int(input("Type in 1st number for multiply: "))
    y= int(input("Type in 2nd number for multiply: "))
    return x*y


output= multiplier()
print (output)
