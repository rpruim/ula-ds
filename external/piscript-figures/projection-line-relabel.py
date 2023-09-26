from figures import *
from Vectors import Vector as Vec

width = 150
height = width
margin = 5

# proj(b -> v) = k v

for scale in [1, 8, 10, 12]:
      beginfigure("projection-line-relabel" + str(scale), width+2*margin, height+2*margin)

      setupcoordinates([margin, margin, width+margin, height+margin],
                  [-1,-1,5,5])
      scale /= 10.0
      x = Vec([2,1])
      y = Vec([2,4])
      k = float(y * x) / float(x * x)
      proj = x * k
      k *= scale 
      kx = k * x
      perp = y - proj
      overshoot = 2.1 * x

      # Grid([-1,1,5], [-1,1,5]).draw()

      settexenv("ACTexConfig")

      axes = Axes()
      axes.setticks([-1,1,5],[-1,1,5])
      # axes.setlabels([0,2,5], [0,2,5])
      axes.draw()
      axes.drawticks()
      # axes.drawlabels()

      Graph(Function(lambda x: 0.5*x), color=blue).draw()

      if scale > 0.2: 
            Line(proj, y, color = lightgray).draw()
            Vector(kx, fillcolor=lightblue).fill()
            Vector(y, tail = kx, fillcolor = lightred).fill()
            Label(r"${k \boldsymbol v}$", 0.8 * proj, alignment="lt", offset=[4,-4], color = lightblue).draw()
            Label(r"${\boldsymbol b} - k {\boldsymbol v}$", kx + 0.5 * (y - kx), color = lightred, alignment="lb", offset=[4,0]).draw()

      Vector(x, fillcolor=black).fill()
      Vector(y, fillcolor=black).fill()

      Label(r"${\boldsymbol b}$", y * 0.75, alignment="rb", offset=[-4,4]).draw()
      Label(r"${\boldsymbol v}$", x * 0.75, alignment="lt", offset=[4,-4]).draw()
      Label(r"${\theta}$", [.5,.5], alignment="lb", offset=[0,0]).draw()

      endfigure()

