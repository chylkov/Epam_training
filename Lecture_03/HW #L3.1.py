
# coding: utf-8

# In[ ]:

def decorator_with_args(decorator_to_enhance):
    """
    Эта функция является декоратором и написана для декораторов.
    Она должна декорировать другую функцию, которая должна быть декоратором.

    """
 
    def decorator_maker(*args, **kwargs):
        # создадим декоратор, который принимает как аргумент только функцию
        def decorator_wrapper(func):
 
            '''        
            декоратор должен быть именно такого типа
            decorator(func, *args, **kwargs)
            '''  

            return decorator_to_enhance(func, *args, **kwargs)
 
        return decorator_wrapper
 
    return decorator_maker


@decorator_with_args
def decorated_decorator(func, *args, **kwargs):
    def wrapper(function_arg1, function_arg2):
        print ("Новая комбинация...:" + str(args) + str(kwargs))
        return func(function_arg1, function_arg2)
    return wrapper



@decorated_decorator(1, 2, 3)
def decorated_function(function_arg1, function_arg2):
    print ("Сектор " + str(function_arg1) + str(function_arg2)) 
    

decorated_function("5", " и 8")

