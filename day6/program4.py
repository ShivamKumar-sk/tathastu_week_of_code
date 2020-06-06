def nextgreater(num,n):
     for i in range(n-1,0,-1): 
         if num[i] > num[i-1]: 
             break
              
     if i == 1 and num[i] <= num[i-1]: 
         print ("not possible")
         return

     x = num[i-1] 
     smallest = i 
     for j in range(i+1,n): 
         if num[j] > x and num[j] < num[smallest]: 
             smallest = j 
           
     num[smallest],num[i-1] = num[i-1], num[smallest] 
       
     x = 0
     for j in range(i): 
         x = x * 10 + num[j] 
       

     num = sorted(num[i:]) 

     for j in range(n-i): 
         x = x * 10 + num[j] 
       
     print( "Next number is:",x )
n=input()
number=[]
for i in n:
    i=int(i)
    number.append(i)
nextgreater(number,len(n))
