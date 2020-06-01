Lst=[]
def Least(x,sum=0):
    for i in x:
        Lst.append(sum+i)
        y=list(x)
        y.remove(i)
        Least(y,sum+i)
    return Lst
    
x=[int(x) for x in input('enter integers: ').split()]
z=Least(x)
i=sorted(x)[0]
while(True):
    if i not in z:
        print('least integer is:',i)
        break
    else:
        i+=1

