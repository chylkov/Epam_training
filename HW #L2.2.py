
# coding: utf-8

# In[1]:

from typing import NewType
from typing import Callable
import typing
function = Callable[..., list]

friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол', 'email': 'email@email.com'}, 
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол', 'email': 'email1@email1.com'},
    {'name': 'Петя', 'gender': 'Мужской', 'sport': 'Плавание', 'email': 'email2@email.com'}, 
    {'name': 'Аня', 'gender': 'Женский', 'sport': 'Баскетбол', 'email': 'email3@email1.com'}]
    

def select(*field_name: list):
    
    '''
    Функция на вход принимает названия полей через запятую
    На выходе возвращает список полей
    '''
    
    field_name_list = []
    for arg in field_name:
        field_name_list.append(arg)
        
    return field_name_list



def field_filter(field_name: str, *collection: list):
    
    '''
    Функция на вход принимает название поля и список значений по которому происходит фильтрация этого поля
    На выходе возвращает словарь с названием поля и значениямт по которым нужно фильровать 
    '''
    
    field_name_list = []
    for arg in collection:
        for field in arg:
            field_name_list.append(field)
    
    result = {field_name: field_name_list}
        
    return result



def query(collection: list, select: function, *field_filter: function) -> list:
    
    '''
    Функция на вход принимает 
    collection - набор данных в виде списка элементами которого являеются слвари
    select - набор поелей, по которым происходит вывод информации
    field_filter - набор словарей с названием поля и значениямт по которым нужно фильровать (может быть несколько)
    
    '''
    
    filtered_list =[]
    friend_list = []
    friend_list=collection
    filter_list = {}
    
    for arg in field_filter:
        filter_list.update(arg)
           
    
    for friend in friend_list:
        new_friend = {}
        for f in filter_list:

            if friend.get(f) not in filter_list.get(f):
                break
        else:
            for field in select:

                new_friend[field] = friend.get(field)                   
            filtered_list.append(new_friend)
    
    print(filtered_list)


# In[2]:

query(friends, select('name', 'gender', 'sport'), 
      field_filter('sport', [ 'Баскетбол']), field_filter('gender', [ 'Женский', 'Мужской']))


# In[ ]:



