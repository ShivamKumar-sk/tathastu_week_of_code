x=[int(x) for x in input().split()]
k=int(input())
if k>len(x)-1:
    exit()
for i in x:
    if x.count(i)>1:
        exit()
x.sort()
print(x[k-1])
    
    
    
