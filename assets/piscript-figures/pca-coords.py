from figures import *

width=150
height=150
margin = 5

size = 3
beginfigure('pca-coords', width+2*margin, height+2*margin)
setupcoordinates([margin, margin, width+margin, height+margin],
                 [-size,-size,size,size])

Grid([-size,1,size], [-size,1,size]).draw()

axes = Axes()
axes.draw()

xhat = [1.5,1.5]

for p in [[1,0], [0,1], xhat]:
    Vector(p, fillcolor=black).fill()

Label(r'${\boldsymbol u}_1$', [1,0], alignment='lt', offset=[3,-3]).draw()
Label(r'${\boldsymbol u}_2$', [0,1], alignment='rb', offset=[-3,3]).draw()     
Label(r'$\widehat{\boldsymbol x}=\begin{bmatrix}{\boldsymbol u}_1\cdot{\boldsymbol x} \\ {\boldsymbol u}_2\cdot{\boldsymbol x} \end{bmatrix}$', xhat, alignment='cb', offset=[0,3]).draw()    

endfigure()

