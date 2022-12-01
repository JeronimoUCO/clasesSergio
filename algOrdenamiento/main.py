activo = True

#Este es un comentario
def calcular_suma(a,b):
    return a + b
def bubbleSort(lista):
    n = len(lista)

    print(f"""
    --------------------------------------------------------------------------
    Ejemplo de ordenamiento de Burbuja:

    Lista a ordenar = {lista}
    
    Instrucciones:
    --------------------------------------------------------------------------
    """)
    for i in range(n-1):

        for j in range(0, n-i-1):

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
        print(f"""
    --------------------------------------------------------------------------
    Se recorre la lista durante varias iteraciones y cuando se encuentra que un elemento es menor a su inmediatamente posterior, se intercambian sus posiciones
    Complejidad temporal: O(n^2)
    Lista iteracion = {lista}
    
    Instrucciones:
    --------------------------------------------------------------------------
    """)
    return lista

def selectionSort(lista):
    # método de ordenación Selección
    nb = len(lista)  # define una variable que contenga la logitud de la lista
    print(f"""
    --------------------------------------------------------------------------
    Ejemplo de ordenamiento de seleccion:

    Lista a ordenar = {lista}

    Instrucciones:
    --------------------------------------------------------------------------
    """)
    # iteración por toda la longitud de la lista desde el primero al ultimo
    for actual in range(0, nb):
        # se asigna inicialmente la variable "mas_pequeno" al indice de la iteraición
        mas_pequeno = actual
        for j in range(actual+1, nb):  # comparar con el elmento actual con los siguientes
            if lista[j] < lista[mas_pequeno]:
                mas_pequeno = j    # si es mas pequeño se asigna ese valos a "mas_pequeno"
        # revisa si el indice actual corresponde al elemento menor respecto a los elementos de la derecha, si esto no pasa:
        if min is not actual:
            # creamos una variable temp que contiene al elemento del indice actual de interaición
            temp = lista[actual]
            lista[actual] = lista[mas_pequeno]  # los intercambia de posición
            lista[mas_pequeno] = temp
        print(f"""
        --------------------------------------------------------------------------
        Se itera por toda la longitud de la lista desde el primero hasta el ultimo, a cada elemento se le compara con los siguientes,
        si un elemento dado es mayor a algun elemento posterior a este, se intercambian sus posiciones
        Complejidad temporal: O(n^2)
        
        Lista iteracion = {lista}
        --------------------------------------------------------------------------
        """)
    return(lista)

def insertionSort(lista):
    print(f"""
        --------------------------------------------------------------------------
        Ejemplo de ordenamiento por insercion:
        
        Lista a ordenar = {lista}
        
        Instrucciones:
        --------------------------------------------------------------------------
        """)
    for i in range(len(lista)):
        for j in range(i, 0, -1):
            # Itera sobre todos los elementos de la lista y revisa si los elementos anteriores son mayores a los posteriores, si esto pasa, los intercambia de posiciones hasta tener una lista ordenada
            if (lista[j - 1] > lista[j]):
                aux = lista[j]
                lista[j] = lista[j - 1]
                lista[j - 1] = aux
                print(f"""
                --------------------------------------------------------------------------
                Se itera por toda la lista, si un elemento anterior es mayor a su inmediatamente posterior, se intercambian
                Complejidad temporal: O(n^2)

                Lista iteracion = {lista}
               --------------------------------------------------------------------------
               """)
    return(lista)

def quickSort(lista):
    # Se define una variable que contiene una lista "izquierda"
    izquierda = []
    # Se define una variable que contiene una lista "centro"
    centro = []
    # Se define una variable que contiene una lista "derecha"
    derecha = []
    print(f"""
        Ejemplo quick sort:
    --------------------------------------------------------------------------
        Lista a ordenar = {lista}

        Instrucciones:
        Se define una variable que contiene una lista "izquierda", una que contiene una lista "centro" y otra que contiene una lista "derecha"
        Izquierda = {izquierda}
        Centro = {centro}
        Derecho = {derecha}
    --------------------------------------------------------------------------
    """)
    if len(lista) > 1:  # Si la lista no es ni vacia ni de un elemento, se escoge un pivote
        pivote = lista[0]
        print(f"""
        --------------------------------------------------------------------------
        Si la lista no es ni vacia ni de un elemento, se escoge un pivote
        pivote = {pivote}
        --------------------------------------------------------------------------
        """)
        for i in lista:  # Si itera sobre cada elemento de la lista, si el elemento es menor al pivote, se añade a la lista izquierda, si es mayor, a la de la derecha, y si es igual, a la del centro
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)

            print(f"""
            --------------------------------------------------------------------------
            Se itera sobre cada elemento de la lista, si el elemento es menor al pivote, se añade a la lista izquierda, si es mayor, a la de la derecha, y si es igual, a la del centro
            Complejidad temporal: 
              Peor caso -> O(n^2)
              Mejor caso -> O(nLog n)
            
            izquierda = {izquierda}
            derecha = {derecha}
            centro = {centro}
            pivote = {pivote}

            Se ejecuta el mismo algoritmo tanto a la izquierda como a la derecha hasta que cada una de estas listas tengas 1 elemento
            --------------------------------------------------------------------------
            """)
        # print(izquierda+["-"]+centro+["-"]+derecha)
        # Se hace el proceso de fraccion y comparacion con pivotes en la lista hasta que en izquierda y derecha solo quede un elemento, centro permanece sin cambio
        return quickSort(izquierda)+centro+quickSort(derecha)
    else:
        print(f"""
      --------------------------------------------------------------------------
    Si la lista tiene solo un elemento, se retorna, porque ya está ordenada
    lista={lista}
      --------------------------------------------------------------------------
    """)
        return lista  # Si la lista tiene solo un elemento, se retorna, porque ya está ordenada

