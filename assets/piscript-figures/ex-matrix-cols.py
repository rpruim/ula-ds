from figures import *

width = 200
height = width
margin = 5

size = 5.5

beginfigure("ex-matrix-cols", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-size,-size,size,size])

u = [2,-0.5]
v = [-1,1.5]

Axes().draw()

gsave()
cliptoboundingbox()
atransform(u,v)
Grid([-12,1,12],[-12,1,12]).draw()
grestore()

vector = Vector(u, color=gray, fillcolor=gray)
vector.fill()
vector.draw()

vector = Vector(v, color=gray, fillcolor=gray)
vector.fill()
vector.draw()

Label(r"${\boldsymbol v}_1$", u, offset=[4,-4], alignment="lt").draw()
Label(r"${\boldsymbol v}_2$", v, offset=[-4,4], alignment="rb").draw()
 
points = [[[-3,-3], r"${\boldsymbol b}$", [-4,4], "rb"]]

for point in points:
    pp = vsum(smult(point[0][0],u), smult(point[0][1],v))
    vect = Vector(pp, fillcolor=black)
    vect.fill()
    vect.draw()
    Label(point[1], pp, offset=point[2], alignment=point[3]).draw()

endfigure()
