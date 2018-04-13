
# coding: utf-8

# In[ ]:

import abc

class Vehicle(metaclass=abc.ABCMeta):
    """
    Абстрактный класс описывающий транспортное средство
    """
    def __init__(self, wheel, model, year, mileage, base_price):
        self.wheel = wheel
        self.year = year
        self.model = model
        self.mileage = mileage
        self.base_price = base_price

    @abc.abstractmethod
    def vehicle_type(self):
        """
        Абстрактная функция возвращающая тип транспортного средства
        :return: str
        """
        pass

    @property
    def is_motocycle(self):
        """
        Функция показывающая является ли тарнспортноесредство мотоциклом или нет
        :return:bool
        """
        return self.wheel == 2

    @property
    def price(self):
        """
        Рассчитывает стоимость транспортного средства
        """
        return self.base_price - 0.1 * self.mileage


class Car(Vehicle):
    """
    Класс машины
    """
    def __init__(self, model, year, mileage, base_price):
        super().__init__(4, model, year, mileage, base_price)


    def vehicle_type(self):
        return "Car"


class Motocycle(Vehicle):
    """
    Класс мотоцикла
    """
    def __init__(self, model, year, mileage, base_price):
        super().__init__(2, model, year, mileage, base_price)


    def vehicle_type(self):
        return "Motocycle"


class Truck(Vehicle):
    """
    Класс тягочей
    """
    def __init__(self, model, year, mileage, base_price):
        super().__init__(6, model, year, mileage, base_price)


    def vehicle_type(self):
        return "Truck"


class Bus(Vehicle):
    """
    Класс автобусов
    """
    def __init__(self, model, year, mileage, base_price):
        super().__init__(8, model, year, mileage, base_price)


    def vehicle_type(self):
        return "Bus"


if __name__ == '__main__':
    honda = Motocycle("Honda", 2018, 10000, 1 * 10e6)

    print("motocycle type: ", honda.vehicle_type())
    print("is motocycle: ", honda.is_motocycle)
    print("purchase: ", honda.price)

