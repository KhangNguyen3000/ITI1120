import math

'''
Created on Sep 13, 2017

@author: Khang Nguyen
'''

def t(x, y):
    return(x*y)/2

def c(r):
    return(2*math.pi*(r**2))

def sadd(a, b):
    return a+b

def stm(s):
    h = s//3600
    m = (s%3600)//60
    s = (s%3600)%60
    print(str(h)+"h."+str(m)+"min:"+str(s)+"sec")
    return (h , m, s)

def f1(x):
    '''
    (number) -> number
    return x to the power 2 and then added 2
    
    '''
    return x**2+10 

def f2(x):
    print(x**2+10)
    
def rect():
    print("***********")
    print("***********")
    print("***********")
    print("***********")
    print("***********")
    return None

