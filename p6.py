import random
l=["s1","s2","s3","s4","s5"]
l1=[]
for i in range(5):
    s=random.sample(l,5)
    if s not in l1:
      l1.append(s)
for i in range(5):
    for j in range(5):
        print(l1[i][j],end=" ")
    print() 