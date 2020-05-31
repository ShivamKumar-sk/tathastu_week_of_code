def oddeven(n):
    if n%2!=0:
        return 'ODD'
    else:
        return 'EVEN'

def Prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 'Prime'
    else:
        return 'Not Prime'

def Palindrome(n):
    i=n
    rev=0
    while(i>0):
        d=i%10
        rev=rev*10+d
        i=i//10
    if rev==n:
        return 'Palindrome'
    else:
        return 'Not Palindrome'
def arm(n):
    n=str(n)
    sum=0
    for i in n:
        i=int(i)
        sum=sum+i*i*i
    if sum==int(n):
        return 'Armstrong'
    else:
        return 'Not Armstrong'
        
        
        
n=int(input('enter a number: '))
oe=oddeven(n)
p=Prime(n)
pal=Palindrome(n)
a=arm(n)
print('Given number is',oe)
print('Given number is',pal)
print('Given number is',p)
print('Given number is',a)
