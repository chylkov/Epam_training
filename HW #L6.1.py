
# coding: utf-8

# In[ ]:

# HW #L6.1

import abc

class Сurrency(metaclass=abc.ABCMeta):
    
    def __init__(self):
        pass

        
    
    @abstractmethod
    def course():
        pass
    
     
    
class Euro(Сurrency):
    def __init__(self):
        super(Сurrency, self).__init__()

class Dollar(Сurrency):
    def __init__(self):
        super(Сurrency, self).__init__()
        
class Ruble(Сurrency):
    def __init__(self):
        super(Сurrency, self).__init__()

