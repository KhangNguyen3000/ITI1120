import math
import turtle

'''
Created on Sep 21, 2017

@author: KhangNguyen
'''
###################################################################
# Question 1
################################################################### 
def mh2kh(s):
    '''
    (number)->number
    returns the speed expressed in kilometres/hour from mile/hour
    '''
    return (s * 1.60934)

###################################################################
# Question 2
################################################################### 
def pythagorean_pair(a,b):
    '''
    (number,number)->boolean
    takes two integers a and b as input and returns
    True if a and b are pythagorean pair and False otherwise
    Precondition: a and b must be integers
    '''
    return ((math.sqrt(abs(a)**2 + abs(b)**2)).is_integer())

###################################################################
# Question 3
################################################################### 
def in_out(xs,ys,side):
    '''
    (number,number)->boolean
    takes three numbers as input, where Here xs and ys represent the x and y 
    coordinates of the bottom left corner of a square; and side represents the
    length of the side of the square
    function prompts the user to enter two numbers that represent the x
    and y coordinates of some query point. print True if the given
    query point is inside of the given square, otherwise print False.
    Precondition: side must be a positive number
    '''
    x = float(input("Enter a number for the x coordinate of a query point: "))
    y = float(input("Enter a number for the y coordinate of a query point: "))
    print((xs <= x <= (xs + side)) and (ys <= y <= (ys + side)))
    
###################################################################
# Question 4
###################################################################
def safe(n):
    '''
    (number)->boolean
    The function determines if n is a safe number. A number is not
    safe if it contains a 9 as a digit, or if it can be divided by 9. The 
    function should test if n is safe and return True if n is safe and False
    otherwise.
    Precondition: n is non negative and has a max of 2 digits
    '''
    return not("9" in str(n) or n%9 == 0)

###################################################################
# Question 5
###################################################################
def quote_maker(quote, name, year):
    '''
    (string, string, string )->string
    returns a string of the following form: In year, a person called 
    name said: “quote.”
    '''
    return('In '+str(year)+', a person called '+str(name)+' said: “'+str(quote)+'”')

###################################################################
# Question 6
###################################################################
def quote_displayer():
    '''
    (string, string, string )->None
    prompts the user for a quote, name,
    and year. The function then prints a sentence using the same format 
    as specified in the previous question.
    '''
    quote = input("Give me a quote: ")
    name = input("Who said that? ")
    year = input("What year did she/he say that? ")
    print(quote_maker(quote, name, year))

###################################################################
# Question 7
###################################################################
def rps_winner():
    '''
    (None)->None
    prompts the user for choice of player 1 and then choice of
    player 2, and then it displays the result for player 1.
    If both players make the same choice, we have a draw. 
    Precondition: words must be rock paper or scissors
    '''
    print("What choice did player 1 make?")
    p1 = input("Type one of the following options: rock, paper, scissors: ")
    print("What choice did player 2 make?")
    p2 = input("Type one of the following options: rock, paper, scissors: ")
    print("Player 1 wins. That is "+str((p1 == "rock" and p2 == "scissors")or\
                                        (p1 == "paper" and p2 == "rock")or\
                                        (p1 == "scissors" and p2 == "paper")))
    print("It is a tie. That is not "+str(p1 != p2))
    
###################################################################
# Question 8
###################################################################
def fun(x):
    '''
    (number)->number
    input a positive number x and solves
    the following equation for y and returns y. The equation is 104y=x+3. 
    Precondition: x must be a positive number
    '''
    return ((math.log(x + 3, 10))/4)

###################################################################
# Question 9
###################################################################
def ascii_name_plaque(name):
    '''
    (string)->None
    takes an input string
    representing a person’s name and draws a name plaque
    '''
    length = len("* __"+name+"__ *")
    print("*"*length+"\n*"+(" "*(length - 2))+"*"+"\n* __"+name+"__ *"+"\n*"+\
          (" "*(length - 2))+"*\n"+"*"*length)

