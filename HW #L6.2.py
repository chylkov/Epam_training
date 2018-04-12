
# coding: utf-8

# In[ ]:

# HW #L6.2

class Something:
    def _init__(self, x):
        self.x = x
        
    @prop
    def attr(self):
        return self.x ** 2
    
s = Something(10)
s.attr

