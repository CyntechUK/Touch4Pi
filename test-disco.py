import pitouch
from time import sleep
from random import randint

pit = pitouch.PiTouch()

pit.all(0)


while True:
  pit.red(randint(0,100),randint(1,4))
#  pit.all(0)
  pit.green(randint(0,100),randint(1,4))
#  pit.all(0)
  pit.blue(randint(0,100),randint(1,4))
#  pit.all(0)
  sleep(0.01)
