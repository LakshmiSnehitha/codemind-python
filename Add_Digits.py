t=int(input())
s=0
while(t!=0):
    c=t%10
    s=s+c
    t=t//10
    if(t==0 and s>9):
        t=s
        s=0
print(s)
    