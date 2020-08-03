def ah(l,x,y):
    '''
(list, int, int)-> (int,int)
Write a function called ah(l,x,y) that
given a list l, and integers x and y such that x <=y, returns
two numbers. The first is the number of elements of l that
are between x and y (including x and y). The second number is
the minimum element of l that is between x and y (including x
and y).
'''
    k = y
    c = 0
    for i in l:
        if i >= x and i<=y:
            c = c+1
            if i <= k:
                k = i
    return (c, k)
            
def is_perfect(x):
    '''(int)-> boolean
There are four perfect numbers less than
10,000. Write a program that prints all these four numbers.
• Your program should have a function called is_perfect that
takes as input a positive integers and returns True if it is perfect
and False otherwise.
'''
    c = 0
    for i in range(x-1):
        if x%(i+1) == 0:
            c = c+(i+1)
    return (x == c)

def allperf():
    '''
(None) -> None
it looks for all
perfect numbers smaller than 35 million. What do you notice?
Assuming that you computer can do a billion instructions in a sec, can
you figure out how long, roughly, will it take your computer to find 5th
perfect number (it is 33,550,336).
'''
    for i in range(35000000):
        if is_perfect(i) == True:
            print(i)

def arithmetic(l):
    '''(list) -> boolean
Recall that a sequence of numbers forms an arithmetic progression if the difference
between every pair of consecutive numbers is the same. For example: -5, -1, 3, 7, 11
forms an arithmetic progression since the difference between every pair of
consecutive numbers is 4. On the contrary 5, 10, 15, 24, 29 is not an arithmetic
progression since the difference between some consecutive pairs is 5 and some 4.
A sequence that has exactly one number is considered arithmetic, too
'''
    if len(l) != 1:
        k = l[1] - l[0]
        for i in range(len(l)-1):
            #print(l[(i+1)], l[(i)])
            if l[(i+1)] - l[i] != k:
                return False
    return True

def is_sorted(l):
    '''(list) -> boolean
check if the list given is in chronological order so from smallest to biggest
'''
    if len(l) != 1:
        for i in range(len(l)-1):
            #print(l[(i+1)], l[(i)])
            if l[(i+1)] - l[i] < 0:
                return False
    return True
