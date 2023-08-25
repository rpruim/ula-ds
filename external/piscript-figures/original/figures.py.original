from piscript.PiModule import *
from random import *

def setseed(s):
    seed(s)

white = 1
black = 0
gray = 0.5
lightlightgray = 0.9
lightgray = 0.8
darkgray = 0.2

blue = [0,0,1]
darkblue = [0,0,0.5]
medblue = [0.2, 0.2, 1]
lightblue = [0.5, 0.5, 1]
lightlightblue = [0.8, 0.8, 1]

red = [1,0,0]
darkred = [0.5, 0, 0]
medred = [1, 0.2, 0.2]
lightred = [1, 0.5, 0.5]
lightlightred=[1,0.8,0.8]
kindalightred = [1, 0.1, 0.1]

green = [0,1,0]
darkgreen = [0, 0.5, 0]
lightgreen = [0.5, 1, 0.5]
meddarkgreen = [0, 0.6, 0]

cyan = [0,1,1]
darkcyan = [0, 0.5, 0.5]

magenta = [1, 0, 1]
darkmagenta = [0.5, 0, 0.5]
lightmagenta = [1, 0.5, 1]

yellow = [1,1,0]
darkyellow = [0.5, 0.5, 0]
orange = [1, 0.5, 0]
darkorange=[0.5,0.25,0]
lightorange=[1,0.75, 0.25]

gold = [207/255.0, 181/255.0, 59/255.0]

## add some defaults
graphcolor = 0
graphwidth = 1
gridcolor = lightgray
gridwidth = 1
sizeofaxeshticks = 4
sizeofaxesvticks = 4
scaleofaxeshlabels = 1
scaleofaxesvlabels = 1

def setHtickSize(ts):
    sizeofaxeshticks = ts
    

bbox = []
def beginfigure(s, width, height):
    init(s, width, height)
    beginpage()
    settexenv('ACTexConfig')
    clip()
    newpath()

def endfigure():
    endpage()
    finish()

def setupcoordinates(*args):
    global bbox
    if len(args) == 1:
        pbox = [0, 0, width(), height()]
        mbox = args[0]
    else:
        pbox = args[0]
        mbox = args[1]
    bbox = mbox
    translate(pbox[0], pbox[1])
    scale( (pbox[2]-pbox[0])/float(bbox[2]-bbox[0]),
           (pbox[3]-pbox[1])/float(bbox[3]-bbox[1]) )
    translate(-bbox[0], -bbox[1])
    
def cliptoboundingbox():
    newpath()
    box(bbox[0], bbox[1], bbox[2]-bbox[0], bbox[3]-bbox[1])
    clip()

def avg(points):
    s = [0]*len(points[0])
    for p in points:
        s = vsum(s,p)
    return smult(1/float(len(points)), s)

def lincomb(weights, vectors):
    sum = smult(weights[0], vectors[0])
    for i in range(1, len(vectors)):
        sum = vsum(sum, smult(weights[i], vectors[i]))
    return sum

def save():
    gsave()

def restore():
    grestore()

def isinbbox(p):
    if p[0] < bbox[0] or p[0] > bbox[2] or p[1] < bbox[1] or p[1] > bbox[3]:
        return False
    return True

def vdiff(u, v):
    r = []
    for i in range(len(u)):
        r.append(u[i] - v[i])
    return r
def vsum(u, v):
    r = []
    for i in range(len(u)):
        r.append(u[i] + v[i])
    return r

def dot(u,v):
    d = 0
    for i in range(len(u)):
        d += u[i]*v[i]
    return d
def smult(s, u):
    r = []
    for i in range(len(u)):
        r.append(s*u[i])
    return r
def pointonline(p0, t, p1):
    d = vdiff(p1, p0)
    return vsum(p0, smult(t, d))

def cross(p,q):
    return [p[1]*q[2]-p[2]*q[1],
            p[2]*q[0]-p[0]*q[2],
            p[0]*q[1]-p[1]*q[0]]

def bestfitline(x,y):
    N = len(x)
    xysum = 0
    x2sum = 0
    xsum = 0
    ysum = 0
    for i in range(N):
        xsum += x[i]
        ysum += y[i]
        x2sum += x[i]*x[i]
        xysum += x[i]*y[i]
    m = (N*xysum - xsum*ysum)/float(N*x2sum - xsum*xsum)
    b = (ysum - m*xsum)/N
    return [b,m]

class GeneralPath():
    def __init__(self):
        self.color = 0
        self.linewidth = 1
        self.currentpoint = False
        self.miterlimitset = False
        self.dash = None
    def moveto(self, p):
        moveto(p)
        self.currentpoint = True
    def lineto(self, p):
        lineto(p)
        self.currentpoint = True
    def curveto(self, p1, p2, p3):
        curveto(p1, p2, p3)
        self.currentpoint = True
    def quadto(self, p1, p2):
        quadto(p1, p2)
        self.currentpoint = True
    def closepath(self):
        closepath()
        self.currentpoint = True
    def setcolor(self, c):
        self.color = c
    def setlinewidth(self, w):
        self.linewidth = w
    def setmiterlimit(self, l):
        self.miterlimitset = True
        self.miterlimit = l
    def append(self, points):
        if self.currentpoint == False:
            moveto(points[0])
        else:
            lineto(points[0])
        for p in points:
            lineto(p)
    def newpath(self):
        newpath()
        self.currentpoint = False
    def stroke(self):
        gsave()
        setlinewidth(self.linewidth)
        if self.miterlimitset:
            setmiterlimit(self.miterlimit)
        if self.dash != None:
            setdash(self.dash)
        stroke(self.color)
        grestore()

