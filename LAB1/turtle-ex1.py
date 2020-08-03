import turtle 
s=turtle.Screen() 
t=turtle.Turtle() 

#move the pen
t.pensize(10)
t.penup()
t.goto(0, -10)
t.pendown()

# draw the circle, i.e. circle of radius 10  
t.circle(10)

#move the pen
t.penup()
t.goto(0, -25)
t.pendown()

# draw the circle, i.e. circle of radius 25  
t.circle(25)

#move the pen
t.penup()
t.goto(0, -50)
t.pendown()

# draw the circle, i.e. circle of radius 50  
t.circle(50)

#move the pen
t.penup()
t.goto(0, -75)
t.pendown()

# draw the circle, i.e. circle of radius 75  
t.circle(75)

#move the pen
t.penup()
t.goto(0, -100)
t.pendown()

# draw the circle, i.e. circle of radius 100  
t.circle(100)

#move the pen
t.penup()
t.goto(0, 175)
t.pendown()

#draw line
t.goto(0, -175)

#move the pen
t.penup()
t.goto(-175, 0)
t.pendown()

#draw line
t.goto(175, 0)

#move the pen
t.penup()
t.goto(-125, -125)
t.pendown()

#draw line
t.goto(125, 125)

#move the pen
t.penup()
t.goto(-125, 125)
t.pendown()

#draw line
t.goto(125, -125)

s.exitonclick()