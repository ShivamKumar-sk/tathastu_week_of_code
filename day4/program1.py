tup=tuple([(tup) for tup in input('enter elements of tuple:').split()])
n=(input('enter an element to count occurence: '))
c=0
if n in tup:
    for i in tup:
        if i==n:
            c+=1
    print(c)
else:
    print('element is not in tuple')
