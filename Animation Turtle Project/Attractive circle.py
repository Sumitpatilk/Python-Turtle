import turtle
turtle.bgcolor('red')

cppsecrets = turtle.Turtle()
cppsecrets.speed(0)

for i in range(180):
    cppsecrets.forward(100)
    cppsecrets.right(30)
    cppsecrets.forward(20)
    cppsecrets.left(60)
    cppsecrets.forward(50)
    cppsecrets.right(30)
    cppsecrets.penup()
    cppsecrets.setposition(0,0)
    cppsecrets.pendown()
    cppsecrets.right(2)
    turtle.done