n=int(input('enter the length of fibonacci:'))
Lst=[]
sum=1
a=0
b=1
t=0
Lst.append(a)
Lst.append(b)
for i in range(2,n):
    t=a+b
    a=b
    b=t
    sum=sum+t
while(True):
    if t>=sum:
        break
    t=a+b
    a=b
    b=t
    Lst.append(t)
if sum in Lst:
    print('Yes')
else:
    print('Not')
