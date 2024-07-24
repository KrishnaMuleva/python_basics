'''for i in range(1,6):

   for j in range(1,i+1):
        print(j, end=' ')
   print('')'''

'''n=int(input("please enter a no.:"))
for x in range (1,n+1):
    z=n+1-x
    if x<=n/2:
        for y in range(1,x+1):
            print (y,end='')
    else:
        for y in range(1,z+1):
            print(y,end='')
    print('')'''

'''n=int(input('please enter a no.:'))
a=int(n/2)
for x in range (1,a+1):
    for y in range (1,x+1):
        print(y,end='')
    print('')
for x in reversed(range(1,a+1)):
    for y in range(1,x+1):
        print(y,end='')
    print('')'''

n=int(input("please enter a no.:"))
for x in range (1,n+1):
    a=n-x
    for y in range(1,a+1):
        print(' ',end='')
    for y in range(x,0,-1):
        print(y,end='')
    for y in range(1,x+1):
        if y==1:continue
        print(y,end='')
    print('')
for x in range (n-1,0,-1):
    a=n-x
    for y in range(1,a+1):
        print(' ',end='')
    for y in range(x,0,-1):
        print(y,end='')
    for y in range(1,x+1):
        if y==1:continue
        print(y,end='')
    print('')

