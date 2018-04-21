
# coding: utf-8

# In[ ]:


#Task 1
        
    
def union(*args):
    U =set()
    for m in args:
        for s in m:
            if s not in U:
                U.add(s)             
    return U


def intersect(*args):
    I = set()
    
    #set_user = set(s)
  #  I = set_user
    for m in args:
        for s in m:
            include = True
            for n in args:
                if s not in n:
                    include = False
                    break
            if include == True:
                I.add(s)
            
    return I

