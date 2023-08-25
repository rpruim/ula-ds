from piscript.PiModule import *
import math

class Label():
    def __init__(self, s, p, scale = 0.9, color = 0, 
                 angle = 0, offset = [0,0], basis = [[1,0], [0,1]],
                 alignment = "lb"):
        self.s = s
        self.p = p
        self.scale = scale
        self.angle = angle
        self.color = color
        self.offset = offset
        self.basis = basis
        self.alignment = alignment
    def setalignment(self, a):
        self.alignment = a
    def setscale(self, s):
        self.scale = s
    def setangle(self, a):
        self.angle = a
    def setcolor(self, c):
        self.color = c
    def setoffset(self, o):
        self.offset = o
    def draw(self):
        gsave()
        newpath()
        gs = revert()
        p = projection2d(self.p)
        p = gs.transform(p)
        translate(p)
        t = texinsert(self.s)
        t.translate(self.offset)
        dx = 0
        if self.alignment[0] == "r":
            dx = -t.width
        elif self.alignment[0] == "c":
            dx = -0.5*t.width
        dy = -t.height
        if self.alignment[1] == "b":
            dy = t.depth
        elif self.alignment[1] == "c":
            dy = -(t.height-t.depth)/2.0
        t.translate(dx, dy)
        t.atransform(self.basis[0], self.basis[1])
        t.scale(self.scale)
        t.rotate(self.angle)
        if type(self.color) is float or type(self.color) is int:
            setgray(self.color)
        else:
            setcolor(self.color)
        place(t)
        grestore()

def axes(x,y,z):
    newpath()
    moveto3d(0,0,0)
    lineto3d(x,0,0)

    moveto3d(0,0,0)
    lineto3d(0,y,0)

    moveto3d(0,0,0)
    lineto3d(0,0,z)

def figaxes(x,y,z):
    newpath()
    moveto3d(tofig([0,0,0]))
    lineto3d(tofig([x,0,0]))

    moveto3d(tofig([0,0,0]))
    lineto3d(tofig([0,y,0]))

    moveto3d(tofig([0,0,0]))
    lineto3d(tofig([0,0,z]))

def saxes(x,y,z):
    newpath()
    moveto3d(-x,0,0)
    lineto3d(x,0,0)

    moveto3d(0,-y,0)
    lineto3d(0,y,0)

    moveto3d(0,0,-z)
    lineto3d(0,0,z)

def poly(points):
    newpath()
    moveto3d(points[0])
    for p in points:
        lineto3d(p)
    closepath3d()

HORIZONTALTICK = 0
VERTICALTICK = 1

def arrow3dtothin(p0, p1, color):
    gsave()
    gs = revert()
    p = projection2d(p0)
    p = gs.transform(p)
    q = projection2d(p1)
    q = gs.transform(q)
    newpath()
    setarrowdims(1.5, 4.5)
    arrow(p, q)
    fill(color)
    grestore()

def arrow3dto(p0, p1, color):
    gsave()
    gs = revert()
    p = projection2d(p0)
    p = gs.transform(p)
    q = projection2d(p1)
    q = gs.transform(q)
    newpath()
    setarrowdims(2, 6)
    arrow(p, q)
    fill(color)
    grestore()

def axesarrows(x,y,z):
    arrow3dto([0]*3, [x, 0, 0], 0)
    arrow3dto([0]*3, [0, y, 0], 0)
    arrow3dto([0]*3, [0, 0, z], 0)

def tick(point, size, color, orientation):
    gsave()
    gs = revert()
    p = projection2d(point)
    p = gs.transform(p)
    newpath()
    translate(p)
    if orientation == HORIZONTALTICK:
        moveto(size/2, 0)
        lineto(-size/2, 0)
    else:
        moveto(0, size/2)
        lineto(0, -size/2)
    stroke(color)
    grestore()

def facetrace(face):
    p = face.p
    n = len(p)
    newpath()
    moveto3d(p[-1][0], p[-1][1], p[-1][2])
    for i in range (n):
        lineto3d(p[i][0], p[i][1], p[i][2])
    closepath3d()

def clipface(face):
    facetrace(face)
    clip()

def getshading(face, color):
    L = get_light(); 
    nf = face.nf
    s = L[0]*nf[0]+L[1]*nf[1]+L[2]*nf[2]
    s = (s + 1.0)/2
    s = Bezier.bernstein(face.shading, s)
    c = color
    return [s*c[0], s*c[1], s*c[2]]

def blend(c1, alpha, c2):
    a = alpha
    a1 = 1-alpha
    return [ c1[0]*a1 + c2[0]*a,
             c1[1]*a1 + c2[1]*a,
             c1[2]*a1 + c2[2]*a ]

