from tabulate import tabulate
import time, os

def printCards():
  infoKeys = [{"NAME": name, **values} for name, values in myBeasts.items()]
  print (tabulate(infoKeys, headers = 'keys', tablefmt='fancy_grid'))

myBeasts = {}
keys = ['TYPE', 'SPECIAL MOVE', 'STARTING HP', 'STARTING MP']

while True:
  os.system("clear")
  print ("👾 PokéBeast - The Non-Copyright Generic Beast Battle Game")
  print ()
  NAME = input ("\033[35mInput your beast\'s name > \033[36m")
  info = {}
  for key in keys:
    info[key] = input(f"\033[35mInput your beast\'s {key.lower()} > \033[36m")
  myBeasts[NAME] = info
  time.sleep(0.5)
  print ()
  printCards()
  time.sleep(0.5)
  print ()
  menu = input ("Again? (y/n) > ")
  if menu == "y":
    continue
  else:
    break
    