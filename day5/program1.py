def replace(num):
    num=str(num)
    num=num.replace('0','5')
    return int(num)
        

n=int(input('enter an integer value:'))
print('finally value is:',replace(n))
