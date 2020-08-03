def largest_34(a):
    '''
(List) -> int
returns the sum of the 3rd and 4th largest values in
the list a
'''
    a.sort(reverse= True)
    return (sum(a[2:4]))
    
def largest_third(a):
    '''
(List) -> int
computes the sum of the len(a)//3 of the
largest values in the list a
'''
    a.sort(reverse= True)
    return (sum(a[:((len(a)//3))]))

def third_at_least(a):
    '''
(List) -> int
returns a value in a that occurs at least
len(a)//3 + 1 times. If no such element exists in a, then this function returns None. If more than
one such element exists, you should return the smaller one
'''
    a.sort()
    c = (len(a)//3)

    for i in range (len(a)-c):
        if a[i] == a[i+c]:
            return a[i]
    return None

def sum_tri(a,x):
     '''
(List, int) -> boolean
returns True if there
exists indices i, j and k (where i and j and k are not necessarily distinct) such that a[i]+a[j]+a[k]=x.
Otherwise it returns False.
'''
    sorted(set(a))
    for i in range(len(a)):
        for e in range(len(a)):
            for t in range(len(a)):
                if a[i]+a[e]+a[t] == x:
                    return True
    return False