def mergeSort(lista):
    print(f"""
    Ejemplo merge sort:
    --------------------------------------------------------------------------
        Lista a ordenar = {lista}

        Instrucciones:
    --------------------------------------------------------------------------
    """)

    if len(lista) == 1:
        return lista
    elif len(lista) > 1:
        mitad = len(lista) // 2
        primeraMitad = lista[:mitad]
        segundaMitad = lista[mitad:]

        mergeSort(primeraMitad)
        mergeSort(segundaMitad)

        i = 0
        j = 0
        k = 0

        while i < len(primeraMitad) and j < len(segundaMitad):
            if primeraMitad[i] < segundaMitad[j]:
                lista[k] = primeraMitad[i]
                i += 1
            else:
                lista[k] = segundaMitad[j]
                j += 1
            k += 1
        while i < len(primeraMitad):
            lista[k] = primeraMitad[i]
            i += 1
            k += 1
        while j < len(segundaMitad):
            lista[k] = segundaMitad[j]
            j += 1
            k += 1
    print(f"""
     Se divide la lista en 2 hasta que queden varias listas de 1 elemento, despues de esto se compara cada lista con la 
     inmediatamente siguiente de forma que se cree una nueva lista en la que queden debidamente ordenados los elementos, se van uniendo así las listas
     hasta formar una ultima lista completamente ordenada
     Complejidad temporal: O(nLogn)

     primera mitad:{primeraMitad}
     segunda mitad:{segundaMitad}
    --------------------------------------------------------------------------
    """)
    return lista

def heapify(lista, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if l < n and lista[i] < lista[l]:
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < n and lista[largest] < lista[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        lista[i], lista[largest] = lista[largest], lista[i]  # swap

        # Heapify the root.
        heapify(lista, n, largest)

def heapSort(lista):
    print(f"""
        --------------------------------------------------------------------------
        Ejemplo de ordenamiento de heap:
        
        Lista a ordenar = {lista}
        
        Instrucciones:
        --------------------------------------------------------------------------
        """)
    n = len(lista)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]   # swap
        heapify(lista, i, 0)
        print(f"""
        --------------------------------------------------------------------------
        Se encuentra el elemento más pequeño de la lista y se le lleva al inicio, este proceso se hace para los siguientes elementos
        Complejidad temporal: O(nLogn)

        Lista iteracion = {lista}
        --------------------------------------------------------------------------
        """)
    return lista

def counting_Sort(arr, p):
    s = len(arr)
    result = [0] * s
    c = [0] * 10
    
    # count of elements
    for i in range(0, s):
        index = round(arr[i] // p)
        c[index % 10] += 1
        
    # cumulative count
    for i in range(1, 10):
        c[i] += c[i - 1]

    # sorted order
    i = s - 1
    while i >= 0:
        index = round(arr[i] // p  )
        result[c[index % 10] - 1] = arr[i]
        c[index % 10] -= 1
        i -= 1
        
    for i in range(0, s):
        arr[i] = result[i]

def radixSort(lista):
    print(f"""
        --------------------------------------------------------------------------
        Ejemplo de ordenamiento de radix:
        
        Lista a ordenar = {lista}
        
        Instrucciones:
        --------------------------------------------------------------------------
        """)
    maximum = max(lista)

    p = 1
    while maximum // p > 0:
        counting_Sort(lista, p)
        p *= 10
        print(f"""
        --------------------------------------------------------------------------
        Se comparan los digitos de todos los elementos de la lista y se ordenan iterativamente, se inicia con unidades, luego decenas, etc... Y así hasta terminar con una lista ordenada
        Complejidad temporal: O(n+k) -> Es altamente eficiente a nivel de tiempo, pero no de espacio

        Lista iteracion = {lista}
        --------------------------------------------------------------------------
        """)
    return lista

while activo:
    eleccion = input("""
    ------------------------------------------------------------------------------------------------------
    Bienvenido al programa tutorial de algoritmos de ordenamiento, escribe a continuacion el numero correspondiente a la opcion que deseas explorar:

    1. Bubble sort
    2. Selection sort
    3. Insertion sort
    4. Quick sort
    5. Merge Sort
    6. Heap sort
    7. Radix Sort
    8. Salir
    ------------------------------------------------------------------------------------------------------
    """)

    if eleccion == "1":
        lista = [5, 7, 3, 1, 8, 4, 9, 2, 6, -3, 0.5]
        print(f"Lista ordenada: {bubbleSort(lista)}")

    if eleccion == "2":
        lista = [5, 7, 3, 1, 8, 4, 9, 2, 6, -3, 0.5]
        print(f"Lista ordenada: {selectionSort(lista)}")

    if eleccion == "3":
        lista = [5, 7, 3, 1, 8, 4, 9, 2, 6, -3, 0.5]
        print(f"Lista ordenada: {insertionSort(lista)}")

    if eleccion == "4":
        lista = [5, 7, 3, 1, 8, 4, 9, 2, 6, -3, 0.5]
        print(f"Lista ordenada: {quickSort(lista)}")

    if eleccion == "5":
        lista = [5, 7, 3, 1, 8, 4, 9, 2, 6, -3, 0.5]
        print(f"Lista ordenada: {mergeSort(lista)}")

    if eleccion == "6":
        lista = [5, 7, 3, 1, 8, 4, 9, 2, 6, -3, 0.5]
        print(f"Lista ordenada: {heapSort(lista)}")

    if eleccion == "7":
        lista = [5, 73, 32, 14, 832, 412, 954, 243, 623, 0.5]
        print(f"Lista ordenada: {radixSort(lista)}")

    if eleccion == "8":
        activo = False
