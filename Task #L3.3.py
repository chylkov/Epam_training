
# coding: utf-8

# In[ ]:

def validate(low_bound, upper_bound):
 
    def my_decorator(func):

        def wrapped(arg):
            for value in arg:
                if value < low_bound or value > upper_bound:
                    print('Function call is not valid!')
                    break
            else:
                print('Pixel created!')

            return func(arg)
 
        return wrapped
 
    return my_decorator

@validate(low_bound = 0, upper_bound = 256)
def set_pixel(pixel):
    pass

set_pixel((2,3,4))
    

