from figures import *
from fig3d import *
from Vectors import Vector as Vec
import math


def avg(points):
    s = [0]*len(points[0])
    for p in points:
        s = vadd(s, p)
    return smult(1/float(len(points)), s)

width=190
margin = 0
height = 150
sc=1
init3d("3d-orthog-proj-3", int(sc*width)+10, int(sc*height)+10)
beginpage()

settexenv("ACTexConfig")

translate(5,5)
newpath()
box(0,0,width,height)
clip()
newpath()

gsave()
 
scale(sc)


#seteye([0.3, 0.25, 1, 0])
seteye([0.45, 0.5, 1, 0])
setlight([3,5,10, 0])

gsave()
gsave3d()

s = 70
translate(90, 60)
#scale3d(s,1.19*s,s)
scale3d(s,s,s)

xa = 1.6
ya = 1.3
za = 1.2
def axes(color):
    newpath()
    moveto3d(0,0,0)
    lineto3d(2*ya,0,0)
    moveto3d(0,0,0)
    lineto3d(0,za,0)
    moveto3d(0,0,0)
    lineto3d(0,0,xa)
    stroke(color)

w1 = smult(0.5, tofig([1,0.3,-0.15]))
w2 = smult(0.5, tofig([-0.2,1,0.2]))
w3 = cross(w1,w2)

a = 1.5
c = 1.7
b = vsum(smult(5.6, w3), vsum(smult(a,w1), smult(c,w2)))
proj = vsum(smult(a,w1), smult(c,w2))

def lincomb(a,v1,c,v2):
    return vadd(smult(a,v1), smult(c,v2))

t0 = 2.5
t1 = t0

gsave()
newpath()
moveto3d(lincomb(-t0,w1,-t1, w2))
lineto3d(lincomb(t0,w1,-t1, w2))
lineto3d(lincomb(t0,w1,t1, w2))
lineto3d(lincomb(-t0,w1,t1, w2))
closepath()
fill(0.8)
clip()

newpath()
symgrid([0,0,0], w1, w2, 4,4)
stroke(gray)
origin = [0,0,0]

grestore()

newpath()
axes(black)

'''
newpath()
moveto3d(b)
lineto3d(proj)
stroke()
'''

delta = 0.2
dz = smult(0.4, w3)
dy = smult(delta, w2)

newpath()
moveto3d(proj)
rmoveto3d(dz)
rlineto3d(dy)
rlineto3d(smult(-1,dz))
stroke()

newpath()
arrow3dto(proj, b, lightred)
arrow3dto(origin, w1, black)
arrow3dto(origin, w2, black)
arrow3dto(origin, b, blue)
arrow3dto(origin, proj, lightblue)
#arrow3dto(proj, b, black)
 
dx = 4
#Label(r'$z$', [0,za,0], alignment="lt", offset=[dx,-dx]).draw()
#Label(r'$y$', [ya,0,0], alignment="rt", offset=[4,-dx]).draw()
#Label(r'$x$', [0,0,xa], alignment="rb", offset=[-dx,0]).draw()
Label(r'${\boldsymbol w}_1$', w1, alignment="lt", offset=[dx,-2]).draw()
Label(r'${\boldsymbol w}_2$', w2, alignment="rb", offset=[-dx,5]).draw()
Label(r'${\boldsymbol b}$', 0.8 * Vec(b), alignment="rb", offset=[-dx,0], color = blue).draw()
Label(r'$\widehat{\boldsymbol b}$', 0.8 * Vec(proj), alignment="rt", offset=[-8,-dx+2], color = lightblue).draw()
Label(r'${\boldsymbol b} - {\hat{\boldsymbol b}}$', 0.5 * (Vec(b) + Vec(proj)), alignment="lb", offset=[dx,0], color = red).draw()

grestore3d()
grestore()

grestore()
box(1,1,width-2,height-2)
stroke()

endpage()
finish()