class Line(GeneralPath):
    def __init__(self, p0, p1, color = 0, linewidth = 1, infinite = False,
                 dash = None):
        GeneralPath.__init__(self)
        self.color = color
        self.linewidth = linewidth
        self.p0 = p0
        self.p1 = p1
        self.infinite = infinite
        self.dash = dash
    def setinfinite(self, b):
        self.infinite = b
    def draw(self):
        t0 = 0
        t1 = 1
        if self.infinite:
            while isinbbox(pointonline(self.p0, t1, self.p1)):
                t1 += 1
            while isinbbox(pointonline(self.p0, t0, self.p1)):
                t0 -= 1
        newpath()
        moveto(pointonline(self.p0, t0, self.p1))
        lineto(pointonline(self.p0, t1, self.p1))
        self.stroke()

class Area(GeneralPath):
    def __init__(self):
        GeneralPath.__init__(self)
    def setfillcolor(self, c):
        self.fillcolor = c
    def fill(self):
        fill(self.fillcolor)

class Vector(Area):
    def __init__(self, p1, tail = [0,0], 
                 fillcolor = 0, color = 0, linewidth = 1, 
                 arrowwidth = 2, arrowdims = None):
        Area.__init__(self)
        self.p0 = tail
        self.p1 = p1
        self.fillcolor = fillcolor
        self.color = color
        self.linewidth = linewidth
        if arrowdims == None:
            self.arrowdims = [arrowwidth, 3*arrowwidth]
        else: self.arrowdims = arrowdims
    def outline(self):
        gs = revert()
        newpath()
        setarrowdims(self.arrowdims[0], self.arrowdims[1])
        arrow(gs.transform(self.p0), gs.transform(self.p1))
    def draw(self):
        gsave()
        self.outline()
        self.stroke()
        grestore()
    def fill(self):
        gsave()
        self.outline()
        fill(self.fillcolor)
        grestore()
    def shade(self):
        gsave()
        self.outline()
        fill(self.fillcolor)
        self.stroke()
        grestore()

class SlopeField(GeneralPath):
    def __init__(self, f, xrange, yrange,
                 color = 0, linewidth = 1, width = 0.25):
        GeneralPath.__init__(self)
        self.color = color
        self.linewith = linewidth
        self.width = width
        self.xrange = xrange
        self.yrange = yrange
        self.f = f
    def draw(self):
        x = self.xrange[0]
        import math
        newpath()
        gsave()
        setlinewidth(self.linewidth)
        while x <= self.xrange[2]:
            y = self.yrange[0]
            while y <= self.yrange[2]:
                slope = self.f(x,y)
                gsave()
                translate(x, y)
                setrad()
                rotate(math.atan(slope))
                moveto(-self.width/2., 0)
                lineto(self.width/2., 0)
                stroke(self.color)
                grestore()
                y += self.yrange[1]
            x += self.xrange[1]
        grestore()

def length(v):
    s = 0
    for i in range(len(v)):
        s += v[i]*v[i]
    return math.sqrt(s)

def vscale(s, v):
    r = []
    for i in range(len(v)):
        r.append(v[i]*s)
    return r

def normalize(v):
    return vscale(1/length(v), v)

def distance(u,v):
    return length(vdiff(u,v))

class DirectionField(GeneralPath):
    def __init__(self, f, xrange, yrange, lengths = [0,1],
                 color = 0, linewidth = 1, arrowwidth=0.2, 
                 arrowheight=0.8):
        GeneralPath.__init__(self)
        self.color = color
        self.linewith = linewidth
        self.lengths = lengths
        self.xrange = xrange
        self.yrange = yrange
        self.f = f
        setdeg()
        setarrowdims(arrowwidth, arrowheight, 50, 80)
    def draw(self):
        x = self.xrange[0]
        import math
        newpath()
        gsave()
        setlinewidth(self.linewidth)
        while x <= self.xrange[2]:
            y = self.yrange[0]
            while y <= self.yrange[2]:
                v = self.f(x,y)
                norm = length(v)
                if (norm < self.lengths[0]):
                    y += self.yrange[1]
                    continue
                if (norm > self.lengths[1]):
                    v = vscale(self.lengths[1]/norm, v)
                gsave()
                translate(x, y)
                setcolor(self.color)
#                print v, self.lengths[0]
                arrow(v)
                fill()
                grestore()
                y += self.yrange[1]
            x += self.xrange[1]
        grestore()

