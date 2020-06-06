x=[float(x) for x in input('enter real numbers:').split()]
a=0
b=0
c=0
x.sort()
for i in x:
    for j in x:
        for k in x:
            if i+j+k>1 and i+j+k<2:
                a=i
                b=j
                c=k
print('Triplet is:',a,b,c)                
