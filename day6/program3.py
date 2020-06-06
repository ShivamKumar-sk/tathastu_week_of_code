n=[int(n) for n in input('enter integers:').split()]
n=sorted(n)
for i in range(len(n)):
    if i!=n[i]:
        k=i
        print('smallest missing no. is:',i)
        break
