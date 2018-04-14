
# coding: utf-8

# In[ ]:


class ClassPropertyDescr():
    """
    Класс дескриптор для функции
    get - функция используемая для получения значений атрибутов
    
    """

    def __init__(self, fget, fset=None):
        self.fget = fget
        self.fset = fset

    def __get__(self, instance, owner):
        return self.fget.__get__(instance, owner)()

    def __set__(self, obj, value):
        return self.fset.__get__(obj, type(obj))(value)

    def setter(self, func):
        self.fset = func
        return self


def prop(func):
    """
    Декоратор 
    :param func: func класса
    :return: дескрипотор func
    """
    return ClassPropertyDescr(func)


class For_Something:
    """
    Просто класс
    """

    def __init__(self, x):
        self.x = x

    @prop
    def attr(self):
        """
        Return square of a x
        :return: square of a x
        """
        return self.x * 3

    @attr.setter
    def attr_setter(self, update):
        self.x = update
        return


if __name__ == '__main__':
    s = For_Something(2)
    print(s.attr)
    s.attr=5
    print(s.attr)

