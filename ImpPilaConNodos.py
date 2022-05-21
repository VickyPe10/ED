from dataclasses import dataclass

class Stack():
    @dataclass # decorador para definir una data class
    class _Node:
        value: any #any representa cualquier tipo
        anterior: '_Node'
    
    __slots__ = ['_top'] #el atributo top es el puntero inicial de la lista que va a contener los elementos de la pila.

    def __init__(self, iterable):
        self._top = None
        if iterable is not None:
            for value in iterable:
                self.push(value)
    
    def __len__(self): # funcion para saber el tamaño de la pila
        n = 0
        node = self._top
        while node is not None:
            node = node.anterior
            n += 1
        return n
    
    def is_empty(self): # es vacia
        return self._top is None

    @property
    def top(self):
        assert not self.is_empty(), 'Pila sin elementos'
        return self._top.value
    
    def push(self, value):
        self._top = Stack._Node(value, self._top) # agrego el valor al nodo nuevo, en la izquierda queda el nuevo valor y en siguiente, el valor que antes estaba en el tope
    
    def pop(self):
        assert not self.is_empty(), 'Pila sin elementos'
        value = self._top.value # guardo el valor que está en el tope
        self._top = self._top.prev # ahora el tope, es el valor que estaba en el nodo siguiente
        return value
    
    def copy(self):
        newStack = Stack() #creo la nueva pila
        if not self.is_empty(): #si la pila no es vacia
            node = self._top #variable aux que guarda el primer valor de mi pila
            newNode = Stack._Node(node.value, None) #creo nuevo nodo que tiene el valor inicial de mi pila y el siguiente en none
            newStack._top = newNode #el tope de mi nueva pila (copia) tiene el valor de newNode
            while node.anterior is not None: #mientras el valor siguiente a mi nodo no sea None
                node = node.anterior #corro la variable aux 
                newNode.anterior = Stack._Node(node.value, None) #el valor siguiente de mi newNode ya no es none, ahora es lo que tiene guardado node
                newNode = newNode.anterior 
        return newStack
    
    def clear(self):
        self._top = None
    
    def __eq__(self, otraPila):
        x = self._top
        y = otraPila._top
        while x is not None and y is not None:
            if x.value != y.value:
                return False
            x = x.anterior # recorrer ambas pilas e ir comparando sus elementos
            y = y.anterior
        return x is None and y is None #solo ocurre si ambas pilas son iguales
    
    def __repr__(self):
        values = []
        node = self._top
        while node is not None:
            values.insert(0, node.value)
            node = node.anterior
        return 'Stack([' + ', '.join(repr(x) for x in values) + '])'