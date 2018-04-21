
# coding: utf-8

# In[ ]:

import time

def my_time_new_decorator(function_to_decorate):
    # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
    # получая возможность исполнять произвольный код до и после неё.
    def the_wrapper_around_the_original_function():
        start_time = time.time()
        function_to_decorate() # Сама функция
        end_time = time.time()
        spend_time = end_time - start_time
        return spend_time
    # Вернём эту функцию
    return the_wrapper_around_the_original_function


@my_time_new_decorator
def another_stand_alone_function():
    time.sleep(3) #это здесь для того, чтобы ответ бы не нулевым (долго выполняемую функцию придумывать было лень)
    m = 0
    for i in range(100):
        m = m + i**50
        
    return(m)


another_stand_alone_function()
    

