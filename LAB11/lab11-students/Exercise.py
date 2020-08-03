def m(i):
    if i == 1:
        return 1/3
    else:
        return i/(2*i+1) + (m(i-1))

for i in range (1,11):
    print ("m("+str(i)+")","=",m(i))

def count_digits(n):
    if len(str(n)) == 1:
        return 1
    else:
        return (1 + count_digits(n//10))

def is_palindrome(s):
    if len(s) < 2:
        return True
    if s[0].lower() != s[-1].lower():
        return False
    return is_palindrome(s[1:-1])

def is_palindrome_v2(s):
    if len(s) < 2:
        return True
    elif s[0].isalpha() == True and s[-1].isalpha() == True:
        if s[0].lower() != s[-1].lower():
            return False
        return is_palindrome_v2(s[1:-1])
    elif s[0].isalpha() == True and s[-1].isalpha() == False:
        return is_palindrome_v2(s[:-1])
    elif s[0].isalpha() == False and s[-1].isalpha() == True:
        return is_palindrome_v2(s[1:])
    else:
        return is_palindrome_v2(s[1:-1])

def gcd(a,b):
    if b == 0:
        return a
    return(gcd(b, (a%b)))
