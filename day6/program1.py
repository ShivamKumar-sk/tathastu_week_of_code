str='ABAABCD'
Lst=[]
for i in str:
    if str.count(i)>1:
        Lst.append(i)
if len(Lst)%2!=0:
    print('we can remove',len(str)-len(Lst),'latters')
else:
    print('we can remove',1+len(str)-len(Lst),'latters')
    
    
    
    
        
    
    

