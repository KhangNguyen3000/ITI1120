def prime(x):
    '''
    (int) -> None
    asks a user for a positive integer and then prints if it is a prime
    number
    '''
    for i in range(x):
        a = str(x)
        if (x%(i+1)) == 0:
            if (i+1) != 1 or (i+1) != (i+1):
                print(a+" is not a prime number")
                return

    print(a+" is a prime number")