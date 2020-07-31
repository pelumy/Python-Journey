'''
list1 =[1,2,3,4,5]
list2 = [6,7,'a']
list1+=list2
print(list1)
list1.append('tumi')
print(list1)
list3 = ['buzzy', 'olly', 'miko']
list1.extend(list3)
print(list1)
list1.insert(5, 'sardine')
print(list1)
list1.remove(list1[5])
print(list1)
list1.pop(2)
print(list1)
list4 = [1,9,0,25,67]
list4.reverse()
print(list4)
print(list1.count('buzzy'))
print(list1.index(5))
list4.clear()
print(list4)
del list4
print(list4)
'''
list1 = [[[0]*3]*3]*3
print(list1)

# list comprehension
list2 =[i  for i in range(5)]
print(list2)

list3 = [x+y  for x in 'abc'  for y in '123']
print(list3)

fruits =['apple', 'mango', 'banana', 'pear']
first_letters = [fruit[0]  for fruit in fruits ]
print((first_letters))

two_dim = [ [0]*3  for i in range(3) ]
print(two_dim)

numbers = [1,2,3,4,5,6]
