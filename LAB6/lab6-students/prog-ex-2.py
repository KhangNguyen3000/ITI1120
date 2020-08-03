'''
asks the user for two integers (one by one
or at the same time if you know how to
handle it). Then it adds them and displays
the sum.
Then the user is asked to enter ‘yes’ if she
wishes to perform the operation again, and
otherwise if she enters anything other than
‘yes’ the program terminates. The operation
(described in the bullet above) is repeated,
as long as the user enters ‘yes’.
'''
x = "yes"
while ("yes") in x.lower():
    l = input("Enter 2 integers: ").split()
    c = int(l[0]) + int(l[1])
    print ("answer is,", c)
    x = input("Continue? ")
