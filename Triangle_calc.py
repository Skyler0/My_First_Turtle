#----Import Statments-----
import turtle as trtl
import math as m
import random as rand

#------config-----
a = "a"
b = "b"
c = "c"
speed = 0
font_setup = ("Arial", 20, "normal")
color = ['blue','green','red', 'purple', 'yellow', 'pink', 'cyan', 'teal']
#----turtle setup----
t = trtl.Turtle()
t.speed(speed)
t.color(rand.choice(color))
t.goto(0,100)
t.goto(0,0)
t.goto(100,0)
t.left(45)
t.goto(0,100)


side_a = trtl.Turtle()
side_a.hideturtle()
side_a.penup()
side_a.goto(-10,50)
side_a.color(rand.choice(color))
side_a.write(a, font=font_setup)

side_b = trtl.Turtle()
side_b.hideturtle()
side_b.penup()
side_b.goto(50,-20)
side_b.color(rand.choice(color))
side_b.write(b, font=font_setup)

side_c = trtl.Turtle()
side_c.hideturtle()
side_c.penup()
side_c.goto(55,45)
side_c.color(rand.choice(color))
side_c.write(c, font=font_setup)

writer1 = trtl.Turtle()
writer1.hideturtle()
writer1.penup()
writer1.goto(50,-50)
writer1.color(rand.choice(color))


writer2 = trtl.Turtle()
writer2.hideturtle()
writer2.penup()
writer2.goto(50,-70)
writer2.color(rand.choice(color))

writer3 = trtl.Turtle()
writer3.hideturtle()
writer3.penup()
writer3.goto(50,-90)
writer3.color(rand.choice(color))

wn = trtl.Screen()


#-----coding----

def missing_var():
    missing_var = wn.textinput("missing_leg or Hypotenuse? ", "What is the Missing Leg or Hypotenuse? ")
    if (missing_var == "a"):
        b = float(wn.textinput("b","What is b (Has to be greater than 0)?"))
        c = float(wn.textinput("c","What is c (Has to be greater than b)? "))
        a = m.sqrt((c * c) - (b * b))
        print(a)
        Area = (a*b)/2
        print(Area)
        Perimeter = a + b + c
        print(Perimeter)
        writer1.write("Missing leg =" + str(a), font=font_setup)
        writer2.write("Area =" + str(Area), font=font_setup)
        writer3.write("Perimeter =" + str(Perimeter), font=font_setup)
    if (missing_var == "b"):
        a = float(wn.textinput("a","What is a(Has to be greater than 0)? "))
        c = float(wn.textinput("c","What is c(Has to be greater than a)? "))
        b = m.sqrt((c * c) - (a * a))
        print(b)
        Area = (a*b)/2
        print(Area)
        Perimeter = a + b + c
        print(Perimeter)
        writer1.write("Missing leg =" + str(b), font=font_setup)
        writer2.write("Area =" + str(Area), font=font_setup)
        writer3.write("Perimeter =" + str(Perimeter), font=font_setup)
    if (missing_var == "c"):
        a = float(wn.textinput("a","What is a(Has to be greater than 0)? "))
        b = float(wn.textinput("b","What is b(Has to be greater than 0)? "))
        c = m.sqrt((a * a) + (b * b))
        print(c)
        Area = (a*b)/2
        print(Area)
        Perimeter = a + b + c
        print(Perimeter)
        writer1.write("Hypotenuse =" + str(c), font=font_setup)
        writer2.write("Area =" + str(Area), font=font_setup)
        writer3.write("Perimeter =" + str(Perimeter), font=font_setup)

#-------events----
missing_var()
wn.mainloop()