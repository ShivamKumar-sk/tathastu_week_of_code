x=[int(x) for x in input().split()]
k=sorted(x)
count=x.index(k[0])
c=0
for i in range(len(k)):
    if k[i]==x[(i+count)%len(k)]:
        c+=1
if c==len(k):
    print('yes the array is sorted and rotated')
else:
    print('array is not sorted and rotated')
    
    
