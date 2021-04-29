import turtle as t
from tmaths import line, ray
from random import randint

linesegments = []

bob = t.Turtle()
s = bob.getscreen()
s.tracer(4000,0)
s.bgcolor("black")

width = 1000
widthpanel = width//2
height = 400

s.setup(width,height)
s.setworldcoordinates(0,0,width, height)

xBox = 50
yBox = 50

minProgress = 20
maxProgress = 50

bob.hideturtle()

x = randint(0, xBox)
y = randint(0, yBox)
start = (x,y)
bob.penup()
bob.goto(x,y)
 


bob.fillcolor("white")
bob.begin_fill()
while bob.pos()[0] < widthpanel - xBox:
  xtemp = x
  ytemp = y
  x = randint(x + minProgress , x + maxProgress)
  y = randint(0, yBox)
  bob.goto(x,y)
  linesegments.append(line(xtemp,ytemp,x,y))

while bob.pos()[1] < height - yBox:
  xtemp = x
  ytemp = y
  x = randint(widthpanel  - xBox, widthpanel)
  y = randint(y + minProgress , y + maxProgress)
  bob.goto(x,y)
  linesegments.append(line(xtemp,ytemp,x,y))

while bob.pos()[0] > xBox:
  xtemp = x
  ytemp = y
  x = randint(x - maxProgress , x - minProgress)
  y = randint(height - yBox ,height)
  bob.goto(x,y)
  linesegments.append(line(xtemp,ytemp,x,y))

while bob.pos()[1] > 1.5*yBox:
  xtemp = x
  ytemp = y
  x = randint(0, xBox)
  y = randint(y - maxProgress , y - minProgress)
  bob.goto(x,y)
  linesegments.append(line(xtemp,ytemp,x,y))

linesegments.append(line(x,y,*start))
bob.goto(start)
bob.end_fill()



p = (widthpanel//2,height//2)
r = (1,0)
first = ray(p, r, bob)


s.clear()
s.bgcolor("black")
bob.goto(start)
bob.fillcolor("white")
bob.begin_fill()
for line in linesegments:
  bob.goto(line.xstart, line.ystart)
  first.intersectsWithLinesegment(line)
bob.end_fill()
s.update()

s.mainloop()