class Box(Area):
    def __init__(self, box, fillcolor = 0, color = 0, linewidth = 1):
        Area.__init__(self)
        self.fillcolor = fillcolor
        self.color = color
        self.linewidth = linewidth
        if box != "boundingbox":
            self.box = box
        else:
            self.box = [bbox[0], bbox[1], bbox[2]-bbox[0], bbox[3]-bbox[1]]
    def outline(self):
        newpath()
        box(self.box[0], self.box[1], self.box[2], self.box[3])
    def fill(self):
        self.outline()
        fill(self.fillcolor)
    def draw(self):
        self.outline()
        self.stroke()
        
class Polygon(Area):
    def __init__(self, points = [], 
                 fillcolor = 0, color = 0, linewidth = 1, closed = False,
                 dash = None):
        Area.__init__(self)
        self.fillcolor = fillcolor
        self.color = color
        self.linewidth = linewidth
        self.points = points
        self.closed = closed
        self.dash = dash
    def close(self):
        self.closed = True
    def addpoint(self, p):
        self.points.append(p)
    def addpoints(self, points):
        for p in points:
            self.addpoint(p)
    def outline(self):
        self.newpath()
        self.append(self.points)
        if self.closed:
            self.closepath()
    def draw(self):
        self.outline()
        self.stroke()
    def fill(self):
        self.outline()
        fill(self.fillcolor)

class Point(Area):
    def __init__(self, p, size = 2.5, color = 0, fillcolor = 0,
                 linewidth=1, style='CIRCLE'):
        Area.__init__(self)
        self.color = color
        self.fillcolor = fillcolor
        self.linewidth = linewidth
        self.x = p[0]
        self.y = p[1]
        self.r = size
        self.style = style
    def setpoint(self, p):
        self.x = p[0]
        self.y = p[1]
    def outline(self):
        gs = revert()
        translate(gs.transform(self.x,self.y))
        newpath()
        if self.style == 'CIRCLE':
            circle(0, 0, self.r)
        if self.style == 'DIAMOND':
            newpath()
            moveto(0,-self.r)
            lineto(self.r, 0)
            lineto(0,self.r)
            lineto(-self.r,0)
            closepath()
        if self.style == 'BOX':
            newpath()
            moveto(-self.r, -self.r)
            rlineto(2*self.r,0)
            rlineto(0,2*self.r)
            rlineto(-2*self.r,0)
            closepath()
    def draw(self):
        gsave()
        self.outline()
        self.stroke()
        grestore()
    def fill(self):
        gsave()
        self.outline()
        fill(self.fillcolor)
        grestore()

class Ellipse(Area):
    def __init__(self, center, axes, 
                 fillcolor = 0, color = 0, linewidth = 1, dash = None):
        Area.__init__(self)
        self.fillcolor = fillcolor
        self.color = color
        self.linewidth = linewidth
        self.center = center
        self.axes = axes
        self.dash = None
    def outline(self):
        translate(self.center)
        scale(self.axes[0], self.axes[1])
        circle(0,0,1)
    def draw(self):
        newpath()
        gsave()
        self.outline()
        self.stroke()
        grestore()
    def fill(self):
        newpath()
        gsave()
        self.outline()
        fill(self.fillcolor)
        grestore()

class Circle(Ellipse):
    def __init__(self, p, r, fillcolor = 0, color = 0, linewidth = 1,
                 dash = None):
        Ellipse.__init__(self, p, [r,r])
        self.fillcolor = fillcolor
        self.color = color
        self.linewidth = linewidth
        self.dash = dash

class Function():
    def __init__(self, f):
        self.f = f
        self.setup()
    def setup(self):
        self.dx = 0.0001
    def value(self, x):
        return self.f(x)
    def derivative(self, x):
        return (self.f(x+self.dx) - self.f(x-self.dx))/(2*self.dx)
    def secondderivative(self, x):
        return (self.f(x+self.dx) - 2*self.f(x) + self.f(x-self.dx))/(self.dx*self.dx)
    def differentiate(self):
        return Derivative(self)
    def antidifferentiate(self, a):
        return Antiderivative(self, a)
    def tangentline(self, a):
        return Function(lambda x : self.derivative(a)*(x-a) + self.value(a))
    def solve(self, x):
        n = 0
        while True:
            next = x - self.value(x)/float(self.derivative(x))
            if abs(next - x) < 0.000001 or n > 100:
                break
            x = next
            n += 1
        return x

