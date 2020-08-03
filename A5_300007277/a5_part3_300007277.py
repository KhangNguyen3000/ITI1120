def digit_sum(n):
    '''(Integer)->Integer
    Takes an integer and sums each digit of the number'''
    if n == 0:
        return 0
    else:
        return (n%10) + digit_sum(n//10)
    
def digital_root(n):
    '''(Integer)->Integer
    Takes an integer and sums each digit then restarts till its 1 digit'''
    if len(str(n)) == 1:
        return n
    else:
        return digital_root(digit_sum(n))
