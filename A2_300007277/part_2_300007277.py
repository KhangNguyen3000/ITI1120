#Khang Nguyen
#300007277

def min_enclosing_rectangle(radius, x, y):
    '''(float/int, float/int)->int/float/None
has 3 input parameters. The first is a number representing a radius of a circle and the next two are two numbers
representing the x- and y-coordinates of its center. Consider the smallest axis-aligned rectangle that contains that circle.
The function should return the x- and y-coordinates of the bottom-left corner of that rectangle
'''
    if radius >= 0:

        return ((x-radius),(y-radius))

def series_sum():
        '''(None)-> int/float
prompts the user for an non-negative integer n. If the user enters a negative
integer the function should return None otherwise the function should return the sumer of the following series 1000 +
1/1
2 + 1/2
2 + 1/3
2 + 1/4
2 + ... + 1/n2
for the given integer n. 
'''
        x = int(input("Please enter a non-negative integer: "))
        if x>= 0:
            c = 0
            for i in range (x):
                c = c + (1/(i+1)**2)
            return(1000+c)

def pell(n):
    '''
(int)-> int
takes one integer parameter n, of type int. If n is negative, pell returns None. Else,
pell returns the nth Pell number
'''
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n>1:
        l = [0,1]
        for i in range(n-1):
            l.insert((i+3),(2*l[i+1] + l[i]))
        return l[-1]
    
        
def countMembers(s):
    '''
(String) -> int
takes a single input parameter s, of type str. countMembers then returns
the number of characters in s, that are extraordinary
y a character is extraordinary if it is one of the following: the lower case letter between e and j (inclusive), the upper
case letters between F and X (inclusive), numerals between 2 and 6 (inclusive), and the exclamation point (!), comma (,),
and backslash (\)

'''
    l = list(s)
    n = list("efghijFGHIJKLMNOPQRSTUVWX23456!,\\")
    c = 0
    for i in range(len(s)):
        for a in range(len(n)):
            if l[i] == n[a]:
                c = c+1
    return (c)
    
def casual_number(s):
    '''
(String) -> int/None
Imagine a customer in a bank is asked to enter a whole number representing their approximate monetary worth. In that
case, some people use commas to separate thousands, millions etc, and some don’t. In order to perform a some calculations
the bank needs that number as na integer. Write a function, called casual_number(s) that has one parameter, s, as
input where s is a string. Function casual_number(s) should return an integer representing a number in s. If s does not
look like a number the function should return None
'''
    l = list(s)
    n = list("1234567890")
    c= ""
    for i in range(len(s)):
        t = False
        for a in range(len(n)):
            if l[i] == "-" and i == 0 and a == 0 and len(s) > 1:
                c = c+l[i]
                t = True
            elif l[i] == n[a]:
                c = c+l[i]
                t = True
            elif l[i] == ",":
                if l[i-1] != "," or l[i+1] != ",":
                    t = True
                else:
                    t = False
        if t == False:
                return None
    return int(c)
def alienNumbers(s):
    '''
(String) -> int
 They have symbols for various numeric values, and they just add all the
values for the symbols in a given numeral to calculate the number. NASA’s linguists have given you the following table of
symbols and their numeric values. Since they have a lot of these numbers to compute, they want you to write a function
that they can use to automate this task.
'''
    l = list(s)
    return (l.count("T")*1024 + l.count("y")*598 + l.count("!")*121 + l.count("a")*42 + l.count("N")*6 + l.count("U"))
    
def alienNumbersAgain(s):
    '''
(String) -> int
takes a single string parameter s, and returns the numeric value of
the number that s represents in the alien numbering system.
NASA is very pleased with your proof-of-concept solution in the previous question. Now, they’ve designed a small chip
that runs a very restricted version of python - it doesn’t have any of the string methods that you are used to.
'''
    l = list(s)
    n = list("Ty!aNU")
    m = [1024,598,121,42,6,1]
    c = 0

    for i in range(len(s)):
        for a in range(len(n)):
            if l[i] == n[a]:
                c = c+ m[a]
    return c

def encrypt(s):
    '''
(String) -> String
 has one parameter s where s is a string and encrypt
returns a string which isthe encrypted version of s.s how it works: you write out your message backwards (so, Hello,5
world becomes dlrow ,olleH). But you don’t stop there, because that’s too easy to crack - anyone can figure that out!
Now that you’ve written in backwards, Then you start on either side of the string and bring the characters together. So
the first and the last characters become the first and the second character in the encrypted string, and the second and
the second last characters become the third and the fourth characters in the string, and so on. Thus, Hello, world
ultimately becomes dHlerlolwo
'''
    l = list(s)
    c = ""
    for i in range(len(s)//2):
        c = c + l[-(i+1)] + l[i]
    if len(s)%2 != 0:
       c = c + l[(len(s)//2)]
    return c

def oPify(s):
    '''
(String) -> String
takes a single string parameter (s) and returns a string. This function considers
every pair of consecutive characters in s. It returns a string with the letters o and p inserted between every pair of
consecutive characters of s, as follows. If the first character in the pair is uppercase, it inserts an uppercase O. If however,
it is lowercase, it inserts the lowercase o. If the second character is uppercase, it inserts an uppercase P. If however, it
is lowercase, it inserts the lowercase p. If at least one of the character is not a letter in the alphabet, it does not insert
anything between that pair. Finally, if s has one or less characters, the function returns the same string as s
'''
    l = list(s)
    c = l[0]

    if len(s)<2:
        c = s
    else:
        for i in range(len(s)-1):
            if (l[i].isalpha() == False or l[i+1].isalpha() == False):
                c = c + l[i+1]
            else:
                if(l[i].isupper() == True):
                    c = c + "O"
                else:
                    c = c + "o"
                if(l[i+1].isupper() == True):
                    c = c + "P" + l[i+1]
                else:
                    c = c + "p" + l[i+1]
    return c

def nonrepetitive(s):
    '''
(String) -> boolean
Write a function, called nonrepetitive, that has one parameter, s, where s is a string. The function returns True if
s is nonrepetitive and False otherwise
'''
    l = list(s)
    for i in range(1,len(s)):
        for a in range(len(s)-(i)):
            print(l[a:a+i], l[a+(i):(a+(i+1)+(i-1))])
            if l[a:a+i] == l[a+(i):(a+(i+1)+(i-1))]:
                return False
    return True
