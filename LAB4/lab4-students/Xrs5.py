

def stuff(x):
    '''
    (int)-> None
    asks a user for a positive integer and then prints all the
divisors of the given integer
    '''
    for i in range(x):
        if (x%(i+1)) == 0:
            print ((i+1), end = ", ")

    print()

def prime(x):
    '''
    (int) -> None
    asks a user for a positive integer and then prints if it is a prime
    number
    '''
    for (i) in range(x):
        a = str(x)
        if x == 1:
            print(a+" is not a prime number")
            return
        if (x%(i+1)) == 0:
            print(str(i+1))
            if (i+1) != 1 and (i+1) != (x):
                print(a+" is not a prime number")
                return

    print(a+" is a prime number")

    

x  = int(input("insert non negative number "))
stuff(x)