class RiemannSum(Area):
    LEFT = 0
    MID = 1
    RIGHT = 2
    TRAP = 3
    RANDOM = 4
    def __init__(self, f, N, g = Function(lambda x:0), 
                 fillcolor = 0, color = 0, linewidth = 1,
                 style = 0, domain = None):
        Area.__init__(self)
        self.fillcolor = fillcolor
        self.color = color
        self.linewidth = linewidth
        self.f = f
        self.g = g
        self.N = N
        if domain == None:
            self.x0 = bbox[0]
            self.x1 = bbox[2]
        else:
            self.setdomain(domain)
        self.points = []
        self.style = style
        self.boxes = []
    def setdomain(self,d):
        self.x0 = d[0]
        self.x1 = d[1]
    def setstyle(self, s):
        self.style = s
    def setN(self, N):
        self.N = N
    def getboxes(self):
        h = (self.x1 - self.x0)/float(self.N)
        x = self.x0
        if self.style == RiemannSum.LEFT:
            dx = 0
        elif self.style == RiemannSum.MID:
            dx = h/2.
        elif self.style == RiemannSum.RIGHT:
            dx = h
        elif self.style == RiemannSum.RANDOM:
            dx = h
        else:
            for i in range(self.N):
                left = self.f.value(x)
                right = self.f.value(x+h)
                self.boxes.append([[x, 0], [x+h,0], [x+h,right],[x,left]])
                x += h
            return
        for i in range(self.N):
            if self.style == RiemannSum.RANDOM:
                r = random()
            else: r = 1
            bottom = self.g.value(x+r*dx)
            top = self.f.value(x+r*dx)
            self.boxes.append([[x,bottom], [x+h, bottom], [x+h,top], [x,top]])
            x += h
    def drawbox(self, b):
        moveto(b[0])
        for p in b:
            lineto(p)
        closepath()
    def fill(self):
        if len(self.boxes) == 0:
            self.getboxes()
        for b in self.boxes:
            newpath()
            self.drawbox(b)
            fill(self.fillcolor)
    def draw(self):
        if len(self.boxes) == 0:
            self.getboxes()
        for b in self.boxes:
            newpath()
            self.drawbox(b)
            self.stroke()

class AreaBetweenCurves(Area):
    def __init__(self, f, g = Function(lambda x:0), domain = None, 
                 fillcolor = 0, color = 0, linewidth = 1):
        Area.__init__(self)
        self.f = Graph(f)
        self.g = Graph(g)
        if domain == None:
            self.setdomain([bbox[0], bbox[2]])
        else: 
            self.setdomain(domain)
        self.fillcolor = fillcolor
        self.color = color
        self.linewidth = linewidth
        self.points = []
    def setdomain(self,d):
        self.f.setdomain(d)
        self.g.setdomain(d)
    def getpoints(self):
        self.points = self.f.getpoints() + self.g.getreversepoints()
    def fill(self):
        newpath()
        if len(self.points) == 0:
            self.getpoints()
            self.append(self.points)
            self.closepath()
        fill(self.fillcolor)
    def draw(self):
        if len(self.points) == 0:
            self.getpoints()
            self.append(self.points)
            self.closepath()
        self.stroke()

class Axes(GeneralPath):
    def __init__(self, color = 0, linewidth = 1, labelalignment="lb",
                 frame = "cc", skipzero=True):
        GeneralPath.__init__(self)
        self.color = color
        self.linewidth = linewidth
        self.hticks = None
        self.vticks = None
        self.hlabels = None
        self.vlabels = None
        self.hticksize = sizeofaxeshticks
        self.vticksize = sizeofaxesvticks
        self.frame = frame
        self.haxis = 0
        self.vaxis = 0
        if frame[0] == "l":
            self.vaxis = bbox[0]
        elif frame[0] == "r":
            self.vaxis = bbox[2]
        if frame[1] == "b":
            self.haxis = bbox[1]
        elif frame[1] == "t":
            self.haxis = bbox[3]
        self.hlabelscale = scaleofaxeshlabels
        self.vlabelscale = scaleofaxesvlabels
        self.labelalignment = labelalignment
        self.skipzero = skipzero
    def draw(self):
        newpath()
        self.moveto([bbox[0], self.haxis])
        self.lineto([bbox[2], self.haxis])
        self.moveto([self.vaxis, bbox[1]])
        self.lineto([self.vaxis, bbox[3]])
        self.stroke()
    def sethticksize(self, s):
        self.hticksize = s
    def setvticksize(self, s):
        self.vticksize = s
    def sethticks(self, t):
        self.hticks = t
    def setvticks(self, t):
        self.vticks = t
    def setticks(self, ht, vt):
        self.sethticks(ht)
        self.setvticks(vt)
    def ticks_labels(self, ht, vt):
        self.setticks(ht, vt)
        self.setlabels(ht, vt)
        self.drawticks()
        self.drawlabels()
    def drawhticks(self):
        x = self.hticks[0]
        dx = self.hticks[1]
        right = self.hticks[2]
        while x <= right:
            gsave()
            translate(x, self.haxis)
            gs = revert()
            translate(gs.transform(0,0))
            moveto(0, -self.hticksize/2.)
            rlineto(0, self.hticksize)
            stroke(self.color)
            x += dx
            grestore()
    def drawvticks(self):
        y = self.vticks[0]
        dy = self.vticks[1]
        top = self.vticks[2]
        while y <= top:
            gsave()
            translate(self.vaxis, y)
            gs = revert()
            translate(gs.transform(0,0))
            moveto(-self.vticksize/2., 0)
            rlineto(self.vticksize, 0)
            stroke(self.color)
            y += dy
            grestore()
    def drawticks(self):
        self.drawhticks()
        self.drawvticks()
    def sethlabels(self, l):
        self.hlabels = l
    def setvlabels(self, l):
        self.vlabels = l
    def setlabels(self, hl, vl):
        self.sethlabels(hl)
        self.setvlabels(vl)
    def sethlabelscale(self, s):
        self.hlabelscale = s
    def setvlabelscale(self, s):
        self.vlabelscale = s
    def drawlabels(self):
        self.drawhlabels()
        self.drawvlabels()
    def drawhlabels(self):
        x = self.hlabels[0]
        dx = self.hlabels[1]
        right = self.hlabels[2]
        s = str(dx)
        d = s.find(".")
        if s < 0 or type(dx) is int:
            decimals = 0
        else:
            decimals = len(s) - s.find(".") - 1
        while x <= right:
            if self.skipzero and abs(x) < 0.000000001 and self.frame[0] == "c":
                x += dx
                continue
            s = str(x)
            if s.find(".") < 0 and decimals > 0:
                s += "."
                for i in range(decimals):
                    s += "0"
            else:
                while len(s) - s.find(".") - 1 < decimals:
                    s += "0"
            if self.labelalignment[1] == "b":
                alignment = "ct"
