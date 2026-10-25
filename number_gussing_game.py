import random
secret=random.randint(1,10)
a=int(input("Guess the number : "))

while a!=secret:
    if a<secret:
        print("Too low")
        break
    else:
        print("Too High")
        a=int(input("Guess the number : "))
print(f"Bravo! it was: {secret}")