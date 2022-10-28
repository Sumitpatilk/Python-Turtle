
# import turtle

# def Cppsecrets (python, cplusplus):
#         if python >0:
#          turtle.forward(python)
#         turtle.right(cplusplus)
#         Cppsecrets(python-5,cplusplus)

#         turtle.shape('turtle')
#         turtle.color('black')
#         turtle.reset()
#         turtle.pen(speed=1)
#         turtle.delay(0)
#         length =400
#         turn_by =121
#         turtle.penup()
#         turtle.setpos(-length/2,length/2)
#         turtle.pendown()
#         Cppsecrets(length,turn_by)
     

import turtle

cppsecrets =turtle.Screen()
cppsecrets.title('Animation Circle')
turtle.color('red')
turtle.speed(0)
turtle.hideturtle()

for i in range(100):
      turtle.circle(i*2)
      turtle.bgcolor('black')
      turtle.right(400)

      
      
      

   
       