import os, time
listOfEmail = []

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): # len counts how many items in a list
    print(f"{index+1}: {listOfEmail[index]}") 
  time.sleep(1)


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
    time.sleep(1)
    os.system("clear")
  
  elif menu == "4":
    print()
    for index in range(len(listOfEmail)):
      print(f'\033[33mEmail {index + 1}: {listOfEmail[index]}')
      time.sleep(2)
    os.system('clear')
        
    print()
    for index in range(len(listOfEmail)):
      time.sleep(2)
      print(f'\033[32mEmail {index + 1}')
      print()
      print(f'''Dear {listOfEmail[index]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,
I am Spammington III\033[0m''')
      time.sleep(13)
      os.system('clear')