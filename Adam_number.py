n=int(input())
t=n**2 #144
rev=0
re=0
while(n!=0):
    c=n%10
    rev=rev*10+c
    n=n//10
d=rev**2
while(d!=0):
    e=d%10
    re=re*10+e
    d=d//10
if(re==t):
    print("True")
else:
    print("False")
