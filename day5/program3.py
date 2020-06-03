c=0
def Stole(x):
    if c%2==0:
        max_value=sorted(x)[-1]
    return max_value
        
t=int(input('enter number of houses:'))
Lst=[]
for i in range(t):
    x=[int(x) for x in (input('enter values in houses:').split())]
    Lst.append(Stole(x))
print('maximum stolen value is:',sorted(Lst)[-1])
