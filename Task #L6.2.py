
# coding: utf-8

# In[ ]:

# Task L6.2

import abc

class Vehicle(metaclass=abc.ABCMeta):
    
    def __init__(self, year_made, model, number_wheels, base_price, mileage, price):
        self.year_made = year_made
        self.model = model
        self.number_wheels = number_wheels
        self.base_price = base_price
        self.mileage = mileage
        
    
    @abstractmethod
    def vehicle_type():
        pass
    
    @abstractmethod
    def is_motorcycle(self):
        pass     
    
    @abstractproperty
    def purchase_price(self):
        self.price = self.base_price - 0.1 * self.mileage
        
    
    
class Truck(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__(year_made, model, number_wheels, base_price, mileage, price)

class Car(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__(year_made, model, number_wheels, base_price, mileage, price)
        
class Motocycle(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__(year_made, model, number_wheels, base_price, mileage, price)

class Bus(Vehicle):
    def __init__(self):
        super(Vehicle, self).__init__(year_made, model, number_wheels, base_price, mileage, price)

