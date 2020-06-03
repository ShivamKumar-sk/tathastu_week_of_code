def replace(num,k):
    for i in n:
        if i!=k:        
            num=num.replace(i,k)
    return int(num)
        

n=int(input('enter an integer value:'))
num=str(n)
n=list(str(n))
if len(n)%2==0:
    l=len(n)//2
else:
    l=(len(n)//2)+1
max=n[l]
for i in range(l,len(n)):
    if n[i]>max:
        max=n[i]
print('finally value is:',replace(num,max))