###################################################################
# Question 10
###################################################################
def draw_bike():
    '''
    (None)->None
    draws the bike with Turtle graphics
    '''
    s=turtle.Screen() 
    t=turtle.Turtle()
    t.ht()
    
    t.pensize(7)
    t.pu()
    t.color("blue")   
    t.pu()
    t.goto(85, -50)
    t.dot(30, "black")
    t.dot(25, "grey")    
    t.goto(85,-100)
    t.color("grey")
    t.pensize(5)
    t.pd()
    t.circle(50)
    t.pu()    
    t.goto(-100,-100)
    t.color("grey")
    t.pd()
    t.circle(50)
    t.pu()
    t.pensize(7)
    t.color("blue")    
    t.goto(-100,-50)
    t.pd()
    t.goto(-40,30)
    t.goto(70,30)
    t.goto(70,50)
    t.pu()
    t.goto(50,55)
    t.color("tan")
    t.pd()
    t.goto(90,45)
    t.pu()
    t.goto(70,30)
    t.color("blue")
    t.pd()
    t.goto(-20,-60)
    t.goto(-100,-50)
    t.pu()
    t.goto(-20,-60)
    t.pd()
    t.goto(-40,52.5)
    t.pu()
    t.goto(-55,52.5)
    t.color("brown")
    t.pd()
    t.goto(-30,52.5)
    t.pu()
    t.goto(70,30)
    t.color("blue")
    t.pd()
    t.goto(70,-35)
    t.goto(85,-50) 
    t.pu()
    t.goto(-100, -50)
    t.dot(30, "black")
    t.dot(25, "grey") 
    t.color("black")
    t.pensize(6)
    t.pu()
    t.goto(-20, -60)
    t.pd()
    t.goto(-10,-30)
    t.goto(-15,-30)
    t.goto(-5,-30)
    t.pu() 
    t.goto(-20, -60)
    t.dot(40, "black")
    t.dot(35, "grey") 
    t.pu()
    t.goto(-20, -60)
    t.pd()
    t.goto(-30,-95)
    t.goto(-35,-95)
    t.goto(-25,-95)
    t.pu()
    t.goto(-20, -60)
    t.dot(20, "black")
    t.dot(15, "white")
    s.exitonclick()
    
###################################################################
# Question 11
###################################################################
def alogical(n):
    '''
    (number)->number
    returns the minimum number of times that n needs to be
    divided by 2 in order to get a number equal or smaller than 1.
    Precondition: n must be bigger or equal to 1
    '''
    return (math.ceil(math.log(n,2)))

###################################################################
# Question 12
###################################################################
def time_format(h,m):
    '''
    (number, number)->string
    takes a time of day, expressed in hours, h (integer 0 to 23) and minutes, m
    (integer 0 to 59). The function first rounds the minutes to the nearest 5 
    minutes, and then returns the time as descriptive string.
    '''
    m = 5 * (round(m / 5))
    if m == 60:
        m = 0
        h = h + 1
        
    while h >= 24:
        h = h - 24
        
    strt = ("half past "+str(h)+"o'clock")
    
    if m == 0:
        strt = (str(h)+" o'clock")
    elif m > 30:
        strt = (str(60 - m)+" minutes to "+str(h+1)+" o'clock")
    else:
        strt =(str(m)+" minutes past "+str(h)+" o'clock")
    return strt

###################################################################
# Question 13
###################################################################
def cad_cashier(price,payment):
    '''
    (number, number)->number
    takes two numbers as input, where the second decimal in payment is 0 or 5. 
    They represent a price and payment in Canadian dollars. The function returns
    a real number with 2 decimal places representing the change the customer 
    should get in Canadian dollars.
    '''
    return round((.05 * (round((payment - price) / .05))),2)

###################################################################
# Question 14
###################################################################
def min_CAD_coins(price,payment):
    '''
    (number, number)->(number, number, number)
    returns five numbers that represent the smallest number of coins that 
    add up to the amount owed to the customer (toonies, loonies, quarters,
    dimes, and nickels)
    '''
    change = int(cad_cashier(price,payment)*100)
    toonie = change//200
    change = change - toonie*200
    loonie = change//100
    change = change - loonie*100
    twofive = change//25
    change = change - twofive*25
    ten = change//10
    change = change - ten*10
    five = change//5
    return (toonie, loonie, twofive, ten, five)
