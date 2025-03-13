def fun(x,y):
    if x > y:
        greater=x
    else:
        greater=y
    while(True):
        if((greater%x==0)and (greater%y==0)):# 54 not divise nby 24  so increment 55 55 57 58 59 6
            lcm=greater
            break
        greater +=1
    return lcm
n1=int(input("enter number"))
n2=int(input("enter number"))
print(fun(n1,n2))