### Reinstate commented line for mathtxwhatever
                offset = [0, -self.hticksize/2. - 3]
#                offset = [1.5, -self.hticksize/2. ]
            else:
                alignment = "cb"
                offset = [0, self.hticksize/2. + 3]
#            s = "$" + s + "$"
            label = Label(s, [x, self.haxis], alignment = alignment,
                          scale = self.hlabelscale, color=black,
                          offset = offset)
            label.draw()
            x += dx

    def drawvlabels(self):
        y = self.vlabels[0]
        dy = self.vlabels[1]
        top = self.vlabels[2]
        s = str(dy)
        d = s.find(".")
        if s < 0 or type(dy) is int:
            decimals = 0
        else:
            decimals = len(s) - s.find(".") - 1
        while y <= top:
            if self.skipzero and abs(y) < 0.00000001 and self.frame[1] == "c":
                y += dy
                continue
            s = str(y)
            if s.find(".") < 0 and decimals > 0:
                s += "."
                for i in range(decimals):
                    s += "0"
            else:
                while len(s) - s.find(".") - 1 < decimals:
                    s += "0"
            if self.labelalignment[0] == "l":
                alignment = "rc"
                ### Reinstate commented cmd for mathptwhatever
                offset = [-self.vticksize/2.0 - 2, 0]
#                offset = [-self.vticksize/2.0+2, 2]
            else:
                alignment = "lc"
                offset = [self.vticksize/2.0 + 2, 0]
#            s = "$" + s + "$"
            label = Label(s, [self.vaxis, y], scale = self.vlabelscale,
                          offset = offset, alignment = alignment, color=black)
            label.draw()
            y += dy

class Legend():
    def __init__(self, ll, width, height, colors, labels):
        self.ll = ll
        self.width = width
        self.height = height
        self.colors = colors
        self.labels = labels
    def draw(self):
        N = 100
        gsave()
        translate(self.ll)
        M = len(self.colors)
        dy = self.height/float(N*M)
        y = 0
        count = 0
        gsave()
        for j in range(M):
            color0 = self.colors[j][0]
            color1 = self.colors[j][1]
            for i in range(N):
                newpath()
                moveto(0, y)
                rlineto(self.width, 0)
                rlineto(0, dy)
                rlineto(-self.width, 0)
                closepath()
                fill(blend(color0, color1, count/float(N-1)))
                y += dy
                count+=1
            y = 0
            count = 0
            translate(0, N*dy)
        grestore()
        newpath()
        moveto(0,0)
        rlineto(self.width, 0)
        rlineto(0, self.height)
        rlineto(-self.width, 0)
        closepath()
        stroke()

        for l in self.labels:
            label = l[0]
            pos = l[1]
            y = pos*self.height
            newpath()
            moveto(0, y)
            rlineto(-2,0)
            stroke()
            Label(label, [0,pos*self.height], 
                  offset=[-4,0], alignment="rc").draw()
        grestore()

class Label():
    def __init__(self, s, p, scale = 0.9, color = 0, 
                 angle = 0, offset = [0,0], basis = None,
                 alignment = "lb",clear=False):
        self.s = s
        self.p = p
        self.scale = scale
        self.angle = angle
        self.color = color
        self.offset = offset
        self.alignment = alignment
        self.clear = clear
        self.basis = basis
        t = texinsert(s)
        self.texinsert = t
        t.translate(self.offset)
        dx = 0
        if self.alignment[0] == "r":
            dx = -t.width
        elif self.alignment[0] == "c":
            dx = -0.5*t.width
        dy = -t.height
        if self.alignment[1] == "b":
            dy = t.depth
        elif self.alignment[1] == "c":
            dy = -(t.height-t.depth)/2.0
        t.translate(dx, dy)
        t.scale(self.scale)
        t.rotate(self.angle)
        if self.basis != None:
            t.atransform(self.basis[0], self.basis[1])
        self.bbox = t.bbox

    def draw(self):
        gsave()
        newpath()
        translate(self.p)
        t = self.texinsert
        if self.clear:
            self.mkclear(t)

        if type(self.color) is float or type(self.color) is int:
            setgray(self.color)
        else:
            setcolor(self.color)
        place(t)
        grestore()

    def height(self):
        return self.bbox[3] - self.bbox[1]

    def setalignment(self, a):
        self.alignment = a
    def setscale(self, s):
        self.scale = s
    def setangle(self, a):
        self.angle = a
    def setcolor(self, c):
        self.color = c
    def setoffset(self, o):
        self.offset = o
    def mkclear(self, t):
        gsave()
        ds = 3
        lrevert()
        newpath()
        translate(0,-5)
        b = t.bbox
        boundedbox(b[0]-ds, b[1]-ds, b[2]+ds, b[3]+ds)
        fill(1)
        grestore()

