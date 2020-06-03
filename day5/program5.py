def even(x):
    lst1=[]
    for i in x:
        if i%2==0:
            lst1.append(i)
    return sorted(lst1)

def odd(k):
    lst2=[]
    for i in k:
        if i%2!=0:
            lst2.append(i)
    return sorted(lst2)
    


x=[int(x) for x in input('enter integers:').split()]
a=even(x)
b=odd(x)
k=[]
for i in range(len(b)-1,-1,-1):
    k.append(b[i])
    print('Finally the sorted array is:',k+a)
