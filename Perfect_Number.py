t=int(input())
c=0
for i in range(1,t):
    if(t%i==0):
        c=c+i
if(t==c):
    print("True")
else:
    print("False")