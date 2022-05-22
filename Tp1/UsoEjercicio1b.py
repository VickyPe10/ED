from Ejercicio1 import algoritmoBinario

lista = [1,2,3,4,5,6,7,8,9,10]
n = len(lista)
numero = 8
encontrado = algoritmoBinario(lista, numero, n)

if encontrado == None:
    print ("El numero no se encuentra en la lista.")
else:
    print("El numero se encuentra en la posicion ",encontrado," de la lista.")