class Graph(GeneralPath):
    def __init__(self, f, domain = None, N = 100, 
                 color = graphcolor, linewidth=graphwidth, dash = None):
        GeneralPath.__init__(self)
        self.f = f
        if domain == None:
            self.x0 = bbox[0]
            self.x1 = bbox[2]
        else:
            self.setdomain(domain)
        self.N = N
        self.color = color
        self.linewidth = linewidth
        self.dash = dash
    def setfunction(self, f):
        self.f = f
    def setdomain(self, d):
        self.x0 = d[0]
        self.x1 = d[1]
    def setN(self, N):
        self.N = N
    def getpoints(self):
        points = []
        dx = (self.x1 - self.x0)/float(self.N)
        x = self.x0
        newpath()
        points.append([x, self.f.value(x)])
        for i in range(self.N):
            x += dx
            points.append([x, self.f.value(x)])
        return points
    def getreversepoints(self):
        points = []
        dx = (self.x0 - self.x1)/float(self.N)
        x = self.x1
        newpath()
        points.append([x, self.f.value(x)])
        for i in range(self.N):
            x += dx
            points.append([x, self.f.value(x)])
        return points
    def draw(self):
        self.append(self.getpoints())
        self.stroke()

class ParametricCurve(Area):
    def __init__(self, f, g, d, N = 100, color = 0, fillcolor = 0, linewidth=1,
                 dash = None):
        Area.__init__(self)
        self.f = f
        self.g = g
        self.domain = d
        self.N = N
        self.points = []
        self.color = color
        self.fillcolor = fillcolor
        self.linewidth = linewidth
        self.dash = dash
    def setdomain(self, d):
        self.domain = d
    def setN(self, N):
        self.N = N
    def getpoints(self):
        self.points = []
        t = self.domain[0]
        dt = (self.domain[1]-self.domain[0])/float(self.N)
        for i in range(self.N):
            self.points.append([self.f.value(t), self.g.value(t)])
            t += dt
        self.points.append([self.f.value(t), self.g.value(t)])
    def fill(self):
        newpath()
        if len(self.points) == 0:
            self.getpoints()
            self.append(self.points)
        fill(self.fillcolor)
    def draw(self):
        newpath()
        if len(self.points) == 0:
            self.getpoints()
            self.append(self.points)
        self.stroke()

        

class Grid(GeneralPath):
    def __init__(self, xspec, yspec, 
                 color = gridcolor, linewidth = gridwidth, dash = None):
        GeneralPath.__init__(self)
        self.xspec = xspec
        self.yspec = yspec
        self.color = color
        self.linewidth = linewidth
        self.dash = dash
    def draw(self):
        newpath()
        x = self.xspec[0]
        while x <= self.xspec[2]:
            self.moveto([x, bbox[1]])
            self.lineto([x, bbox[3]])
            x += self.xspec[1]
        
        y = self.yspec[0]
        while y <= self.yspec[2]:
            self.moveto([bbox[0], y])
            self.lineto([bbox[2], y])
            y += self.yspec[1]
        self.stroke()

class MGrid(GeneralPath):
    def __init__(self, xspec, yspec, 
                 color = gridcolor, linewidth = gridwidth, dash = None):
        GeneralPath.__init__(self)
        self.xspec = xspec
        self.yspec = yspec
        self.color = color
        self.linewidth = linewidth
        self.dash = dash
    def draw(self):
        newpath()
        x = self.xspec[0]
        while x <= self.xspec[2]:
            self.moveto([x, self.yspec[0]])
            self.lineto([x, self.yspec[2]])
            x += self.xspec[1]
        
        y = self.yspec[0]
        while y <= self.yspec[2]:
            self.moveto([self.xspec[0], y])
            self.lineto([self.xspec[2], y])
            y += self.yspec[1]
        moveto(self.xspec[0], self.yspec[0])
        lineto(self.xspec[2], self.yspec[0])
        lineto(self.xspec[2], self.yspec[2])
        lineto(self.xspec[0], self.yspec[2])
        closepath()
        self.stroke()

class Lagrange(Function):
    def __init__(self, *args):
        if len(args) == 1:
            self.points = args[0]
        else:
            self.points = []
        self.setup()
    def addpoints(self, p):
        self.points = self.points + p
    def addpoint(self, p):
        self.points.append(p)
    def f(self, x):
        self.value(x)
    def setup(self):
        self.n = len(self.points) - 1
        self.x = []
        diffs = []
        self.coeffs = []
        for p in self.points:
            self.x.append(p[0])
            diffs.append(p[1])

        self.coeffs = [diffs[0]]
        while len(diffs) > 1:
            j = self.n - len(diffs) + 2
            next = []
            for i in range(len(diffs) - 1):
                next.append((diffs[i+1] - diffs[i])/float(self.x[i+j]-self.x[i]))
            self.coeffs.append(next[0])
            diffs = next

    def value(self, x):
        val = self.coeffs[self.n]
        for i in range(self.n-1, -1, -1):
            val = val*(x-self.x[i]) + self.coeffs[i]
        return val

