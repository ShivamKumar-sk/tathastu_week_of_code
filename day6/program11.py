x=[int(x) for x in input('enter integers:').split()]
x.sort()
print('Highest product is:',x[-1]*x[-2]*x[-3])
