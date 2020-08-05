def concat_dict():
    keys =['Ten', 'Twenty','Thirty']
    values = [10,20,30]
    dic =dict(zip(keys, values))
    return dic
print(concat_dict())

def merge_dict():
    dict1 ={'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Forty': 40, 'Fifty': 50, 'sixty':60}
    dict3 ={**dict1, **dict2}
    #dict3 = dict1.copy()
    #dict3.update(dict2)
    return dict3
print(merge_dict())

# access key value
sampleDict ={
    'student':{'name': 'Mike',
    'marks':{'physics':70, 'history': 80}}
}
d= sampleDict['student']['marks']['history']
print(d)

# initialize dict from default value
employees = ['kelly','emma','john']
defaults = {'designation':'application developer', 'salary':8000}
init_dict = dict.fromkeys(employees, defaults)
print(init_dict['kelly'])

# creating new dict by extracting from another dict
the_dict ={
    'name': 'kelly',
    'age': 25,
    'salary': 8000,
    'city':'New York'
}
keys = ['name','salary']
new_dict = {k: the_dict[k] for k in keys}
print(new_dict)

# delete set of keys in dict
another_dict ={
    'name': 'kelly',
    'age': 25,
    'salary': 8000,
    'city':'New York'
}
another_key = ['name','salary']
del_key = {k:another_dict[k] for k in another_dict.keys() - another_key}
print(del_key)

# check if value exists in dict
check = {'a':100, 'b':200, 'c': 300}
print(200 in check.values())

# renaming a key
rename = {
    'name': 'kelly',
    'age': 25,
    'salary': 8000,
    'city':'New York'
}
rename['location'] = rename.pop('city')
print(rename)

# get key corresponding to the min value
min_dict ={
    'physics':82,
    'math':65,
    'history':75
}
the_min = min(min_dict, key = min_dict.get)
print(the_min)

# changing dict value name
change ={
    'emp1':{'name':'john', 'salary':7500},
    'emp2':{'name':'emma', 'salary':8000},
    'emp3':{'name':'brad', 'salary':6500}
}
change['emp3']['salary'] =8000
print(change)