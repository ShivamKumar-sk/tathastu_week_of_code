def per(str):
    Lst=[]
    for i in str:
        if i not in Lst:
            Lst.append(i)
    return Lst
str = input('enter a string:')
string=''
for i in per(str):
    string=string+i
print(string)

