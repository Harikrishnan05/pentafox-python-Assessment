s1=input()
cn=1
for i in range(len(s1)):
   if(i==len(s1)-1):
       if(cn>1):
           print(s1[i],end="")
           print(cn,end="")
       else:
          print(s1[i],end="")
       break
   if(s1[i]==s1[i+1]):
       cn+=1
   else:
       if(cn>1):
           print(s1[i],end="");
           print(cn,end="");
           cn=1
       else:
           print(s1[i],end="")