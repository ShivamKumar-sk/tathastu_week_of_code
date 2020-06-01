def per(lst,str=''):
    Set=set(lst)
    slist=[]
    if len(Set)==1:
        str+=''.join(lst)
        return list([str])
    for i in Set:
        Lst=list(lst)
        s=str+i
        Lst.remove(i)
        slist.extend(per(Lst,s))
    return slist

str = input('enter a string:')
lst=per(list(str))
print(','.join(lst))
