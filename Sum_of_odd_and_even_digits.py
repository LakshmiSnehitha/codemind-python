t=int(input())
s=0
m=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if(i%2!=0):
        s=s+l[i]
    else:
        m=m+l[i]
c=abs(s-m)
if(c==0):
    print("YES")
else:
    print("NO")