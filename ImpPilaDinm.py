class Stack():
    __slots__ = ["_datos"]

    def __init__(self, iterable):
        self._datos = [] # a partir del parámetro self. referencio a los atributos. 
                         # self._datos es un atributo: una lista que contiene todos los datos/elementos de mi pila.
        if iterable is not None: # si el parametro que le paso no es None,
            for dato in iterable: # por cada dato en el iterable,
                self.apilar(dato)   # agrego el dato a mi lista
    
    def is_empty(self): # funcion para saber si está vacia la pila
        return len(self._datos) == 0 # retorna 0 si la longitud de mi pila es == 0
    
    def __len__(self): # funcion para saber el tamaño de mi pila
        return len(self._datos)
    
    @property
    def tope(self):
        assert not self.is_empty(), 'Pila sin elementos' # Si la pila no tiene al menos un elemento muestra "Pila sin elementos"
        return self._datos[-1] # Si la pila tiene elementos muestra los datos desde el último ingresado
    
    def apilar(self, dato):
        self._datos.append(dato)

    def desapilar(self):
        assert not self.is_empty(), 'Pila sin elementos'
        return self._datos.desapilar()
    
    def clear(self): # permite vaciar la pila sin tener que desapilar elemento por elemento mientras que le pila no esté vacía
        self._datos.clear()
    
    def __eq__(self, otraPila): # Compara dos pilas
        return self._datos == otraPila._datos
    
    def __repr__(self): # Mostrar los elementos
        return ('Stack ([' + ', '.join(repr(x) for x in self._datos) + '])')