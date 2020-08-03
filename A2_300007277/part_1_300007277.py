#Khang Nguyen
#300007277
import math
import random


def primary_school_quiz(flag, n):
    '''
    (int, int)-> int
    If flag is 0, helps practice subtraction. But if flag is 1,helps practice exponentiation
    generates n math problems that must be answered. For each question, it generates two random positive, single-digit numbers
    and asks for the answer to the math problem with those two numbers. checks if the answer is correct. At the
    end of n questions, returns the number of questions answered correctly.

    '''
    c = 0
    if flag == 0:
        for i in range(n):
            x = random.randrange(1,10)
            y = random.randrange(1,10)
            print("Question "+str(i)+":")
            z = int(input("What is the result of "+str(x)+" - "+str(y)+"? "))
            if z == (x-y):
                c = c + 1
            
    elif flag == 1:
        for i in range (n):
            x = random.randrange(1,10)
            y = random.randrange(1,10)
            print("Question "+str(i)+":")
            z = int(input("What is the result of "+str(x)+" ^ "+str(y)+"? "))
            if z == (x**y):
                c = c + 1
    
    return c    


def high_school_eqsolver(a,b,c):
    '''
    (float,float,float) -> None
    This function has three parameters representing three real numbers for the coefficients of the
    quadratic equation ax2 + bx + c = 0. The function displays/prints the equation first and then prints its solutions
    '''
    if (b**2) - (4*a*c) < 0:
        x = (math.sqrt(-((b**2) - (4*a*c))))/(2*a)
        print("The quadratic equation \n"+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" \nhas the following complex roots: \n"+str(-b/(2*a))+" + "+" i *"+str(x)+"\n and\n"+str(-b/(2*a))+" - "+" i *"+str(x))
        
    else:
        x = (-b+math.sqrt((b**2) - (4*a*c)))/(2*a)
        y = (-b-math.sqrt((b**2) - (4*a*c)))/(2*a)
        print("The quadratic equation \n"+str(a)+"x^2 + "+str(b)+"x + "+str(c)+" \nhas the following real roots: \n"+str(x)+" and "+str(y))



# main

print('''*************************************************************
*                                                           *
*  __Welcome to my math quiz-generator / equation-solver__  *
*                                                           *
*************************************************************\n''')

name=input("What is your name? ")
status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    length = len("*  __"+name+", welcome to my quiz-generator for primary school students.__  *")
    print("*"*length+"\n*"+(" "*(length - 2))+"*"+"\n*  __"+name+", welcome to my quiz-generator for primary school students.__  *"+"\n*"+\
          (" "*(length - 2))+"*\n"+"*"*length)
    print('')
           
    x = int(input("Enter \n0 to practice substractions or \n1 to practice exponentials\n"))
    y = int(input("How many questions would you like to do? : "))
    c = primary_school_quiz(x, y)
    if c/y >= .90:
        print("Congratulations "+name+"! You’ll probably get an A tomorrow. Now go eat your dinner and go to sleep.")
    elif c/y >= .70:
        print("You did well "+name+", but i know you can do better.")
    else:
        print("I think you need more practice "+name+".")        
        

elif status=='2':
    
    length = len("*  __quadratic equation, a·x^2 + b·x + c= 0, solver for "+name+"__  *")
    print("*"*length+"\n*"+(" "*(length - 2))+"*"+"\n*  __quadratic equation, a·x^2 + b·x + c= 0, solver for "+name+"__  *"+"\n*"+\
          (" "*(length - 2))+"*\n"+"*"*length)
    print('')
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        if "yes" in question.lower():
            question = "yes"

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            x = float(input("Enter a number the coefficient a: "))
            y = float(input("Enter a number the coefficient b: "))
            z = float(input("Enter a number the coefficient c: "))
            high_school_eqsolver(x,y,z)
 
else:
    print (name+" you are not a target audience for this software.")
    pass

print("Good bye "+name+"!")
