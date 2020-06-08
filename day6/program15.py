arr=[int(arr) for arr in input('enter values:').split()]
s=0
k=0
res=0
for i in range(len(arr)):
    x=i
    s=arr[0:i]
    k=arr[i+1:]
    s=sorted(s)
    k=sorted(k)
    if len(s)>0 and len(k)>0:
        if s[-1]<=arr[x] and k[0]>=arr[x]:
            res=x
            print(arr[x])
            break
    
    
        
