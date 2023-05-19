t=int(input())
sum=0
l=list(map(int,input().split()))
for i in range(len(l)):
    if(l[i]%2!=0):
        sum=sum+l[i]
print(sum)