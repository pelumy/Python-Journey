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