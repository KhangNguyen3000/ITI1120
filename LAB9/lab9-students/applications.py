# QUESTION 1

def element_uniqueness(L):
     '''(list)->bool
     Returns True if all the elements in the list are distinct,
     in other words, if there is no element in the list that appears more than once.
     Precondition: L is not empty

     >>> element_uniqueness([2, 2,2, 2, 8])
     False
     >>> element_uniqueness([1,-20,-1])
     True
     >>> element_uniqueness([3,2,4,0,3])
     False
     >>> element_uniqueness([10])
     True
     >>> element_uniqueness([10,10])
     False
     >>> element_uniqueness([10,-1])
     True
     '''
     L.sort
     for i in range(len(L)-1):
          if L[i] == L[i+1]:
               return False
     return True
          
 
# QUESTION 2

def one_unique_at_least(L):
     '''(list)->bool
     Returns True if there exist at least one element in L that is unique,
     in other words, that appears exactlly once in the list
     Precondition: L is not empty
     >>> one_unique_at_least([2,2,2,2,8])
     True
     >>> one_unique_at_least([2,1,2])
     True
     >>> one_unique_at_least([1,-20,-1])
     True
     >>> one_unique_at_least([3,2,2,3,3])
     False
     >>> one_unique_at_least([10])
     True
     >>> one_unique_at_least([10,10])
     False
     >>> one_unique_at_least([10,-1])
     True
     '''
     L.sort()
     if len(L) > 2:
          for i in range(len(L)-2):
               if L[i] != L[i+1] and L[i+1] != L[i+2]:
                    return True
          if L[-1] != L[-2]:
               return True
               
     if len(L) == 1:
          return True
     elif len(L) == 2:
          if L[0] == L[1]:
               return False
     return False

# QUESTION 3
     
def all_unique(L):
     ''' (list,int)->list
     Return a list of elements of L that appear exactlly once in L. 
     Precondition: L is not empty
    
     >>> all_unique([2, 2,2, 2, 8])
     [8]
     >>> all_unique([1,-20,-1])
     [-20,-1,,1]
     >>> all_unique([3,2,2,3,3])
     []
     >>> all_unique([10])
     [10]
     >>> all_unique([10,10])
     []
     >>> all_unique([10,-1])
     [-1,10]
     '''
     l = []
     sorted(L)
     if len(L) > 2:
          if L[0] != L[1]:
               l.append(L[0])
          for i in range(len(L)-2):
               if L[i] != L[i+1] and L[i+1] != L[i+2]:
                    l.append(L[i+1])
          if L[-2] != L[-1]:
               l.append(L[-1])
     return l

# QUESTION 1 again

def element_uniqueness_v2(L):
     # make now a 2nd solution to element_uniqueness
     # by making a call to all_unique
     if len(all_unique(L)) == len(L):
          return True
     return False

# QUESTION 2 again

def one_unique_at_least_v2(L):
     # make now a 2nd solution to one_unique_at_least_v2
     # by making a call to all_unique
     if len(all_unique(L)) != 0:
          return True
     return False

# QUESTION 4

def count_unique(L):
     '''(list,int)->int
     Return the number of unique elements of L,
     i.e. the number of elements that appear exactlly once in L
     Precondition: L is not empty
    
     >>> count_unique([2, 2,2, 2, 8])
     1
     >>> count_unique([1,-20,-1])
     3
     >>> count_unique([3,2,2,3,3])
     0
     >>> count_unique([10])
     1
     >>> count_unique([10,10])
     0
     >>> count_unique([10,-1])
     2
     '''
     l = []
     L.sort
     if len(L) > 2:
          if L[0] != L[1]:
               l.append(L[0])
          for i in range(len(L)-2):
               if L[i] != L[i+1] and L[i+1] != L[i+2]:
                    l.append(L[i+1])
          if L[-2] != L[-1]:
               l.append(L[-1])
     return len(l)


# QUESTION 5                               

def duplicates(L):
     ''' (list)->int
     Returns True if the given list L has duplicates, in other,
     if it has at least one element that appears two or more times.
     Precondition: L is not empty

     >>> duplicates([2, 2,2, 2, 8])
     True
     >>> duplicates([1,-20,-1])
     False
     >>> duplicates([3,2,2,3,3])
     True
     >>> duplicates([10])
     False
     >>> duplicates([10,10])
     True
     >>> duplicates([10,-1])
     False
     '''
     if len(all_unique(L)) == len(L):
          return False
     return True
 

# QUESTION 6

def majority(L):
     '''(list)->
     An element of a list is called "majority" if MORE THAN half of the elements of the list are equal to it.
     This function returns the majority element of L if such an element exsits, otherwise it returns None
     >>> majority([2,1,2])
     2
     >>> majority([10,5,1,5,5])
     5
     >>> majority([5,5,1,1])
     
     >>> majority([3])
     3
     >>> majority([8,8,2,8])
     8
     '''

     count = 0
     for e in L:
          if count != 0:
               count += 1 if candidate == e else -1
          else: 
               candidate = e
               count = 1

     return candidate if L.count(candidate) > len(L) // 2 else default
               
