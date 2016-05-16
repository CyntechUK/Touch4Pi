import pitouch
from time import sleep

pit = pitouch.PiTouch()

pit.all(0)

for x in range(0,100):
  pit.all(x)
  sleep(0.04)

pit.all(0)

while True:
  if pit.read() == 1:
    pit.red(100,1)
    pit.blue(100,1)
    pit.green(100,1)
    loop = 1
  elif pit.read() == 2:
    pit.red(100,2)
    pit.blue(100,2)
    pit.green(100,2)
    loop = 1
  elif pit.read() == 3:
    pit.red(100,3)
    pit.blue(100,3)
    pit.green(100,3)
    loop = 1
  elif pit.read() == 4:
    pit.red(100,4)
    pit.blue(100,4)
    pit.green(100,4)
    loop = 1
  else:
    loop = 0

  if loop == 1:
    pit.all(0)
