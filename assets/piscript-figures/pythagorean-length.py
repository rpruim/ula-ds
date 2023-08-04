from figures import *
from Vectors import Vector as Vec

x0 = -1
x1 = 4

x = Vec([3, 2])
origin = Vec([0,0])

width=175
height=width
margin = 5
beginfigure("pythagorean-length", width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [x0,x0,x1,x1])

# Grid([x0,1,x1], [x0,1,x1]).draw()

newpath()
# box(0,0,3,2)
# stroke(0.5)


axes = Axes()
axes.draw()
# axes.setticks([x0,1,x1], [x0,1,x1])
# axes.setlabels([x0,1,x1], [x0,1,x1])
# axes.drawticks()
# axes.drawlabels()

Vector(x).fill()
Line([3, 0], [3, 2], color = blue).draw()
Line([0, 0], [3, 0], color = blue).draw()
Label(r"${\boldsymbol x}$", [0.5 * 3, 0.5 * 2], alignment="lb", offset=[0,10]).draw()
Label(r"${x_0}$", [3.0/2, 0], alignment="lt", offset=[0,-3]).draw()
Label(r"${x_1}$", [3,1], alignment="lt", offset=[4,0]).draw()
Label(r"$| \boldsymbol x |^2 = x_0^2 + x_1^2$", [1,3], alignment="lt", offset=[0,0]).draw()

endfigure()
