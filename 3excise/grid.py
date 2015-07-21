def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)



def beam():
    print "+ - - - -",

def beam_s():
    do_four(beam)
    print "+"

def pillar():
    print "|" + " "*8,

def pillar_s():
    do_four(pillar)
    print "|"
   
    

def grid():
    beam_s()
    do_four(pillar_s)
    beam_s()
    do_four(pillar_s)
    


do_twice(grid)
