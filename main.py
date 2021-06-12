from turtle import Turtle, Screen
import random
screen = Screen()
# initalize players/ position / color
jeff = Turtle()
jeff.shape("turtle")
jeff.color("red")
jeff.penup()
jeff.setx(-50)
jeff.back(300)
jeff.pendown()

paul = Turtle()
paul.shape("turtle")
paul.color("green")
paul.penup()
paul.setx(-50)
paul.sety(50)
paul.back(300)
paul.pendown()

scott = Turtle()
scott.shape("turtle")
scott.color("purple")
scott.penup()
scott.setx(-50)
scott.sety(100)
scott.back(300)
scott.pendown()

dre = Turtle()
dre.shape("turtle")
dre.color("orange")
dre.penup()
dre.setx(-50)
dre.sety(150)
dre.back(300)
dre.pendown()

kevin = Turtle()
kevin.shape("turtle")
kevin.color("yellow")
kevin.penup()
kevin.setx(-50)
kevin.sety(-50)
kevin.back(300)
kevin.pendown()


kelly = Turtle()
kelly.shape("turtle")
kelly.color("blue")
kelly.penup()
kelly.setx(-50)
kelly.sety(-100)
kelly.back(300)
kelly.pendown()

move = random.randint(10,20)




#initialize screen

screen.exitonclick()