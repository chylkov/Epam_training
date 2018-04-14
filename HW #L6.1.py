
# coding: utf-8

# In[ ]:


import abc
import functools
import decimal as dc

dc.Context(prec=10, rounding=dc.ROUND_HALF_UP)

class CurrencyDescr:
    """
    Дескриптор для атрибура value класса Сurrecncy
    """
    def __init__(self, label):
        self.label = label


    def __get__(self, instance, owner):
        return (instance.__dict__[self.label] / instance.course).quantize(dc.Decimal('.01'))


    def __set__(self, instance, value):
        instance.__dict__[self.label] = dc.Decimal(value * instance.course)


class course_dec(dc.Decimal):
    """
    Класстопределяющий метод call
    """
    def __call__(self, cls):
        return dc.Decimal(self / cls.course).quantize(dc.Decimal('.01'))


    def __repr__(self):
        return str(self.quantize(dc.Decimal('.01')))

    def __str__(self):
        return str(self.quantize(dc.Decimal('.01')))


class CourseDescr:
    """
    Дескриптор для course
    """
    def __init__(self):
        self.value = course_dec(0)


    def __get__(self, instance, owner):
        return self.value


    def __set__(self, instance, value):
        self.value = course_dec(value)


@functools.total_ordering
class Currency:
    """
    Абстрактный класс валюты.
    Все значения в валюте dollar
    value - количество
    """
    value = CurrencyDescr('value')

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value) + self.get_sign()

    def __str__(self):
        return str(self.value) + self.get_sign()

    @abc.abstractmethod
    def get_sign(self):
        """
        Возвращает знак валюты
        :return: str
        """
        pass

    def to(self, cls):
        """
        Переводит валюту в валюту класса cls
        :param cls: класс наследуемый от Currency
        :return: instance: экземпляр класса наследуемый от Currency
        """
        if issubclass(cls, Currency):
            # инициализируем экземмляр
            curr = cls(0)
            # копируем значение value
            curr.__dict__['value'] = Currency.get_real_value(self)
            return curr
        else:
            raise TypeError(f"Invalid type {type(other)}")

    @staticmethod
    def get_real_value(instance):
        """
        Возвращает истинное значение value  в dollar
        :param instance: экземпляр класс
        :return: value: Decimal
        """
        if 'value' in instance.__dict__:
            return instance.__dict__['value']
        else:
            raise TypeError("Invalid type")

    def __add__(self, other):
        if isinstance(other, Currency):
            sum_res = Currency.get_real_value(self) + Currency.get_real_value(other)
            res = Dollar(sum_res)
            return res.to(self.__class__)
        else:
            raise TypeError(f"Invalid type {type(other)}")

    def __radd__(self, other):
        if type(other) == (int) and other == 0:
            return self.to(self.__class__)
        else:
            raise TypeError(f"Invalid type {type(other)}.")

    def __sub__(self, other):
        if isinstance(other, Currency):
            sum_res = Currency.get_real_value(self) - Currency.get_real_value(other)
            res = Dollar(sum_res)
            return res.to(self.__class__)
        else:
            raise TypeError(f"Invalid type {type(other)}")

    def __mul__(self, other):
        try:
            val=self.value*other
        except TypeError as e:
            print(e,"Invalid format")
        else:
            return self.__class__(val)


    def __rmul__(self, other):
        try:
            val=self.value*other
        except TypeError as e:
            print(e,"Invalid format")
        else:
            return self.__class__(val)

    def __truediv__(self,other):
        try:
            val=self.value/other
        except TypeError as e:
            print(e,"Invalid format")
        except ZeroDivisionError as e:
            print(e,"Invalid format")
        else:
            return self.__class__(val)

    @functools.total_ordering
    def __eq__(self, other):
        if isinstance(other, Currency):
            return Currency.get_real_value(self) == Currency.get_real_value(other)
        else:
            raise TypeError(f"Invalid type {type(other)}")


    def __lt__(self, other):
        if isinstance(other, Currency):
            return Currency.get_real_value(self) < Currency.get_real_value(other)
        else:
            raise TypeError(f"Invalid type {type(other)}")


class Dollar(Currency):
    """
    Класс валюты Доллар
    """
    default_init=False
    course = CourseDescr()

    def __init__(self, value):
        if not self.default_init:
            self.course = 1
            self.default_init = True
        self.value = value


    def get_sign(self):
        return " $"


class Euro(Currency):
    """
    Класс валюты Евро
    """
    # общий курс  для всех экземпларов
    course = CourseDescr()
    # была ли иниализация
    default_init = False

    def __init__(self, value):
        if not self.default_init:
            self.course = 1.2
            self.default_init = True
        self.value = value


    def get_sign(self):
        return " €"


class Ruble(Currency):
    """
    Класс валюты Рубль
    """
    # общий курс  для всех экземпларов
    course = CourseDescr()
    # была ли иниализация
    default_init = False

    def __init__(self, value):
        if not self.default_init:
            self.course = 0.02
            self.default_init = True
        self.value = value

    def get_sign(self):
        return " ₽"

