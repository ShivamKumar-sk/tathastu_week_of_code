str='ABAABCD'
Lst=[]
for i in range(len(str)):
    for j in range(i+1,len(str)):
        if str[i]==str[j]:
            Lst.append(str[i:j+1])
string=''
for i in Lst:
    if i==i[::-1] and len(i)>len(string):
        string=i
print('Maximum length reversed string is:',string)    
            
                   
               
        
        
    
    
    
    
        
    
    
        
