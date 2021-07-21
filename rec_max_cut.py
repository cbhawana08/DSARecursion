def func(n,a,b,c):
    if n==0:
        return 0
    elif n<0:
        return -1
    na=n-a
    nb=n-b
    nc=n-c
    res=max(func(na,a,b,c),func(nb,a,b,c),func(nc,a,b,c))
    if res==-1:
        return -1
    return res+1
n=int(input())
a=int(input())
b=int(input())
c=int(input())
print(func(n,a,b,c))
