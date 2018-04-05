
# coding: utf-8

# In[ ]:

def translate2(text):
    
    '''
    Функция переводит строку в число
    На вход подается символьная строка (текст)
    Функция берет каждый символ и переводит его в позицию кода в Юникоде
    На выходе получается число
    
    Если на вход подать пустую строку, функция выведет 0
    
    >>> translate2('abcd')  
    979899100
    
    
    '''

    if len(text) == 1:
        return ord(text[-1])
    elif len(text) == 0:
        return 0
    else:
      
        digit = 1
        while ord(text[-1]) // digit != 0:
            digit = digit * 10
            
        number = ord(text[-1])  + translate2(text[:-1])* digit
        return number
    

