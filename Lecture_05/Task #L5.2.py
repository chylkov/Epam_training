
# coding: utf-8

# In[ ]:

#Task2
class SchoolMember: 
    
    """
    Класс который представляет любого человека в школе
    """    
    
    def __init__(self,name,age):
        
        """
        Инициализация члена школы (задается имя)
        """  
        
        self.name = name
        self.age = age 

class Teacher(SchoolMember):
    
    """
    Класс который представляет учителей школы (наследуется от класса SchoolMember)
    """   
    
    def __init__(self,name, age,  salary):
        
        """
        Метод инициализации учителя. Задается имя, возраст и зарплата
        """  
        
        self.salary = salary
        super().__init__(name, age)

        
    def show(self):
        
        """
        Вывод информации по учителю
        """
        
        print(f'Имя:"{self.name}" Возраст:"{self.age}" Зарплата:"{self.salary}"')

class Student(SchoolMember):
    """
    Класс который представляет учеников школы (наследуется от класса SchoolMember)
    """  
    
    def __init__(self,name, age, mark):
        
        """
        Метод инициализации ученика. Задается имя, возраст и оценка
        """  
        
        self.mark = mark
        super().__init__(name, age)
    
    def show(self):
        
        """
        Вывод информации по ученику
        """
        
        print(f'Имя:"{self.name}" Возраст:"{self.age}" Оценки:"{self.mark}"')

