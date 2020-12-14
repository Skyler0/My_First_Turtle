import turtle as trtl

painter = trtl.Turtle()
painter.speed(1000)

#changes the pen size and color 
painter.pensize(2)
painter.pencolor('black')

#puts ground 
painter.goto(400,0)
painter.goto(-400,0)

#draws the base of the house which is a sqaure
painter.begin_fill()
painter.fillcolor('yellow')
painter.goto(50,0)
painter.goto(-50,0)
painter.goto(-50,100)
painter.goto(50,100)
painter.goto(50,0)
painter.end_fill()


#draws the doors 
painter.begin_fill()
painter.fillcolor('#0707e8')
painter.goto(10,0)
painter.goto(10,35)
painter.goto(-10,35)
painter.goto(-10,0)
painter.end_fill()

#draws the door knob
painter.penup()
painter.goto(5,13)
painter.pendown()
painter.begin_fill()
painter.fillcolor('white')
painter.circle(2)
painter.end_fill()

#draws the window
painter.penup()
painter.goto(-30,25)
painter.pendown()
painter.begin_fill()
painter.fillcolor('#a9eff5')
painter.goto(-40,25)
painter.goto(-20,25)
painter.goto(-20,50)
painter.goto(-40,50)
painter.goto(-40,25)
painter.end_fill()
painter.goto(-40,36)
painter.goto(-20,36)
painter.goto(-30,36)
painter.goto(-30,25)
painter.goto(-30,50)


#starts the roof of the house 
painter.penup()
painter.goto(50,100)
painter.pendown()
painter.begin_fill()
painter.fillcolor('black')
painter.goto(0,150)
painter.goto(-50,100)
painter.goto(0,100)
painter.end_fill()

#draws base of garage shell
painter.penup()
painter.goto(50,0)
painter.pendown()
painter.begin_fill()
painter.fillcolor('yellow')
painter.goto(200,0)
painter.goto(200,100)
painter.goto(0,100)
painter.end_fill()

#draws the garage door
painter.penup()
painter.goto(75,0)
painter.pendown()
painter.begin_fill()
painter.fillcolor('white')
painter.goto(75,75)
painter.goto(175,75)
painter.goto(175,0)
painter.end_fill()

#draws lines acrossed garage door
painter.penup()
painter.goto(75,0)
painter.pendown()
painter.goto(75,65)
painter.goto(175,65)
painter.penup()
painter.goto(75,0)
painter.pendown()
painter.goto(75,50)
painter.goto(175,50)
painter.penup()
painter.goto(75,0)
painter.pendown()
painter.goto(75,35)
painter.goto(175,35)
painter.penup()
painter.goto(75,0)
painter.pendown()
painter.goto(75,15)
painter.goto(175,15)


# makes the base of the tree
painter.penup()
painter.goto(-100,0)
painter.pendown()
painter.begin_fill()
painter.fillcolor('#964B00')
painter.goto(-100,100)
painter.goto(-150,100)
painter.goto(-150,0)
painter.goto(-100,0)
painter.end_fill()

#makes the leaves of the tree
painter.penup()
painter.goto(-125,100)
painter.pendown()
painter.begin_fill()
painter.fillcolor('#5ea307')
painter.circle(50)
painter.end_fill()

#makes the moon
painter.penup()
painter.goto(-300,200)
painter.pendown()
painter.begin_fill()
painter.fillcolor('white')
painter.circle(45)
painter.end_fill()
painter.penup()
painter.goto(-300,210)
painter.pendown()
painter.circle(10)









window = trtl.Screen()
window.bgcolor('#191970') #changes the color of my background to a night 
window.mainloop()