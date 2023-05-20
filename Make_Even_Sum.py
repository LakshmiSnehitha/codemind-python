t=int(input())
s=0
l=list(map(int,input().split()))
for i in range(len(l)):
    s=s+l[i]
if(s%2==0):
    print("1")
else:
    print("0")