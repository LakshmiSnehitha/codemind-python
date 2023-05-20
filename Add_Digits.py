a=int(input())
s=0
while(a!=0):
    c=a%10
    s=s+c
    a=a//10
    if(a==0 and s>9):
        a=s
        s=0
print(s)