class Hermite(Function):
    def __init__(self, *args):
        if len(args) == 1:
            self.points = args[0]
        else:
            self.points = []
        self.setup()
    def addpoints(self, p):
        self.points = self.points + p
    def addpoint(self, p):
        self.points.append(p)
    def f(self, x):
        self.value(x)
    def setup(self):
        self.x = []
        diffs = []
        self.coeffs = []
        for i in range(len(self.points)):
            self.x.append(self.points[i][0])
            self.x.append(self.points[i][0])
            diffs.append(self.points[i][2])
            if i != len(self.points) - 1:
                diffs.append((self.points[i+1][1] - self.points[i][1])
                             /float(self.points[i+1][0]-self.points[i][0]))

        self.coeffs = [self.points[0][1], diffs[0]]
        while len(diffs) > 1:
            j = len(self.x) - len(diffs) + 1
            next = []
            for i in range(len(diffs) - 1):
                next.append((diffs[i+1] - diffs[i])/float(self.x[i+j]-self.x[i]))
            self.coeffs.append(next[0])
            diffs = next

    def value(self, x):
        self.n = len(self.coeffs)-1
        val = self.coeffs[self.n]
        for i in range(self.n-1, -1, -1):
            val = val*(x-self.x[i]) + self.coeffs[i]
        return val

class Derivative(Function):
    def __init__(self, f):
        self.setup()
        self.f = f
    def value(self, x):
        return (self.f.value(x+self.dx)-self.f.value(x-self.dx))/(2.0*self.dx)

class Antiderivative(Function):
    def __init__(self, f, a):
        self.setup()
        self.f = f
        self.a = a
        self.N = 50
    def setN(self, N):
        self.N = N
    def value(self, x):
        sum = 0
        h = (x - self.a)/float(self.N)
        x = self.a
        for i in range(self.N/2):
            sum += self.f.value(x) + 4*self.f.value(x+h) + self.f.value(x+2*h)
            x += 2*h
        return sum*h/3.0
    def derivative(self, x):
        return self.f.value(x)

def midpoint(u, v):
    return [ (u[0] + v[0]) / 2.,
             (u[1] + v[1]) / 2.
             ]
    
class QuadTree():
    def __init__(self, b, d):
        self.corners = b
        self.depth = d
    def subdivide(self):
        bottom = midpoint(self.corners[0], self.corners[1])
        left = midpoint(self.corners[0], self.corners[3])
        right = midpoint(self.corners[1], self.corners[2])
        top = midpoint(self.corners[2], self.corners[3])
        mid = midpoint(bottom, top)
        return [QuadTree([self.corners[0], bottom, mid, left], self.depth-1),
                QuadTree([bottom, self.corners[1], right, mid], self.depth-1),
                QuadTree([left, mid, top, self.corners[3]], self.depth-1),
                QuadTree([mid, right, self.corners[2], top], self.depth-1)
                ]
    def intersects(self, g):
        sign = g.value(self.corners[3])
        for i in range(4):
            nextsign = g.value(self.corners[i])
            if sign * nextsign <= 0:
                return True
            sign = nextsign
        return False


    def findzero(self, p1, p2, g):
        dx = p2[0]-p1[0]
        dy = p2[1]-p1[1]
        change = 0.00001
        if dx != 0:
            dx = change*abs(dx)/dx
            dy = 0
            dt = dx
        else:
            dy = change*abs(dy)/dy
            dx = 0
            dt = dy
        p = p1
        diff = 1
        N = 0
        while abs(diff) > 0.000001 and N < 50:
            f = g.value(p)
            if f == 0:
                break
            df = (g.value([p[0] + dx, p[1] + dy]) - f)/dt
            diff = f/float(df)
            if dx != 0:
                nextp = [ p[0] - diff, p[1] ]
            else:
                nextp = [ p[0], p[1] - diff ]
            N += 1
            p = nextp
        return p
        

    def segments(self, g):
        corner = self.corners[3]
        sign = g.value(corner)
        segments = []
        lastZero = None
        for i in range(4):
            nextcorner = self.corners[i]
            nextsign = g.value(nextcorner)
            if sign == 0 and nextsign == 0:
                segments.append([corner, nextcorner])
            elif sign * nextsign <= 0:
                if lastZero == None:
                    lastZero = self.findzero(corner, nextcorner, g)
                else:
                    thisZero = self.findzero(corner, nextcorner, g)
                    segments.append([lastZero, thisZero])
                    lastZero = thisZero
            corner = nextcorner
            sign = nextsign
        return segments
            
class LevelSet():                
    def __init__(self, f, k):
        self.f = f
        self.k = k
    def value(self, p):
        return self.f(p[0], p[1]) - self.k
                
