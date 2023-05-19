t=int(input())
s=0
p=1
while(t!=0):
    c=t%10
    s=s+c
    p=p*c
    t=t//10
if(p==s):
    print("Spy Number")
else:
    print("Not Spy Number")
    