def do_twice(f,param):
  f(param)
  f(param)

def print_twice(string):
  print string
  print string

def do_four(f,param2):
  do_twice(f,param2)
  do_twice(f,param2)


do_four(print_twice,"spam")


  
