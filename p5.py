w1=list(input())
w2=list(input())

w3=w1[0].lower()
w4=w2[0].lower()
if(w3==w4):
    w1.remove(w1[0])
    w2.remove(w2[0])

l1=w1
l2=w2


l3=[]
for i in l1:
    for j in l2:
        if(i==j):
            l3.append(j)

for i in l3:
    if i in l1:
        l1.remove(i)
    if i in l2:
        l2.remove(i)
l4=l1+l2
s=""
for i in l4:
    s+=i
print(s)
