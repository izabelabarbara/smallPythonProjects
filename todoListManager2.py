import os, time

todoList = []

def add():
  print ()
  item = input("What yould you like to add to the list? > ")
  if item in todoList:
    print ("But you already have it on your list1")
  else:
    todoList.append(item)
    print (f"I have added {item} to your list")
  print ()

def remove():
  print()
  item = input("What would you like to remove from your list? > ")
  if item in todoList:
    confirmation = input(f"Are you sure you want to remove {item} from your list? > ")
    if confirmation == "yes" or confirmation == "remove":
      todoList.remove(item)
      print(f"All done! I have removed {item} from your list.")
    else:
      print("I wouldn\'t do anything without your permission")
  else:
    print ("This wasn\'t even on your list.")
  print()

def view():
  print()
  if len(todoList) == 0:
    print("Your list is empty tho. Go ahead and add something")
  else:
    for index in range(len(todoList)):
      print(f"{index+1}. {todoList[index]}")
  print()

def menu():
  os.system("clear")
  menu = input ("Do you want to add, edit or view your list? > ")
  if menu == "add":
    add()
  elif menu == "edit":
    remove()
  elif menu == "view":
    view()
  else:
    print("I didn\'t quite get that...Try again?")
  time.sleep(2)

while True:
  menu()