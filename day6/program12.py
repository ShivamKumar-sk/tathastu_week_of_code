x=input('enter strings:').split()
x=list(x)
Lst=[]
for i in x[0]:
    Lst.append(i)
for i in x:
    for j in Lst:
        if j in i:
            if Lst.index(j)!=i.index(j):
                Lst.remove(j)
        else:
            Lst.remove(j)
sum=''
for i in Lst:
    sum=sum+i   
print('max prefix is:'sum)        
        
        
    
        
