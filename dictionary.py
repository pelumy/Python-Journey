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