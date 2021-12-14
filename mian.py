

önskelista=input("""
many:
1)skapa önskelista
2)läs upp önskelista
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
        f.readlines(y)