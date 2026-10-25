temps = [1,2,3,4,5,6,7]
for t in temps:
    if t==4:
        continue
    print("Temp :",t)
for i in range(100,200):
    if i%7==0:
        print("the first multiple of 7:",i)
        break
print("Search over")