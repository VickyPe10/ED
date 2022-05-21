class _Iterator():

    __slots__ ['_node', '_end']

    def __init__(self, head, end):
        self._node = head #inicio el iterador en el nodo head
        self._end = end #el nodo final es el que apunta al siguiente del ultimo (head)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._node is self._end: #si el nodo al que estoy apuntando es el head,
            raise StopIteration #termino la iteracion
        
        value = self._node.value #variable auxiliar que guarda el valor del nodo al que estoy apuntando
        self._node = self._node.next #corro el puntero al siguiente de mi nodo actual (avanzo en en la lista)
        return value #retorno el valor del puntero al que estoy apuntando

class _Coordinate():
    __slots__ = ['_node']

    def __init__(self, coordinateOrNode): #creo una coordenada
        if isinstance(coordinateOrNode, DoubleLinkedList._Coordinate): #si el valor que se da es una coordenada
            self._node = coordinateOrNode._node #se lo asigno a un nodo
        
        else:
            self._node = coordinateOrNode #si no, no referencia a ningun nodo
    
    @property
    def value (self): #retorno el valor de mi nodo
        return self._node.value
    
    @value.setter #permite modificar el valor del nodo
    def value (self,value): #modifico el valor del nodo redefiniendo el valor
        self._node.value = value

    def advance(self): #avanzo al siguiente nodo
        self._node = self._node.next

    def next(self): #retorno la coordenada que referencia al nodo siguiente 
        return DoubleLinkedList._Coordinate(self._node).advance()
    
    def retreat(self): #retrocedo al nodo anterior
        self._node = self._node.prev

    def prev(self): #retorna la coordenada que referencia al nodo anterior al actual
        return DoubleLinkedList._Coordinate(self._node).retreat()

    def __eq__(self, otherCoordinate): #dos coordenadas son iguales si referencian al mismo objeto
        return self._node is otherCoordinate._node
    
    def find(first, last, value): #buscar un objeto
        while first != last: #mientras el primero sea distinto del ultimo
            if first.value == value: #si el valor del primero es igual al valor buscado
                return first #devuelvo el primero
            
            first = first.next() #si el valor buscado no es el primero, avanzo 
        
        return last #retorno el ultimo en caso de que sea igual al valor buscado

class DoubleLinkedList():
    @dataclass
    class _Node: #nodos que guardan un valor, su anterior y su siguiente
        value: any
        prev: '_Node' = None
        next: '_Node' = None
    
    @dataclass
    class _Head: #nodo escondido que no almacena un valor (nodo que representa la cabeza de mi lista)
        prev: '_Node' = None
        next: '_Node' = None
    
    __slots__ = ['_head'] #atributo que hace referencia a la cabeza de la lista

    def __init__(self, iterable):
        self._head = DoubleLinkedList._Head() #creo el nodo cabeza de mi lista
        self._head.prev = self._head.next = self._head #el nodo tiene un anterior y un siguiente que son None

        if iterable is not None:
            for value in iterable:
                self.appendBack(value) #agrego el valor del iterable al final de la lista
        
    def __len__(self):
        n = 0 #contador de datos en mi lista
        nodo = self._head.next #puntero aux que apunta al valor siguiente de mi nodo cabecera 

        while nodo is not self._head: #si el nodo no es el cabecera
            n += 1 #aumento mi contador de datos
            nodo = nodo.next #avanzo el puntero 
        return n
    
    def is_empty(self):
        return self._head.next is self._head #retorno None si el unico nodo de mi lista es el cabecera (head)
    
        @property
        def front(self):
            assert not self.is_empty(), 'Lista vacía'
            return self._head.next.value #retorno el valor siguiente a mi head si la lista no está vacia
        
        @property
        def back(self):
            assert not self.is_empty(), 'Lista vacía'
            return self._head.prev.value #retorno el valor anterior a mi head si la lista no está vacia
    
    def appendFront(self, value): #inserto el valor que quiero antes del begin (primer nodo de la lista despues del head)
        self.insert(self.begin(),value)
    
    def appendBack(self, value): #inserto el valor que quiero al final de la lista (despues del end)
        self.insert(self.end(), value)
    
    def copy(self):
        newList = DoubleLinkedList() #creo una nueva lista enlazada doble
        act = newList._head #act guarda el nodo cabecera de mi nueva lista

        for value in self: #por cada valor en mi lista doble
            node = DoubleLinkedList._Node(value) #el puntero nodo apunta al valor del primer nodo de mi lista
            node.prev = act #act ahora es el valor anterior al nodo que apunta el puntero node
            act.next = node #se guarda el valor de mi puntero node
            act = node #se corre el puntero act al lugar del puntero node

        newList._head.prev = act
        act.next = newList._head
        return newList      
    
    def clear(self):
        self._head.prev = self._head.next = self._head #el primer valor de mi lista y el último, se vuelven None = limpio la lista
    
    def begin(self):
        return DoubleLinkedList._Coordinate(self._head.next) #begin = el valor siguiente a mi nodo cabecera
        #crea una coordenada que referencia al siguiente del nodo cabecera
    
    def end(self):
        return DoubleLinkedList._Coordinate(self._head) #end = apunta a mi nodo cabecera (siguiente a mi último valor)
        #crea una coordenada que apunta al nodo cabecera

    def __eq__(self, otherList):
        p = self.begin() #primer valor de mi lista
        q = otherList.begin() #primer valor de una segunda lista

        while p!= self.end() and q != otherList.end(): #mientras el valor de p no sea el siguiente del ultimo, y el valor de q no sea el siguiente del ultimo
            if p.value != q.value: #si el valor de p y q son distintos
                return False #las listas son distintas
            
            p.advance() #avanzo un valor en la primera lista
            q.advance() #avanzo un valor en la segunda lista
        
        return p == self.end() and q == otherList.end() #termino de recorrer cuando p y q referencien al siguiente del ultimo valor de la lista (o sea, al head)
    
    def __repr__(self):
        return 'DoublyLinkedList([' + ', '.join(repr(v) for v in self) + '])'
    
    def insert (self, coordenada, value):
        current = coordenada._node #referencia a un nodo especifico
        newNode = DoubleLinkedList._Node(value) #se crea el nodo que se va a insertar 
        newNode.prev = current.prev #el anterior del nodo creado, es el anterior del nodo al que referencia actual
        newNode.next = current #el siguiente del nodo creado, es el nodo al que apunta mi puntero actual
        newNode.prev.next = newNode #el siguiente del nodo anterior de mi nuevo nodo, es el nuevo nodo
        newNode.next.prev = newNode #el anterior del nodo siguiente al nodo nuevo, es el nuevo nodo
    
        #return DoubleLinkedList._Coordinate(current) #retorno la coordenada que apunta a mi nodo actual
    
    def erase (self, coordenada): 
        current = coordenada._node #referencia a un nodo especifico
        current.prev.next = current.next #el next del nodo anterior a current, ahora apunta al nodo siguiente de current 
        current.next.prev = current.prev #el prev del nodo siguiente a current, ahora apunta al nodo anterior de current
        return coordenada.next() #retorno la coordenada siguiente
    
    def __iter__(self):
        return DoubleLinkedList._Iterator(self._head.next, self._head)