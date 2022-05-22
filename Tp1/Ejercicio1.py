def algoritmoLineal (lista, numero):
    for x in lista:
        if (x == numero):
            return True
        else:
            continue

def algoritmoBinario (lista, numero, n):
    minimo = 0
    maximo = n - 1
    medio = 0
    while minimo <= maximo:
        medio = (maximo + minimo)//2
        if lista[medio] < numero:
            minimo = medio + 1

        elif lista[medio] > numero:
            maximo = medio - 1
        
        else:
            return medio
    
    return None
