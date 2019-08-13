import random as r
l=[]
for n in range(1000):
    r.seed(int(r.random()*100000))
    l.insert(len(l),int(r.random()*10000000))
l.sort()
print(l)
