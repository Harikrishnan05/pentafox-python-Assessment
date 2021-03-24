l=list(map(int,input().split(",")))
s=""
for i in range(len(l)):
    s+=chr(l[i]+64)
print(s)