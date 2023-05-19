t=int(input())
c=0
l=list(map(int,input().split()))
for i in range(len(l)):
    c=c+l[i]
    r=c/t
print("%0.2f"%r)