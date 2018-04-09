
# coding: utf-8

# In[ ]:

# Homework
import random

class Matrix:
    def __init__(self, arg1 = None, arg2 = None):

               
        if (arg1 is not None) and (arg2 is not None) :
            value =[]
            for i in range(arg1):
                row=[]
                for j in range(arg2):
                    row.append(random.randint(-100, 100))
                value.append(row)
                
            self.number_rows = arg1
            self.number_columns = arg2
            self.value = value
                
        elif type(arg1) == list and arg2 is None:
            self.value = arg1
            self.number_rows = len(arg1)
            self.number_columns = len(arg1[0])
            
            
    def __add__(self, other):
        if self.number_rows == other.number_rows:
            value = []
            for i in range(self.number_rows):
                row=[]
                for j in range(self.number_columns):
                    row.append(self.value[i][j] + other.value[i][j])
                value.append(row)     

            return Matrix(value)
        else:
            print("Matrixes must be the same size")
            
            
    def __sub__(self, other):
        value = []
        for i in range(self.number_rows):
            row=[]
            for j in range(self.number_columns):
                row.append(self.value[i][j] - other.value[i][j])
            value.append(row)     

        return Matrix(value)
    
    
    def __mul__(self, other):
        value = []
        if str(other).isdigit():
 
            for i in range(self.number_rows):
                row=[]
                for j in range(self.number_columns):

                    row.append(self.value[i][j] *other)
                value.append(row)     

        return Matrix(value)
    
    def __rmul__(self, other):
        value = []
        if str(other).isdigit():
 
            for i in range(self.number_rows):
                row=[]
                for j in range(self.number_columns):

                    row.append(self.value[i][j] *other)
                value.append(row)     

        return Matrix(value) 
    

    def __eq__(self, other):
        for i in range(self.number_rows):
            for j in range(self.number_columns):
                if self.value[i][j] != other.value[i][j]:
                    break
                    
            return True
        
        else:
            return False
        
        
    def is_squared(self):
        if self.number_columns == self.number_rows:
            return True
        else:
            return False
        
    def is_symmetric(self):
        if self.number_columns == self.number_rows:
            for i in range(self.number_rows):
                for j in range(self.number_columns):
                    if self.value[i][j] == self.value[j][i]:
                        break

                return False

            else:
                return True
        else:
            return "Matrix is not squared"
        
        
    def transp(self):
        value = []
        for i in range(self.number_columns):
            row=[]
            for j in range(self.number_rows):
                row.append(self.value[j][i])
            value.append(row)     

        return Matrix(value)
        

