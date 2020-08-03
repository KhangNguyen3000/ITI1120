'''
Created on Oct 2, 2017

@author: Khang Nguyen
'''

def print_vowle(p):
    '''
    (str) -> None
    '''
    for ch in p:
        if "AEIOUaeiou".__contains__(ch):
            print(ch)
            
            
def c_vowle(p):
    '''
    (str) -> int
    '''
    z =0;
    for ch in p:
        if "AEIOUaeiou".__contains__(ch):
            z = z+1
            
    return z

def v_vowle(p):
    '''
    (str) -> str
    '''
    z ="";
    for ch in p:
        if "AEIOUaeiou".__contains__(ch):
            z = z+str(ch)
            
    return z