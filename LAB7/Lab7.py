def indexes(s1,s2):
    '''(string,string) -> list
takes a string and a one letter string and returns list with everysingle index of the letters presence in the string

'''
    l = []
    for i in range(len(s1)):
        if s1[i] == s2[0]:
            l.append(i)
    return l

def doubles(l):
    '''(list)-> None
Takes a list of integeres and prints out every single pair in wich the latter is double the one before
'''
    for i in range(0,len(l)-1,2):
        if (l[i]*2) == l[i+1]:
            print(l[i+1])

def four_letter(l):
    '''
(list) -> list
takes a list and returns a list of the 4 letter words
'''
    l2 = []
    for i in range(len(l)):
        if len(l[i]) == 4:
            l2.append(l[i])
    l2 = list(set(l2))
    return(l2)

def inBoth(l,l2):
    '''
(list,list)-> boolean
takes 2 lists and if an element is present in both lists returns true
'''
    for i in range(len(l)):
        for k in range(len(l2)):
            if l2[k] == l[i]:
                return True
    return False

def intersect(l,l2):
    '''
(list,list) -> list
takes 2 lsits and returns  a list of every single element in common
'''
    l3 = []
    for i in range(len(l)):
        for k in range(len(l2)):
            if l2[k] == l[i]:
                l3.append(l2[k])
                
    return l3

def pair(l,l2,n):
    '''
(list,list,integer) -> None
takes 2 lists and an integer then prints out every single pair 1 from list1 and 1 from list2 that when added together give the integer
'''
    for i in range(len(l)):
        for k in range(len(l2)):
            if (l2[k] + l[i]) == n:
                print(l[i],l2[k])

def pairSum(l,n):
    '''
(list,integer) -> none
takes a list and prints out every single pair which gives out the integer picked as sum
'''
    for i in range(len(l)):
        for k in range(i, len(l)):
            if l[i] + l[k] == n:
                print(i, k)

def lastfirst(l):
    '''
(list) -> list,list
takes a list of names an dreturns 2 lists, one withthe last names and one with the first names
'''
    l2 = []
    l3 = []
    for i in range(len(l)):
            y = l[i].split(",")
            l2.append(y[0])
            l3.append(y[1])
    return(l3,l2)

def subsetSum(l,n):
    '''
(list,integer) -> boolean
takes a list and an integer then checks if any combinations of elements in the list gives the integer the n gives back true or false
'''
    for i in range(len(l)):
        for k in range(i, len(l)):
            for q in range(k,len(l)):       
                if l[i] + l[k] + l[q] == n:
                    return True
    return False
    
def mystery(n):
    '''
(integer) -> integer
takes a random integer and returns the number of times it takes to multiply it by 2
'''
    a = 0
    while n > 1:
        n = n//2
        a = a+1
    return a

def inversions(s):
    '''
(string) -> integer

takes a string and swaps 2 characters at a time so the string is alphabetical then returns the number of swaps needed
'''
    a = 0
    c = False
    while c == False:
        c = True
        l = []
        for i in range(len(s)-1):
            if s[i] > s[i+1]:
                if i != 0:
                    l.pop()
                l.append(s[i+1])
                l.append(s[i])
                a = a+1
                c = False
            else:
                if i == 0:
                    l.append(s[i])
                l.append(s[i+1])
        s = "".join(l)
    return a
        
def sublist(l,l2):
    '''
(list,list) -> boolean
takes 2 lsit and returns true if list 1 is a subset of list 2
'''
    q = []
    for i in range(len(l)):
        for k in range(len(l2)):
            if l[i] == l2[k]:
                q.append(k)
    t = q[:]
    q.sort()
    if q == t:
        return True
    else:
        return False

def mssl(l):
    '''
(list) -> integer
takes a list and checks everysingle combination fo sums and gives out the largest number
'''
    b = 0
    for i in range(len(l)):
        a = 0
        for k in range(i,len(l)):
            a = a+l[k]
            if (a > b):
                b = a
    return b
            


























