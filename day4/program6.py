dict=input('enter words:').split()
dict=list(dict)
arr=input('enter characters:').split()
arr=list(arr)
k=[]
for i in dict:
    c=0
    for j in i:
        if j in arr:
            c+=1
    if c==len(i):
        k.append(i)
print(k)
