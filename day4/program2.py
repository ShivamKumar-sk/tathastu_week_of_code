tup=tuple([(tup) for tup in input('enter elements of tuple:').split()])
lst=list(tup)
Lst=[]
l=len(lst)
while(len(Lst)!=l):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    Lst.append(min)
    lst.remove(min)
print('sorted tuple is:'tuple(Lst))
    
