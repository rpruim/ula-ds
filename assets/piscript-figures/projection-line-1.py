from figures import *

width = 150
height = width
margin = 5

v = [2,1]
w = [2,4]
a = dot(v,w)/float(dot(v,v))
proj = smult(a,v)

beginfigure("projection-line-1", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-1,-1,5,5])

Grid([-1,1,5], [-1,1,5]).draw()

settexenv("ACTexConfig")

axes = Axes()
axes.setticks([-1,1,5],[-1,1,5])
axes.setlabels([0,2,5], [0,2,5])
axes.draw()
axes.drawticks()
axes.drawlabels()

Graph(Function(lambda x: 0.5*x), color=blue).draw()
Vector(v).fill()
Vector(w).fill()

Label(r"${\boldsymbol w}$", v, alignment="lt", offset=[4,-4]).draw()
Label(r"${\boldsymbol b}$", w, alignment="rb", offset=[-4,4]).draw()
Label(r"$L$", [5,2.5], alignment="rb", offset=[-4,4]).draw()

endfigure()


