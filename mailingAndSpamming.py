import os, time, random
listOfEmail = ["qwe","asdfgh","12345","ash","1234567890","0987654321","qwertyuiop","poiuytrewq","mnbvcxzz","lkjhgfdsa","zxcvhj","1z2x3c","4vv5b6n77m","m0m0m09mnnn99nn9n0","77777777","88888888","w4yb546456b4","vvvccvcvcvcvv","weweeweweeweww"]

listOfContent = ["random content 1","some other content","im too lazy to writte it, sorry","bllablablablablabla","it\'s beeen a loooooooonngg daaayyy without you my frieeeend","random email \#3456789283764536728","sth some text some more some letters here and some letters there","ok i think that\'s enough for a list of random stuff",]

def emailContentGenerator():
  content = listOfContent[random.randint(1,(len(listOfContent)-1))]
  return content

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): 
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(1)

def spamming():
  for index in range(10):
    os.system("clear")
    content = emailContentGenerator()
    print (f"""Email {index+1}

    Dear {listOfEmail[index]}
    
    {content}""")
    time.sleep(2)

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint() 
  elif menu == "4":
    spamming()
  time.sleep(1)
  os.system("clear")