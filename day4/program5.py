name=[(name) for name in input('enter the names of candidates:').split()]
votes={}
lst=[]
for i in name:
    k=int(input('enter no. of votes:'))
    votes[i]=k
    lst.append(k)
lst=sorted(lst)
c=0
Lst={}
for i in lst:
    if i==lst[-1]:
        c+=1
k=[]
if c==1:
    for i,j in votes.items():
        if lst[-1]==j:
            print(i,'won the election' )
else:
    for i ,j in votes.items():
        if j==lst[-1]:
            Lst[i]=len(i)
            k.append(len(i))
k=sorted(k)           
for i,j in Lst.items():
    if j==k[0]:
        print(i,'won the selection')
        
