#Russian Mafia is watching
import time
username=str(input("Enter username:"))
if username in ["Aleksei", "Miko", "Jeremy", "Asla"]:
  password=str(input("Enter password:"))
  if password in ["JoelSux.qwerty"]:
    print("Access granted. Welcome, Russian Mafia!")
    print(" What do You wish to do?")
    print("   1. Interfere in American Presedential Election?")
    print("   2. Blow up Central Europe?")
    print("   3. Or eat donuts?")
    option=str(input("Choose an option from the list:"))
    if option in ["1"]:
      code1=str(input("Enter access code:"))
      if code1 in ["JoelSux.1234"]:
        print("Firewall has been succesfully broken. Interfering in Presidential Election...")
        print("11%")
        print("25%")
        print("49%")
        print("67%")
        print("82%")
        print("99%")
        print("100%")
        print("Hack succesfully complete. Mission ended. Cleaning up the traces.")
      else: 
        print("Incorrect access code. You Suck!")
    if option in ["2"]:
      code2=str(input("Enter security code to Tsar-Bomba:"))
      if code2 in ["JoelSux.1234"]:
        print("0%")
        print("11%")
        print("25%")
        print("49%")
        print("67%")
        print("82%")
        print("99%")
        print("100%")
        donuts=str(input("Missiles launched, Central Europe succesfuly destroyed in 5. 4. 3. 2. 1. Boom! Would u like donuts?"))
        if donuts in ["Yes", "yes", "YES", "Sure"]:
          print("Hacking online donuts store in progress. Hack completed. Free donuts will be delivered in 5. 4. 3. 2. 1. Enjoy!")
        else:
          print("Yeah, pizza is better.")
      else:
        print("Incorrect access code. You Suck!")
    if option in ["3"]:
      code3=str(input("Enter access code to best Donuts:"))
      if code3 in ["JoelSux.1234"]:
        print("Hacking online donuts store in progress. Hack completed. Free donuts will be delivered in 5. 4. 3. 2. 1. Enjoy!")
      else:
        print("Incorrect access code. You Suck!")
    elif option in ["Alfa"]:
      alfacode=str(input("For launching Operation Alfa, enter the secret code:"))
      if alfacode in ["007290"]:
        print("Fingerprint needed.Fingerprint needed.Fingerprint needed.")
        time.sleep(5)
        print("\nFingerprint matched.\nOperation Alfa launched.\n5.\n4.\n3.\n2.\n1.\nUniting countries to make new USSR.\nLaunching rockets towards 40.377937, -111.803055 (America) and 43.413029, 34.299316 (Europe).\nInvading Moon.\nLaunching top secret weapon.\nRevolution of the Galaxy has started.")
        print("...")
        time.sleep(18)
        print("\033[31m \nThe Galaxy is under Your total control, Stalin.\033[0m")        
      else:
        print("Incorrect password. Security protocol launched. Ending service connection. 01101010100011010.")
        
  else:
    print("Ha-ha, wrong password! You suck!")  
else:
  print("Access denied. You suck, %s!" % username)
