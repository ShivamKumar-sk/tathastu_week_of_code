n=3
r=5
while(n>0 and r>0):
    for j in range(0,r):
        if j%2!=0:
            print('*',end='')
        else:
            print(n,end='')
    print('\n')
    n-=1
    r-=2
a=3
b=5
x=1
y=0
while(x<=a and y<b):
    for i in range(y+1):
        if i%2!=0:
            print('*',end='')
        else:
            print(x,end='')
    print('\n')
    x+=1
    y+=2
        
    
