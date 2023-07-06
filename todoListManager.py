import time
todoList = []

def viewList():
  if len(todoList) == 0:
    print("\033[32mThere\'s nothing on your list yet\033[35m")
    print()
  else:
    count = 1
    for item in todoList:
      print(f"\033[34m{count}. {item}\033[35m")
      count +=1
    print()

def addToList():
  print()
  item = input("\033[35mWhat would you like to add to your list?: \033[0m")
  if item in todoList:
    print ("\033[32mOh, but you already have it on your list!\033[35m")
  else:
    todoList.append(item)
    print (f"\033[32mI have added {item} to your list.\033[35m")
  print()

def removeFromList():
  if len(todoList) == 0:
    print()
    print ("\033[32mBut you haven\'t added any tasks yet...\033[35m")
    print()
  else:
    print()
    item = input("\033[35mWhat task did you manage to complete?: ")
    if item in todoList:
      todoList.remove(item)
      print (f"\033[32mGreat! I have removed {item} from your list.\033[35m")
    else:
      print("\033[32mThis item wasn\'t even on your list.\033[35m")
    print()


def listMenu():
  time.sleep(0.5)
  menu = input("\033[35mDo you want to view, add or edit your list?: \033[0m")
  if menu == "add":
    addToList()
  elif menu == "edit":
    removeFromList()
  elif menu == "view":
    viewList()
  else:
    print ("\033[32mI didn\'t quite get that. Try again?\033[35m")
    print ()

while True:
  listMenu()
