t=int(input('enter no. of values in a dictionary:'))
dict={}
for i in range(t):
    key,value=input().split()
    value=int(value)
    dict[key]=value
lst=[]
r={}
for i,j in dict.items():
    if j not in lst:
        r[i]=j
    lst.append(j)
print('Finally dictionary is:',r)        
            
