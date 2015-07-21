from swampy.TurtleWorld import *

world=TurtleWorld()
t=Turtle()
def draw_koch(t,x):
    if x>3:
        draw_koch(t,x/3)
        lt(t,60)
        draw_koch(t,x/3)
        rt(t,120)
        draw_koch(t,x/3)
        lt(t,60)
        draw_koch(t,x/3)
    else:
        fd(t,x)
        return

draw_koch(t,100)
