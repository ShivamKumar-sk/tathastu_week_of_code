string=input('enter a string: ')
rev=''
for i in range(len(string)-1,-1,-1):
    rev=rev+string[i]
print('reversed string is:',rev)
