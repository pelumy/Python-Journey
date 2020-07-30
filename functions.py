import example
def greet(name):
    '''greets the person passed in as a parameter'''
    print(f'Hello, {name}. Good morning')

greet('Itunu')
print (greet ('May'))

def absolute_value(num):
    '''returns abs value of entered number'''
    if num>=0:
        return num
    else:
        return -num

print (absolute_value(2))

def my_func():
    x = 10
    print('value inside function:', x)

x=20
my_func()
print('Value outside function:', x)

#Function Arguments
def gree (name, msg = 'Good morning!'):
    '''
    Greets the name assigned
    if no msg is stated, it defaults to "good morning"
    '''
    print(f'Hello {name}, {msg}')

gree(msg= 'How do you do', name ='Kate')

#arbitrary args
def arb(*names):
    '''greets all names assigned'''
    for name in names:
        print(f'hello {name}')

arb('Monica', 'Luke', 'Steve', 'John')

#recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(4))

#anonymous/lambda fnx
double = lambda x: x*2
print(double(5))

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2==0), my_list))
print(new_list)

#module
mod = example.add(4,5.5)
print (mod)
print(dir(example))
print(dir())

def outer():
    first_num = 1
    def inner():
        first_num = 0
        second_num = 1
        print('inner - second_num is: ', second_num)
    inner()
    print('outer - first_num is: ', first_num)

    
outer()

def oute():
    first_num = 1
    def inne():
        nonlocal first_num
        first_num = 0
        second_num = 1
        print(f'inner- second is {second_num}')
    inne()
    print(f'outer - first is {first_num}')

oute()

def sum_list(mylist):
    list_sum = 0
    for items in mylist:
        list_sum += items
    return list_sum

lis = [1,2,3,4,5,6,7,8,9,10]
print(sum_list(lis))

def contains_a(string, el):
    count = 0
    for i in string:
        if (i == el):
            count+=1
    return count

the_string = 'saandala'
print(contains_a(the_string, 'a')) 

def contains_letter(myl, letter):
    for i in myl:
        if (i == letter):
            continue
        print(f'yes, the list contains letter {i}')


print(contains_letter([1,2,3,4,4,5], 4))

number = 'sas'
# while number in range (0,15):
if(number == number[::-1]):
    print(number)
        # number += 2