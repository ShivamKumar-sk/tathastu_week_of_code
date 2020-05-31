n=int(input())
a=0
b=1
print(a,b,end=' ')
c=2
for i in range(n):
    k=a+b
    a=b
    print(k,end=' ')
    c+=1
    b=k
    if c==n:
        break
    
    
    
