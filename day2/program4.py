n=11
c=5
j=0
while(j!=5):
    for i in range(n):
        if i>=c-j and i<=c+j:
            print(' ',end='')
        else:
            print('*',end='')
    print('\n')
    j+=1
j=4
while(j!=-1):
    for i in range(n):
        if i>=c-j and i<=c+j:
            print(' ',end='')
        else:
            print('*',end='')
    print('\n')
    j-=1
    
        
    
