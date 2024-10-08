from figures import *

width=150
height=width
margin = 5

size = 3
beginfigure('two-dim-basis', width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size, -size, size, size])

Grid([-size, 1, size], [-size, 1, size]).draw()

axes = Axes()
axes.draw()
axes.setticks([-size,1,size], [-size, 1, size])
axes.setlabels([-size,1,size], [-size, 1, size])
axes.drawticks()
axes.drawlabels()

e1 = [1,0]
e2 = [0,1]
u  = [-2, -1]
#Tu = [-v[1], v[0]]

for v in [e1, e2, u]:
    v = Vector(v, color=blue, fillcolor=blue)
    v.fill()
    v.draw()

sc = 1
Label(r'${\boldsymbol e}_1$', e1, alignment='lb', offset=[3,3],
      scale=sc).draw()
Label(r'${\boldsymbol e}_2$', e2, alignment='lb', offset=[3,3],
      scale=sc).draw()
Label(r'${\boldsymbol v}$', u, alignment='rb', offset=[-3,3],
      scale=sc).draw()
#Label(r'$T({\boldsymbol v})$', Tu, alignment='rb', offset=[-3,3]).draw()

endfigure()

