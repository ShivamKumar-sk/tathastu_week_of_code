def ac(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ac(m-1,1)
    elif m>0 and n>0:
        return ac(m-1,ac(m,n-1))
m,n=map(int,input().split())
print(ac(m,n))
