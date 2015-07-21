
from swampy.TurtleWorld import *
import regpol
World = TurtleWorld()
bob=Turtle()
bob.delay=0.01
def circle(t,r):
    t=Turtle()
    d=2*r
    circum=3.14*d
    l= circum/(d)
    regpol.square(t,16*l,r/2)



circle(bob,100)

    
    