class Implicit(GeneralPath):
    def __init__(self, f, k, color = 0, linewidth = 1, 
                      box = None, depth = 8, initialdepth = 4):
        GeneralPath.__init__(self)
        self.color = color
        self.linewidth = linewidth
        if box == None:
            self.bbox = bbox
        else:
            self.bbox = box
        self.depth = depth
        self.initialdepth = initialdepth
        self.levelset = LevelSet(f, k)
        self.k = k
        
    def draw(self):
        newpath()
        gsave()
        setlinewidth(self.linewidth)
        root = QuadTree([ [self.bbox[0], self.bbox[1]],
                          [self.bbox[2], self.bbox[1]],
                          [self.bbox[2], self.bbox[3]],
                          [self.bbox[0], self.bbox[3]]
                          ], self.depth)
        tree = [root]
        for i in range(self.initialdepth):
            newtree = []
            for node in tree:
                newtree = newtree + node.subdivide()
            tree = newtree
        while len(tree) > 0:
            node = tree.pop(0)
            if node.depth == 0:
                segments = node.segments(self.levelset)
                for s in segments:
                    self.moveto(s[0])
                    self.lineto(s[1])

            elif node.intersects(self.levelset):
                tree = tree + node.subdivide()
        
        self.stroke()
        grestore()
    
    def getpoints(self):
        root = QuadTree([ [self.bbox[0], self.bbox[1]],
                          [self.bbox[2], self.bbox[1]],
                          [self.bbox[2], self.bbox[3]],
                          [self.bbox[0], self.bbox[3]]
                          ], self.depth)
        tree = [root]
        for i in range(self.initialdepth):
            newtree = []
            for node in tree:
                newtree = newtree + node.subdivide()
            tree = newtree
        points = []
        while len(tree) > 0:
            node = tree.pop(0)
            if node.depth == 0:
                segments = node.segments(self.levelset)
                for s in segments:
                    points.append([[s[0][0], s[0][1], self.k],
                                   [s[1][0], s[1][1], self.k]])

            elif node.intersects(self.levelset):
                tree = tree + node.subdivide()

        return points

def blend(c1, c2, alpha):
    r = [0]*3
    for i in range(3):
        r[i] = c1[i]*(1-alpha) + c2[i]*alpha
    return r

def integrate(f, domain, N):
    result = 0
    x0, x1 = domain
    h = (x1-x0)/float(2*N)
    x = x0
    for i in range(N):
        term = f(x) + 4*f(x+h) + f(x+2*h)
        result += h*term/3.0
        x+=2*h
    return result

def bisection(f, value, domain, tolerance):
    low = domain[0]
    high = domain[1]
    while True:
        middle = (low+high) / 2.0
        ymid = f(middle)
        if abs(ymid - value) < tolerance:
            return middle
        if ((f(low)-value) * (ymid-value)) > 0:
            low = middle
        else:
            high = middle

def mkaxes(rx, ry):
    axes = Axes()
    axes.draw()
    axes.setticks(rx,ry)
    axes.setlabels(rx,ry)
    axes.drawticks()
    axes.drawlabels()

def mklabels(x1, s1, y1, s2):
    Label(s1, [x1, 0], offset=[-3,3], alignment="rb").draw()
    Label(s2, [0, y1], offset=[3,-3], alignment="lt").draw()

def mycurveto(p,q,r,s):
    moveto(p)
    curveto(vsum(p,q), vsum(r,s), s)

def halfcurvearrow(p, q, r, arrowdims = None, color=None):
    if color == None:
        color = 0
    gsave()
    gs = revert()
    p = gs.transform(p)
    q = gs.transform(q)

    mid = [(p[0]+q[0])/2.0, (p[1]+q[1])/2.0]
    diff = vdiff(q,p)
    ldiff = length(diff)
    rn = sqrt(r*r - ldiff*ldiff/4.0)
    if r < 0:
        rn *= -1
    
    diff = smult(1/length(diff), diff)
    normal = [diff[1], -diff[0]]
    center = vsum(mid, smult(rn, normal))
    dp = vdiff(p, center)
    dq = vdiff(q, center)
    angle1 = atan2(dp[1], dp[0])
    angle2 = atan2(dq[1], dq[0])

    if arrowdims != None:
        setarrowdims(arrowdims[0], arrowdims[1])

    '''
    anglediff = angle2 - angle1
    if anglediff > pi:
        anglediff -= 2*pi
    if anglediff < -pi:
        anglediff += 2*pi
    '''
    while angle2 - angle1 > pi:
        angle2 -= 2*pi
    while angle2 - angle1 < -pi:
        angle2 += 2*pi
    anglediff = angle2 - angle1
    angle3 = angle1+0.5*anglediff

    r= abs(r)
    newpath()
    if angle2 - angle1 > 0:
        arcarrow(center, r, angle1, angle2)
        fill()
        arcarrow(center, r, angle1, angle3)
        fill()
    else:
        arcnarrow(center, r, angle1, angle2)
        fill()
        arcnarrow(center, r, angle1, angle3)
        fill()

    grestore()
