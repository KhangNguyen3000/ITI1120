def first_neg(l):
    '''
(List) -> int
takes a (possibly empty) list of
numbers as input parameter, finds the first occurrence of a
negative number, and returns the index (i.e. the position in the
list) of that number. If the list contains no negative numbers or it
is empty, the program should return None. Use while loop (and
not for loop) and your while loop should stop looping once the
first negative number is found.
'''
    i = 0
    while i in range(len(l)):
        if l[i] < 0:
            return i
        i = i+1
        
def sum_5_consecutive(l):
    '''
(List) -> boolean
Write a function sum_5_consecutive that takes a list of numbers as input and
returns True if there are 5 consecutive numbers in the list that sum to zero.
Otherwise it returns False. The function should also return False if the list has
less than 5 elements
'''
    c = False
    if len(l) > 5:
        for i in range(len(l)-4):
            print(l[i] , l[i+1] , l[i+2] , l[i+3] , l[i+4])
            if (l[i] + l[i+1] + l[i+2] + l[i+3] + l[i+4]) == 0:
                c = True
        while i in range(len(l)-4) and (l[i] + l[i+1] + l[i+2] + l[i+3] + l[i+4]) == 0:
            print(l[i] , l[i+1] , l[i+2] , l[i+3] , l[i+4])
            c = True
            i = i + 1
    return c

def fib(n):
    '''
(int) -> List
takes as input an integer n (greater
than 1) and creates a list containing n values such that
a[0] = 1
a[1] = 1
a[i] = a[i-1] + a[i-2] for all i in the range 1 < i < n
and it prints that list once it creates it
'''
    a = [0,1]
    i = 2
    while i in range(n+1):
        a = a + [a[i-1] + a[i-2]]
        i = i + 1
    return a[1:]

def inner_product(l,n):
    '''
(List, List) -> int
takes as input two lists of
integers (of same length) and then computes and returns the inner
product of the two lists of integers. The inner product of
two lists x = [x1, x2, ..., xn] and y = [y1, y2, ..., yn] is the value
x1 y1 + x2 y2 + ... + xn yn .
'''
    i = 0
    c = 0
    while i in range (len(l)):
        c = c + l[i]*n[i]
        i = i + 1
    return c
