from turtle import *

screen = Screen()
screen.bgcolor('black')

t = Turtle()
t.shape('turtle')
t.pensize(2)
t.pencolor('pink')

for x in range(100):
    t.forward(x*3)
    t.left(88)