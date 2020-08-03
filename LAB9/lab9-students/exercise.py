def get_year():
    while True:
        c = input("Please enter a 4 digit integer \t")
        try:
            int(c)
            return c
        except ValueError:
            print("that was not a 4 digit integer")

def min_or_max_index(l, b):
    v = [0,l[0]]
    if b:
        for i in range(len(l)):
            if l[i] < v[1]:
                v[0] = i
                v[1] = l[i]
    else:
        for i in range(len(l)):
            if l[i] > v[1]:
                v[0] = i
                v[1] = l[i]
    return (v[0], v[1])

def first_one(L):
    b=0
    e = len(L) - 1

    while b != e + 1:
        mid = (b + e) // 2
        if L[mid] < 1:
            b=mid+1
        else:
            e=mid-1
          
    if 0 <= b < len(L) and L[b] == 1:
        return b
    else:
        return -1

def last_zero(L):
    return (first_one(L) - 1)

def selection_sort_v1(L):
     ''' sorts given list L'''
     for i in range(len(L)-1):
          # Find the minimum in the list[i..len(L)-1]
          min_index=i
          for j in range(i+1, len(L)):
               if(L[min_index]>L[j]):
                    min_index=j
          #Swap L[i] with L[min_index] if necessary
          L[i],L[min_index]=L[min_index], L[i]
          print(L)
