from fig3d import *

init3d("coordinates-3d", 110, 110)
beginpage()

seteye([0.7, 0.5, 0.8, 0])
#setlight([0,20,10, 0])

newpath()
center()
translate(0,-15)
scale(50,60,70)

moveto3d(0,0,0)
lineto3d(1,0,0)
moveto3d(0,0,0)
lineto3d(0,1,0)
moveto3d(0,0,0)
lineto3d(0,0,1)
stroke()

Label(r"$y$", [1,0,0], alignment="lb", offset=[-3,3]).draw()
Label(r"$z$", [0,1,0], alignment="lt", offset=[3,-3]).draw()
Label(r"$x$", [0,0,1], alignment="rb", offset=[-3,3]).draw()


finish()
endpage()
