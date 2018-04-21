
# coding: utf-8

# In[ ]:


# Task L6.1
       
class Price():
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instanse, value):
        if value > 0 and value <= 100:
            self.value = value
        else:
            raise ValueError('Price must be between 0  and 100')
               
    def __delete__(self, instanse):
        del self.value
        

class Book():
    price = Price()
    
    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price

