n=4
m=8
k=7
c=0
while(n>0):
    for i in range(m):
        if i==c or k-c==i:
            print('*',end='')
        else:
            print(' ',end='')
    c+=1
    n-=1
    print('\n')
c=3
m=8
k=7
n=0
while(n!=4):
    for i in range(m):
        if i==c or k-c==i:
            print('*',end='')
        else:
            print(' ',end='')
    c-=1
    n+=1
    print('\n')
    
        
