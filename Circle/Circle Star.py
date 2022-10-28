from turtle import*
import turtle
t=turtle.Turtle()
t.speed(4500)
t.color('cyan')
t.screen.bgcolor('black')

def square(tf,left,r):
	f=60
	for i in range(r):
		t.fd(f)
		t.left(tf)
		t.fd(f)
		t.left(tf)
		t.fd(f)
		t.left(tf)
		t.fd(f)
		t.left(left)
square(30,130,90)
		
turtle.done()
