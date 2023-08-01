from figures import *

width = 200
height = width
margin = 5

size = 6

beginfigure("parallelogram-law", width, height)
setupcoordinates([margin, margin, width-margin, height-margin],
                 [-1,-1,6,6])

w = [4,2]
v = [1.5,3]
s = vsum(v,w)
d = vdiff(v,w)

axes = Axes()
axes.draw()

newpath()
moveto([0,0])
lineto(w)
lineto(s)
lineto(v)
closepath()
stroke()

for ve in [w,v,s]:
    Vector(ve).fill()

Vector(v, tail=w).fill()
Label(r"$|{\boldsymbol v}|$", smult(0.6, w), alignment='lt', offset=[2,-2]).draw()
Label(r"$|{\boldsymbol w}|$", smult(0.6,v), alignment='rb', offset=[-2,2]).draw()
Label(r"$|{\boldsymbol v}|+|{\boldsymbol w}|$", smult(0.75,s), alignment='lt', offset=[2,-2]).draw()
Label(r"$|{\boldsymbol v}|-|{\boldsymbol w}|$", w, alignment='lb', offset=[-13,7]).draw()

endfigure()
