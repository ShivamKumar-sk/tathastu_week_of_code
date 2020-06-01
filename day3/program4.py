def duplicates(lst):
    Lst=[]
    for i in lst:
        if i not in Lst:
            Lst.append(i)
    return Lst


lst=[lst for lst in input('enter item of a list :').split()]
Lst=duplicates(lst)
print(Lst)

