import time
import os
print()
print()
print("Welkom")
print("Please identify yourself")
identity = input("> ")
print()
print("Welcome" + identity)
time.sleep(0.5)
print()
print("Level 2 Access Clearance Granted")
print()
time.sleep(1)
while True:
    print()
    print("----------------------------------------------")
    print("Files Object 145")
    print()
    print("         Interview 1")
    print("         Interview 2 (Level 5 Access Required)")
    print("         Interview 3 (Level 5 Access Required)")
    choise = input("[1,2,3] ")
    choise = interview.lower()
    if choise == "1":
        print()
        print("This interview was taken when 145 wanted to join for a programing group named █████. All irrelvant infomation has been removed")
        print()
        print("Date of Recording: ██-██-2019")
        print()
        print("[BEGIN RECORD")
        print()
        print("Interviewer: Hallo, ")
        print("145: Eh ja, mijn naam is Tim")
       print("Interviewer: Dus Tim, vertel me iets over je zelf.")
        print("145: Ehm.. oke, ik ben 18 jaar, ik woon op █████ ██████ in Purmerend samen met mijn moeder, broertje en stief vader.")
        print("Interviewer: Nog iets anders?")
       print("145: Bedoel je hobby's of zo iets?")
        print("145: Ik freerun graag samen met mijn neef, eh.. ik zit op nog op judo, daar ga ik elke donderdag naar toe.")
        print("Interviewer: Zijn er nog andere dingen die ik over je zouden moeten weten?")
        print("145: Ja, ik heb autisme en tourette waardoor ik soms rare bewegingen of geluiden kan maken.")
        print("Interviewer: Oke, dat was het voor nu.")
        print()
        print("[END RECORD]")
        os.system("pause")
    elif choise == "2" or choise == "3":
        print()
        print("You don't have Permision to Access this file")
        time.sleep(1)
        continue
    else:
        continue