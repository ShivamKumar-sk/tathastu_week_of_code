k=int(input('enter the number of lists:'))
Lst=[]
for i in range(k):
    x=[int(x) for x in input().split()]
    Lst=Lst+x
print('one sorted lists is',sorted(Lst))
    
