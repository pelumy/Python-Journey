'''
a = 1
while a <5:
    a += 1
    if a == 3:
        break
    print(a)
for i in range(1,6):
    print(i)

else:
    print(' All iterations completed')

print((lambda a,b: a+b) (4,6))
'''

def stringy(size):
    # Good Luck!
    for i in range(0,size+1):
        if i == (i%2 == 0):
            return '0'
        else:
            return '1'
    return ''.join(i)
print(stringy(5))

pala = ['a', 'b', 'c', 'd']
for i, j in enumerate(pala):
    print(i,j)
    