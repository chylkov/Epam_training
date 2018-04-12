
# coding: utf-8

# In[ ]:


# Task L6.3

n = int(input('Number of pairs '))
pairs =[]
for i in range(n):
    pairs.append(input().split())

for pair in pairs:
    try:
        print(int(pair[0])/int(pair[1]))
      
        
    except ZeroDivisionError :
        print('Error code: integer division or module by zero')
        
    except ValueError :
        print("Error code: invalid literal for int() with base 10: '$'")

