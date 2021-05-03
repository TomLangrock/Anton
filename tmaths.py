class line:
    def __init__(self,xstart,ystart,xstop,ystop):
        self.xstart = xstart
        self.ystart = ystart
        self.xstop = xstop
        self.ystop = ystop
    
    def __repr__(self):
        repr = "(("
        repr += str(self.xstart) + ", " 
        repr += str(self.ystart) + "), (" 
        repr += str(self.xstop) + ", " 
        repr += str(self.ystop) + "))"
        return repr

class ray:
    def __init__(self, p, r , turtle):
        self.p = p
        self.r = r
        self.turtle = turtle

    def __repr__(self):
        return str(self.p) + " " + str(self.r)
    
    def intersectsWithLinesegment(self, linesegment):
        num = self.r[1]*(linesegment.xstart - self.p[0])+self.r[0]*(self.p[1]-linesegment.ystart) 
        denom = self.r[1]*(linesegment.xstart - linesegment.xstop)+self.r[0]*(linesegment.ystop-linesegment.ystart)
        if denom != 0:
            v = num/denom
        else:
            v = 0.5

        if 0 < v < 1:
            self.turtle.goto(linesegment.xstart + v*(linesegment.xstop-linesegment.xstart), linesegment.ystart + v*(linesegment.ystop-linesegment.ystart) )
            self.turtle.pencolor("red")
            self.turtle.dot()
    
    def updateRayDirection(self, x, y):
        self.r[0] = x - self.p[0]
        self.r[1] = y - self.p[1]