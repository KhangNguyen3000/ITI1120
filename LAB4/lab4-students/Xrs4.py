

x  = int(input("insert non negative number "))
str = input("Char to repeat: ")


for i in range(x):
    print(" "*((x) - i), end = str*((i+1)+(1*i)))
    print()