'''
ninja_belt ={
    'crystal' : 'red',
    'ryu' : 'black'
}

print(ninja_belt['crystal'])
print(ninja_belt['ryu'])
print('crystal' in ninja_belt)
print(list(ninja_belt.keys()))
val = list(ninja_belt.values())
print(val)
print(val.count('red'))
print(val.count('black'))
ninja_belt['yoshi'] = 'red'
print(list(ninja_belt.values()))
print(val)
val = list(ninja_belt.values())
print(val)
print(val.count('red'))

person = dict(name = 'itunu', age = 25, food ='beans')
print(person)
'''
dict1 ={}
print(type(dict1))
dict1 =dict([ (1,'apple'), (2, 'burger')   ])
print(dict1)

dict2 = dict1.get(1)
print(dict2)
print(dict1[2])

cubes = {1:1, 2:8, 3:21, 4:64, 5:125}
total = 0
for i in cubes:
    total += cubes[i]
print(total)

dict3 = {'Brand':'gucci', 'Industry':'fashion', 'year':1921}
dict3['Industry'] = 'makeup'
print(dict3)
dict3 ['color'] = 'blue'
print(dict3)

# deleting dict

# remove one item
dict3.pop('year')
print (dict3)
del cubes[1]
print(cubes)

# remove random item
print(cubes.popitem())

# clear all items
cubes.clear()
print(cubes)

# del all dict
del cubes
# print cubes

if 'industry' in dict3:
     print('true')
else:
    print('false')