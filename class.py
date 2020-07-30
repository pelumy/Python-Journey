# class Person:
#     "This is a person class"
#     age = 10

#     def greet(self):
#         print('Hello')

# print (Person.age)
# print (Person.greet)

# harry = Person()
# print(harry.greet)
# harry.greet()

# class ComplexNumber:
#     def __init__(self, r=0, i=0):
#         self.real = r
#         self.imag = i
#     def get_data(self):
#         print(f'{self.real}+{self.imag}j')

# num1 = ComplexNumber(2,3)
# num1.get_data()
# num2 = ComplexNumber(5)
# num2.attr = 10
# print((num2.real, num2.imag, num2.attr))

# del num1.imag
# num1.get_data()

class Car:
    def __init__(self,#color,model
    ):
        # self.color = color
        # self.model = model
        self.engine = 'off'

    def start_engine(self):
        # if self.engine == 'off':
            print('Starting engine')
            self.engine ='on'
        # else:
        #     print ('Engine has already started running!')

    def stop_engine(self):
        # if self.engine == 'on':
            print('Stopping engine')
            self.engine = 'off'
        # else:
        #     print('Engine is already off')

    # def display_cars(self):
    #     print(self.color)
    #     print(self.model)
    #     print(f'The engine is {self.engine}')
    def drive(self):
        if self.engine:
            print('Driving the car')
        else:
            print('You need to start the car first')
        

# mycar = Car('gold', 'Benz')
# print(mycar.color)
# print(mycar.model)
# mycar.start_engine()
# mycar.display_cars()
# mycar.stop_engine()
# mycar.display_cars()

class BlueCar:
    color ='blue'

class Honda(Car, BlueCar):
    #pass
    model = 'Honda Civic'

    
    def start_engine(self):
        super().start_engine()
        print('dri my Honda')
        

car = Honda()
print(car)
car.start_engine()
car.drive()
car.stop_engine()
print(car.model)
car.start_engine()
print(car.color)
