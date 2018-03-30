
# coding: utf-8

# In[ ]:


def translate(text):
    number=0
    for b in text:
        if number == 0:
            number = ord(b)
        else: 
            r = 1
            while ord(b) // r != 0:
                r = r * 10
                
            number = number * r + ord(b)
                
    print(number)

translate('abcd')  

