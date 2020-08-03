'''
Created on Sep 21, 2017

@author: KhangNguyen
'''

def is_divisible(x,y):
    '''
    (number,number)->boolean
    insert 2 numbers and returns wether the 1st divded by the 2nd give you 
    an integer
    '''
    if(x%y == 0):
        b = True
    else:
        b = False
    return b
x = int(input("Enter 1st integer:\n"))
y = int(input("Enter 2nd integer:\n"))

b = is_divisible(x,y)

if b == True:
    print(str(x)+" is divisible by "+str(y))
else:
    print(str(x)+" is not divisible by "+str(y))