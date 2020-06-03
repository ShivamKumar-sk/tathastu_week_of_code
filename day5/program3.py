
def Stole(x,c):
    if c%2==0:
        max_value=sorted(x)[-1]
        return max_value
    else:
        return 0
        
t=int(input('enter number of houses:'))
Lst=[]
c=0
for i in range(t):
    x=[int(x) for x in (input('enter values in houses:').split())]
    k=Stole(x,c)
    c+=1
    Lst.append(k)
print('maximum stolen value is:',sorted(Lst)[-1])
