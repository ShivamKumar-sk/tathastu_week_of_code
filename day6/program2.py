x=[int(x) for x in input('enter integers:').split()]
for i in x:
    if i>1 or i<0:
        exit()
x.sort()
print('sorted list is:',x)

        
