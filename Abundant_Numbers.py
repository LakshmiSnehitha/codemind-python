n=int(input())
fact=1
s=0
for i in range(1,n):
    if(n%i==0):
        s=s+i
if(s>n):
    print("True")
else:
    print("False")
    