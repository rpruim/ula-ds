from figures import *

width = 150
height = width
margin = 5
imargin = 20
size = 6

trajectorycolor = lightblue
pointcolor = lightred

lam1 = 0.9
lam2 = 0.7
points = [[5,0], [5,1], [5,3], [5,5], [3,5], [1,5], [0,5]]

iters = [0,1,2,3]

def poncurve(p, k):
    return [lam1**k*p[0], lam2**k*p[1]]

def pointoncurve(p, k):
    p = Point(poncurve(p,k), 2)
    p.fill()

def trajectory(p):
    k = 1.5
    v = Vector(poncurve(p, k+0.1), tail=poncurve(p,k),
               arrowdims=[1,5], fillcolor=blue).fill()
    ParametricCurve(Function(lambda x: poncurve(p,x)[0]),
                    Function(lambda x: poncurve(p,x)[1]),
                    [-20,20], color=blue).draw()


def traj(p):
    trajectory(p)
    for k in iters:
        pointoncurve(p, k)

def plot(basis0, basis1):
    gsave()
    setupcoordinates([margin, margin, width+margin, height+margin],
                     [-size,-size,size,size])

    gsave()
    cliptoboundingbox()
    atransform(basis0, basis1)

    MGrid([-20,1,20],[-20,1,20]).draw()
    
    for pp in points:
        traj(pp)
        traj([-pp[0], pp[1]])
        traj([pp[0], -pp[1]])
        traj([-pp[0], -pp[1]])

    grestore()
        
    grestore()

beginfigure("ex-dynam-sol-d",
            2*width+2*margin+imargin, height+2*margin)

plot([1,0],[0,1])

translate(width+imargin,0)
plot([2,2],[2,4])

endfigure() 
    
