def lic(x,y):
    if(x>y):
        g=x
    else:
        g=y
    while(True):
        if((g%x==0) and(g%y==0)):
            lcm=g
            break
        g=g+1
    return lcm
a,b=map(int,input().split())
print(lic(a,b))