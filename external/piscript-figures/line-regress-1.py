from figures import *

width = 175
height = width
margin = 7

size = 4

beginfigure("line-regress-1", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1,-1,size,size])

settexenv("ACTexConfig")

points = [[1,1], [2,1], [3,3]]

m = 1
b = -1/3.0

xr = [-1,1,size]

Grid(xr, xr).draw() 

axes = Axes()
axes.setticks(xr,xr)
axes.setlabels([-1,1,size], [-1,1,size])
axes.draw()
axes.drawticks()
axes.drawlabels()

def f(x):
    return m*x + b

for p in points:
    newpath()
    gsave()
    moveto(p)
    lineto([p[0], f(p[0])])
    setlinewidth(2)
    stroke(red)
    grestore()
    p = Point(p, 2.5, fillcolor=lightred)
    p.fill()
    p.draw()

gsave()
cliptoboundingbox()
Graph(Function(f), color=blue).draw()
grestore()

mklabels(size, r"$x$", size, r"$y$")

endfigure() 
