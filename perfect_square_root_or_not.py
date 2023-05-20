n=int(input())
s=0
for i in range (1,n+1):
    if(n==i*i):
        s=i*i
if(n==s):
        print("True")
else:
    print("False")