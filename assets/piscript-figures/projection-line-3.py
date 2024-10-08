from figures import *

width = 150
height = width
margin = 5

v = [2,1]
w = [2,4]
a = dot(v,w)/float(dot(v,v))
proj = smult(a,v)
y = smult(2.1,v)

beginfigure("projection-line-3", width+2*margin, height+2*margin)
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
Vector(w).fill()
Vector(proj, fillcolor=black).fill()
Vector(y, fillcolor=black).fill()
Vector(w, tail=proj, fillcolor=gray).fill()
Vector(w, tail=y, fillcolor=gray).fill()
#Vector(v).fill()

z = proj
gsave()
translate(z)
newpath()
uu = normalize(vdiff(w, z))
vv = normalize(v)
dx = 0.35
moveto(smult(dx, uu))
rlineto(smult(dx, vv))
rlineto(smult(-dx, uu))
stroke(gray)
grestore()

#Label(r"${\boldsymbol v}$", v, alignment="lt", offset=[4,-4]).draw()
Label(r"$\widehat{\boldsymbol b}$", proj, alignment="lt", offset=[4,2]).draw()
Label(r"${\boldsymbol y}$", y, alignment="lt", offset=[4,-4]).draw() 
Label(r"${\boldsymbol b}$", w, alignment="rb", offset=[-4,4]).draw()
Label(r"$L$", [5,2.5], alignment="rb", offset=[-4,4]).draw()
Label(r"${\boldsymbol b}-\widehat{\boldsymbol b}$", smult(0.5,vsum(proj,w)),
      alignment="rt", offset=[2,-6]).draw() 
 
endfigure()



