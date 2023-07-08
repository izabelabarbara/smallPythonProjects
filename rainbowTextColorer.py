myString = input("type sth > ")
for letter in myString:
  if letter.lower() == "g":
    print ("\033[32m", end='')
  elif letter.lower() == "b":
    print ("\033[34m", end='')
  elif letter.lower() == "r":
    print ("\033[31m", end='')
  elif letter.lower() == "y":
    print ("\033[33m", end='')
  elif letter.lower() == "v":
    print ("\033[35m", end='')
  elif letter == " ":
    print("\033[0m", end='')

  print(letter, end='')
  