import turtle

turtle.bgcolor('black')
turtle.speed(60)

col =('Purple','Red','yellow','orange')

for i in range(100):
    turtle.forward(i*2)
    turtle.right(60)
    turtle.color(col[i%4])

    for a in range(100):
     turtle.forward(a*2)
     turtle.right(90)
     turtle.circle(200)