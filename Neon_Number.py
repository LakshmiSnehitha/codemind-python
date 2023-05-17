a=int(input())
c=a**2
sum=0
while(c!=0):
    b=c%10
    sum=sum+b
    c=c//10
if(sum==a):
    print("Neon Number")
else:
    print("Not Neon Number")