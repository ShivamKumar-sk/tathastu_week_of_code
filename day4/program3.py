t=int(input('enter no. of values in a dictionary:'))
dict={}
for i in range(t):
    key,value=input().split()
    value=int(value)
    dict[key]=value
lst=[]
for i,j in dict.items():
    lst.append(j)
lst=sorted(lst)  
k=lst[-2]
for i,j in dict.items():
    if j==k:
        l=i
print('second maximum value in dictionary is:',l,':',k)
    
