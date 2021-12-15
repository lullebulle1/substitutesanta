import time
import random
import os
def quit():
    os.exit
def clearconsol():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command='cls'
    os.system(command)


önskelista=input("""
many:
1)skapa önskelista
2)läs upp önskelista
3)naughty list 
""")

if "skapa önskelista" in önskelista:
    x=input("vad heter filen: ")
    with open(x,"w", encoding="utf8" ) as x:
        print("mata in vad dina barn heter: ")
        barn=input("barnets namn: ")
        x.write(barn+"\n")
        for pryl in range (10):
            pryl=input("lägg till sak, du kan max skriva 10 saker.: ")
            x.write(pryl+"\n")

if "läs upp önskelista" in önskelista:
    y=input("vad heter filen du vill läsa up: ")
    with open(y, "r", encoding="utf8") as f:
        time.sleep(2)
        print(f.read())

if "naughty list" in önskelista:
    list=input(f"is this the file you want to use: naughtylist.txt? ")
    if "yes" in list:
        print("this is the kid on the naughty list: ")
        with open("naughtylist.txt", "r", encoding="utf8") as naughtylist:
            print(naughtylist.read())
    else:
        quit()
add=input("do you want to adda to the naughty list?")
if "yes" in add:
    lol=" "
    with open("naughtylist.txt","a", encoding="utf8" ) as append:
        while True:
            lol=input("kids name, press space to stop: ")
            if " " in lol:
                print(naughtylist.read)
                break
            else:
                append.write(lol+"\n")
                pass
    time.sleep(1)
    with open("naughtylist.txt", "r", encoding="utf8") as naughtylist:
            print(naughtylist.read() + lol)

        
