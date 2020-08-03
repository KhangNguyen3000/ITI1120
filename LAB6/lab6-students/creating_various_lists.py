import math
import random

n=int(input("Enter a positive even integer for the size of the list?" ))
a = [0]*n
print("1.",a)
b = random.sample(range(1,100),n)
print("2.",b)
i = 0
a = []
while i in range(n):
    a = a+[0]
    i = i + 1

print("1.",a)
b =[]
i = 0
while i in range(n):
    b = b+[random.randrange(1,100)]
    i = i + 1

b=[None]*n

print("2.",b)
c = b
print("3.",c)
c[:n//2] = [0]*(n//2)
print ("4.",c)

d = b
print("5.",d)

d = []
i = 0
while i in range(n):
    d = d+[b[i]]
    i = i + 1
print("5.", d)

e = []
i = 0
while i in range(n):
    e = e+[b[i]]
    i = i + 2
print("6.",e)
