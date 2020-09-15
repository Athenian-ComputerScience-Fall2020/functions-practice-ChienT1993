'''
Collaborators: 

'''
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide (x,y): 
    return x/y

x= int(input("Enter a number: "))
y= int(input("Enter a number: "))
print ("Type 1 to add, 2 to subtract, 3 to multiply, 4 to divide")
calculator = int(input("1,2,3,4?: "))
if calculator== 1:
    print (add(x,y))
elif calculator== 2:
    print (subtract(x,y))
elif calculator== 3:
    print (multiply(x,y))
elif calculator== 4:
    print (divide(x,y))