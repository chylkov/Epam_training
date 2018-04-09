
# coding: utf-8

# In[ ]:

# Homework
import random

class MatrixError(Exception):
    """ An exception class for Matrix """
    pass

class Matrix:
    
    """
    Класс матриц. Матрицу можно задавать двумя способами:
    1) задать количество строк и количество столбцов, тогда матрица создается случайным образом, 
    где каждый элемент матрицы будет равномерно распределен на интервале от -100 до 100
    
    2) задать матрицу в виде списка
    
    
    """
    
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
        
        else:
            raise MatrixError("Use another way to make matrix")
            
            
    def __add__(self, other):
            
        """
        Сложение матриц
   
        """
        if self.number_rows != other.number_rows:
            raise MatrixError("Trying to add matrixes of varying rank!")
        else:
            value = []
            for i in range(self.number_rows):
                row=[]
                for j in range(self.number_columns):
                    row.append(self.value[i][j] + other.value[i][j])
                value.append(row)     

            return Matrix(value)


                

            
            
    def __sub__(self, other):
        
        """
        Вычитание матриц
   
        """
        value = []
        for i in range(self.number_rows):
            row=[]
            for j in range(self.number_columns):
                row.append(self.value[i][j] - other.value[i][j])
            value.append(row)     

        return Matrix(value)
    
    
    def __mul__(self, other):
        
        """
        Умножение матрицы на матрицу или умножение матрицы на число (слева на право)
   
        """
        value = []
        if str(other).isdigit():
 
            for i in range(self.number_rows):
                row=[]
                for j in range(self.number_columns):

                    row.append(self.value[i][j] *other)
                value.append(row)
            return Matrix(value)
                
        elif self.number_columns == other.number_rows :
            
            for i in range(self.number_rows):
                row=[]
                for j in range(other.number_columns):
                    summa = 0
                    for k in range(self.number_columns):
                        summa = summa + self.value[i][k] * other.value[k][j]
                    row.append(summa)   

                value.append(row)
                
            return Matrix(value)
        else:
            raise MatrixError("Check the size of matrix")
        
        
    
    
    
    def __rmul__(self, other):
        
        """
        Умножение матрицы на матрицу или умножение числа на матрицу (справа на лево)
   
        """
        value = []
        if str(other).isdigit():
 
            for i in range(self.number_rows):
                row=[]
                for j in range(self.number_columns):

                    row.append(self.value[i][j] *other)
                value.append(row)     

        return Matrix(value) 
    

    def __eq__(self, other):
        
        """
        Проверка равны ли две матрицы
   
        """
        for i in range(self.number_rows):
            for j in range(self.number_columns):
                if self.value[i][j] != other.value[i][j]:
                    return False
                    break
    
        else:
            return True
            
        
        
    def is_squared(self):
        
        """
        Проверка является ли матрица квадратной
   
        """
        if self.number_columns == self.number_rows:
            return True
        else:
            return False
        
    def is_symmetric(self):
        
        """
        Проверка является ли квадратная матрица симметричной
   
        """
        if self.number_rows != self.number_columns:
            raise MatrixError("Matrix is not squared")
        
        else:
            for i in range(self.number_rows):
                for j in range(self.number_columns):
                    if self.value[i][j] != self.value[j][i]:
                        return False
                        break
                        

            else:
                return True

        
        
    def transp(self):
        
        """
        Транспонирование матрицы
   
        """
        value = []
        for i in range(self.number_columns):
            row=[]
            for j in range(self.number_rows):
                row.append(self.value[j][i])
            value.append(row)     

        return Matrix(value)
        