def transparentface(face, color, alpha, interior):
    gsave()
    clipface(face)
    interior(getshading(face, color), alpha)
    grestore()

def point(point, r, fillc, strokec):
    gsave()
    gs = revert()
    p = projection2d(point)
    p = gs.transform(p)
    translate(p)
    newpath()
    circle(0,0,r)
    if fillc != None:
        fill(fillc)
    if strokec != None:
        stroke(strokec)
    grestore()

def distance(u,v):
    d = vsub(u,v)
    return math.sqrt(dot(d,d))

def vadd(u, v):
    r = []
    for i in range(len(u)):
        r.append(u[i]+v[i])
    return r

def vsub(u, v):
    r = []
    for i in range(len(u)):
        r.append(u[i]-v[i])
    return r

def smult(s, u):
    r = []
    for i in range(len(u)):
        r.append(u[i]*s)
    return r

def dot(u, v):
    r = 0
    for i in range(len(u)):
        r += u[i]*v[i]
    return r

def cross(u,v):
    r = [0]*3
    r[0] = u[1]*v[2] - u[2]*v[1]
    r[1] = u[2]*v[0] - u[0]*v[2]
    r[2] = u[0]*v[1] - u[1]*v[0]
    return r

def normalize(u):
    l = math.sqrt(dot(u,u))
    r = []
    for i in range(len(u)):
        r.append(u[i]/l)
    return r

def arc3d(u, v, r):
    u = normalize(u)
    v = normalize(v)
    theta = math.acos(dot(u, v))
    n = normalize(cross(u, v))
    s = cross(n, u)
    N = 100
    dtheta = theta/N
    theta = 0
    points = []
    points.append(smult(r,u))
    newpath()
    moveto3d(u)
    for i in range(N):
        theta += dtheta
        p = vadd(smult(r*math.cos(theta), u),
                 smult(r*math.sin(theta), s))
        lineto3d(p)
        points.append(p)
    return points

def grid(origin, v1, v2, s, t):
    for i in range(s+1):
        moveto3d(vadd(origin, smult(i, v1)))
        rlineto3d(smult(t, v2))
    for j in range(t+1):
        moveto3d(vadd(origin, smult(j, v2)))
        rlineto3d(smult(s, v1))

def symgrid(origin, v1, v2, s, t):
    for i in range(-s, s+1):
        moveto3d(vadd(vadd(origin, smult(i, v1)), smult(-t,v2)))
        rlineto3d(smult(2*t, v2))
    for j in range(-t,t+1):
        moveto3d(vadd(vadd(origin, smult(j, v2)),smult(-s,v1)))
        rlineto3d(smult(2*s, v1))

def decorateAxis(start, direction, length, tickPositions, tickGeometry,
                 labels, labelAlignment, labelOffset):
    newpath()
    moveto3d(start)
    rlineto3d(smult(length, direction))
    stroke()

    labelPositions = []
    for tick in tickPositions:
        position = vadd(start, smult(tick, direction))
        labelPositions.append(position)
        gsave()
        gs = revert()
        p = projection2d(position)
        p = gs.transform(p)
        translate(p)
        newpath()
        moveto(tickGeometry[0])
        lineto(tickGeometry[1])
        stroke()
        grestore()

    for i in range(len(labels)):
        Label(labels[i], labelPositions[i], alignment = labelAlignment, offset = labelOffset).draw()

def tofig(p):
    return [p[1], p[2], p[0]]

def graph(f, bbox, M, N, c):
    dx = (bbox[2]-bbox[0])/float(M)
    dy = (bbox[3]-bbox[1])/float(N)
    faces = []
    x = bbox[0]
    for i in range(M):
        y = bbox[1]
        for j in range(N):
            p0 = tofig([x,y,f(x,y)])
            p1 = tofig([x+dx, y, f(x+dx,y)])
            p2 = tofig([x+dx, y+dy, f(x+dx, y+dy)])
            p3 = tofig([x, y+dy, f(x, y+dy)])
            faces.append(Face([p0, p1, p2, p3], c))
            y += dy
        x += dx
    return ConvexSurface(faces)

def spacecurve(r, domain, N):
    newpath()
    dt = (domain[1]-domain[0])/float(N)
    t = domain[0]
    moveto3d(tofig(r(t)))
    for i in range(N):
        t += dt
        lineto3d(tofig(r(t)))

def angle2d(p,q):
    p = projection2d(p)
    q = projection2d(q)
    return math.atan2(q[1]-p[1], q[0]-p[0])


        

