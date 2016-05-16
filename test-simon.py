import pitouch
from time import sleep
from random import randint

pit = pitouch.PiTouch()
pit.all(0) # Reset LEDs

sequence = []
response = []
count = 0
go = 0
start = 1


def checkseq():
  global sequence, response
  print sequence
  print response
  x = 0
  while len(sequence) > len(response):
    response.append(pit.touch())
    print response
    if sequence[x] == response[x]:
      pit.blue(30)
      sleep(0.2)
      pit.all(0)
    else:
      gameover()
    x += 1
  if sequence == response:
    pit.green(100)
    sleep(0.3)
    pit.all(0)
    print "Carry on"
    response = []
  else:
    gameover()

def addtoseq():
  global sequence, count
  rand = randint(1,4)
  sequence.append(rand)

def playseq():
  for x in sequence:
    pad(x)
    sleep(1)
    pit.all(0)
    sleep(0.2)


def pad(num):
  if num == 1: # Green
    pit.all(0)
    pit.green(100,1)
  if num == 2: # Red
    pit.all(0)
    pit.red(100,2)
  if num == 3: # Yellow
    pit.all(0)
    pit.red(50,3)
    pit.green(100,3)
  if num == 4:
    pit.all(0)
    pit.blue(100,4)


def gameover():
  global start
  global go
  pit.red(100)
  go = 1
  start = 1

def gamestart():
  global start
  global count
  pad(1)
  sleep(1)
  pad(2)
  sleep(1)
  pad(3)
  sleep(1)
  pad(4)
  sleep(1)
  start = 0
  count = 0

def restart():
  global start, count, go, sequence, response
  start = 0
  count = 0
  go = 0
  sequence = []
  response = []
  pit.all(0)
  sleep(1)

while True:
  if go == 0:
    if start == 1:
      gamestart()
      pit.all(0)
      sleep(1)
    addtoseq()
    playseq()
    checkseq()

  else:
    raw_input("Game over, press enter to continue")
    restart()
#  print sequence
#  print "--"
#  addtoseq()
