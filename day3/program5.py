def interSection(lst1,lst2):
    Lst=[]
    for i in lst1:
        if i in lst2:
            Lst.append(i)
    return Lst


lst1=[lst1 for lst1 in input('enter items list1 :').split()]
lst2=[lst2 for lst2 in input('enter items list2 :').split()]
Lst=interSection(lst1,lst2)
print('intersection of two list is:',Lst)

