'''
Created on Sep 21, 2017

@author: KhangNguyen
'''


############# QUESTION 1 ##############
def pay(wage, t):
    '''
    (number, number)->number
    returns the amount of money made with the wage and time worked
    '''
    if t > 40:
        m = wage*40
        t = t-40
        if t > 20:
            m = m + (wage*1.5)*20
            t = t-20
            m = m+ (wage*2)*t           
        else:
            m = m + (wage*1.5)*t
    else:
        m = wage*t
    
    return (m)

############# QUESTION 2 ##############
def rps(po,pt):
    '''
    (String) -> integer
    insert rock paper or scissors and return -1 if player 1 wins 0 if tie
    and 1 if player2 wins
    '''
    p1 = ord(po)
    p2 = ord(pt)
    if (p1 == p2):
        w = 0
    elif (p1 < p2):
        if(p1 == (p2-3)):
            w = 1
        else:
            w = -1
    else:
        if(p2 == (p1-3)):
            w = -1
        else:
            w = 1
    return w
