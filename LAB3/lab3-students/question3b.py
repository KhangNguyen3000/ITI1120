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

def is_divisible23n8(x):
    '''
    (number)->String
    insert 2 numbers and returns wether the integer is divisble by and 3 but not 8
    '''
    if((is_divisible(x,2) == True and (is_divisible(x,3) == True and\
                                        (is_divisible(x,8) != True)))):
        b = "yes"
    else:
        b = "no"
    return b

x = int(input("Enter an integer:\n"))

b = is_divisible23n8(x)

if b == "yes":
    print(str(x)+" is divisible by 2 and 3 but not 8")
else:
    print("It is not true that "+str(x)+" is divisible by 2 and 3 but not 8")