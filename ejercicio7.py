
import array

import ctypes

class Array(object):
    """
    Implementation of the array data structure
    """

    def __init__(self, n):
        """
        Initialize the class
        """
        self.l = 0
        self.n = n
        self.array = self._create_array(self.n)        
    
    def _create_array(self, n):
        """
        Creates a new array of capacity n
        """
        return (n * ctypes.py_object)()
        

class Array(Array):
    def __getitem__(self, item_index):
        """
        Return element at item_index
        """
        if (item_index < 0) or (item_index >= self.n):
            raise IndexError('index out of range!')
        try:
            x = self.array[item_index]
        except ValueError:
            x = None
        return x
    
    def __setitem__(self, item_index, item):
        """
        Set element at item_index
        """
        if (item_index < 0) or (item_index >= self.n):
            raise IndexError('index out of range!')
        self.array[item_index] = item   


class Array(Array):
    
    def __init__(self, n, values=None):
        self.l = 0
        self.n = n
        self.array = self._create_array(self.n)
        if values:
            self.initialize_array(values)
            
    def initialize_array(self, values):
        """
        Initialize array
        """
        if self.n != len(values):
            raise ValueError("element count different than capacity")
        for item in values:
            self.array[self.l] = item
            self.l += 1
            
    def list_array(self):
        """
        List elements of the array
        using list comprehension
        """
        return ", ".join(str(x) if x is not None else '_' for x in self)       


class Array(Array):
    def insert_to_tail(self, item):
        """
        Add new item to the tail of the array
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        self.array[self.l] = item
        self.l += 1

class Array(Array):
    def insert_to_tail(self, item):
        """
        Add new item to the tail of the array
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        self.array[self.l] = item
        self.l += 1          

class Array(Array):
    def insert_to_head(self, item):
        """
        Add new item to the beginning of the array
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        i = self.l
        while (i > 0):
            self.array[i] = self.array[i-1]
            i -= 1
        self.array[0] = item
        self.l += 1
        
class Array(Array):
    def insert(self, index, element):
        """
        implementation of insert
        """
        if self.l == self.n:
            raise ValueError("no more capacity")
        if (index < 0) or (index > self.l):
            raise IndexError('index out of range!')
        x = self.l
        while x > index:
            self.array[x] = self.array[x-1]
            x -= 1
        self.array[index] = element
        self.l += 1

class Array(Array):
    def linear_search(self, element):
        """
        Return the index of element
        """
        for i in range(self.l):
            if self[i] == element:
                return i
        return None        



 ##Remove the element at the first position
class Array(Array): 
    def remove_first(self):
    #simplemente para eliminar el primero hay que mover todos los datos hacia la izquierda linea 143
        x = 0
        while x < self.n-1:      # x crece hasta ser igual al ultimo valor dentro de la lista array            
            self.array[x] = self.array[x+1] 
            x = x+1
   #el ultimo elemento en el array original ya no existe 
    #reduce el tamano del array
        self.array[self.l-1] = None   
        self.l -= 1

  ##Remover posicion especifica dentro del array
class Array(Array): 
    def remove_Index(self, index): 

        # sirve para verificar si el indice ingresado previamente en la funcion esta dentro del rango 
        if self.l == self.n:
            raise ValueError("no more capacity")
        if (index < 0) or (index > self.n-1):
            raise IndexError('index out of range!')
        #mueve los datos hacia la izquierda 1 posicion, como en la funcion remove first 
        x = index
        while x < self.n-1:                 
            self.array[x] = self.array[x+1]  # movemos todos los valores una posicion hacia la izquierda comenzando en el indice  
            x = x+1

#el ultimo elemento en el array original es null
    #reduce el tamano del array
        self.array[self.l-1] = None   
        self.l -= 1
  

#Remover el ultimo elemento en la lista
class Array(Array): 
    def remove_Last(self): 
        self.array[self.l-1] = None   
        self.l -= 1

       
  



if __name__ == '__main__':
    
    # implementar un array de tamanio 5
    A = Array(5)
    A[0] = 1     # A.__setitem__(0,0)
    A[1] = 2     # A.__setitem__(1,2)
    A[2] = 3
    A[3] = 4
    A[4] = 5
    print(A.list_array())

    A.remove_Last()
    print(A.list_array())
    A.remove_first()
    print(A.list_array())
    A.remove_Index(2)
    print(A.list_array())