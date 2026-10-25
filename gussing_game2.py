import random

secret=random.randint(1,10)
attempt=0
while attempt<=5:
    a=int(input("Guess the Number :"))
    if(a==secret):
        print("Bravo! u found it")
    elif(a<secret):
        print("Too Low")
    else:
        print("Too High")

    attempt+=1
if(a!=secret):
    print("U Lost! get out")
