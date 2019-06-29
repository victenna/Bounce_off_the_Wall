import turtle
import time
wn=turtle.Screen()
wn.setup(800,800)
wn.bgcolor('red')
turtle.tracer(2)
t=turtle.Turtle()
image='python.gif'
wn.addshape(image)
t.shape(image)
class Motion(turtle.Turtle):
     def __init__(self,color,direction):
        super().__init__()
        self.up()
        self.shape('square')
        self.shapesize(5)
        self.color(color)
        self.setheading(direction)
clr=['white','gold','blue','green',\
     'pink','yellow','violet','grey']
square=[0,0,0,0,0,0,0,0]
for i in range(8):
    square[i]=Motion(clr[i],i*45)
q=-1
q2=1
while True:
    time.sleep(0.05)
    q=q+1
    q1=q%50
    if q1==49:
        q2=q2*(-1)
    for i in range(8):
        square[i].fd(3*q2)
    
    
        
    
