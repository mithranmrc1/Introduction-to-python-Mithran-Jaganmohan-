answer=["a","b","c","d"]
correct=["a","c","c","d"]
score=0
for a,b in zip(answer,correct):
    if(a==b):
        score+=1
print(f"score= {score}/4")

scores = [12, 17, 9, 15, 14]
best = -1
bestpos = 0
for pos, s in enumerate (scores, start=1) :
    if s > best:
      best = s
      bestpos = pos
print (f"Best: {best} (student # {bestpos} ) ")