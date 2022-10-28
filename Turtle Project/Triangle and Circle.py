from re import A
from turtle import*
import turtle
 
a = turtle.Turtle()
Screen =turtle.Screen()
Screen.bgcolor('black')
col = ('red','yellow','green','blue','cyan')
a.speed(0)

for i in range(100):
    a.forward(i*4)
    a.right(91)
    a.color(col[i%5])

    for b in range(3):
        a.forward(i*4)
        a.right(91)
        a.circle(90)

        for c in range(2):
            a.forward(i*4)
            a.right(91)