def Knapsack(lst,bag,W):
    v=0
    for i in range(len(lst)-1,-1,-1):
        for k,j in bag.items():
            if lst[i]==j and W>0:
                W=W-k[1]
                v=v+k[0]
    return v
    
    

    
n,W=map(int,input().split())
bag={}
lst=[]
for i in range(n):
    v,w=map(int,input('enter value and weight:').split())
    bag[v,w]=v/w
    lst.append(v/w)
lst=sorted(lst)
for i,j in bag.items():
    if lst[-1]==j:
        if i[1]>W:
            value=j*W
            print('value of the weight in Knapsack:',value)
        elif i[1]==W:
            value=i[0]
            print('value of the weight in Knapsack:',value)
        else:
            value = Knapsack(lst,bag,W)
            print('value of the weight in Knapsack:',value)            
            
