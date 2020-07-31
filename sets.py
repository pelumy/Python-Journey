set1 = {1,2,3,'a', 'b', 'c'}
set2 ={1,5,7,'c', 'a',3}
print(set1 | set2)
print(set1 & set2)
print(set2 - set1)
print(set1 ^ set2)
'''
myset = set( ('fish', 'meat', 'pepper', 'noodles', 'flakes') )
print(myset)
myset.add('chicken')
print(myset)
myset.update(['plaintain','periperi'])
myset.remove('fish')
print(myset)
'''
set3 =set1.symmetric_difference_update(set2)
print(set3)