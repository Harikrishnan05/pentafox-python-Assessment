L=list(map(int,input().split()))
s=int(input())
c1=0
c2=0
f=0
for i in range(len(L)):
    for j in range(i+1,len(L)):
        n=L[i]+L[j]
        print(n)
        if(n==s):
            f=1
            c1=L[i]
            c2=L[j]
            break
    
        n=0
    if (f==1):
        break
if (f==1):
    print(c1,",",c2)
else:
    print("No Pairs found")