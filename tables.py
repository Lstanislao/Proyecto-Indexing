from funciones import pedirPelicula

peliculas = [
]

titulos = [
]

codigos = [
]


def agregarPelicula():
    global peliculas
    peli = pedirPelicula()
    peliculas.append(peli)
    index = peliculas.index(peli)
    titulo = peli[2].lower()
    codigo = peli[1]
    agregarTitulo(titulo, index)
    insertarCodigo(codigo, index)


def agregarTitulo(titulo, index):
    global titulos
    print(titulos)
    palabras = titulo.split(" ")
    for palabra in palabras:
        if palabra != "":
            posicion = buscar(palabra, titulos)
            if posicion == False:
                insertarTitulo(palabra, index)
            else:
                indices = titulos[posicion][1]
                newIndices = []
                print(indices)
                for indice in indices:
                    newIndices.append(indice)
                newIndices.append(index)
                print(newIndices)
                titulos[posicion][1] = newIndices
    print('titulos: ', titulos)


def ordenarTitulos():
    global titulos
    titulos = sorted(titulos, key=lambda fila: fila[0])


def buscar(buscado, arreglo):
    izquierda = 0
    derecha = len(arreglo) - 1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        elementoDelMedio = arreglo[mitad][0]
        if elementoDelMedio == buscado:
            return mitad
        if buscado < elementoDelMedio:
            derecha = mitad - 1
        else:
            izquierda = mitad + 1
    return False


def insertarTitulo(newPalabra, index):
    global titulos
    # AQUI CREO QUE NO SE PUEDE HACER UN SOLO PROCEDDIMIENTO PARA INSERTAR TANTAO CODIGO COMO TITULO PORQUE NECESITAS MODIFICAR LA VARIABLE GLOBAL
    izquierda = 0
    derecha = len(titulos) - 1
    # medio = (izquierda + derecha) // 2
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        elementoDelMedio = titulos[mitad][0]
        if elementoDelMedio == newPalabra:
            return mitad
        if newPalabra < elementoDelMedio:
            derecha = mitad - 1
        else:
            izquierda = mitad + 1
    # print('soy izquierda ', izquierda)
    # print('soy derecha ', derecha)
    # INSERTAR Y ACOMODAR LOS INDICES
    if izquierda >= len(titulos) or len(titulos) == 0:
        titulos.append([newPalabra, [index]])
    else:
        temporal = titulos[izquierda]
        titulos[izquierda] = [newPalabra, [index]]
        # print(temporal)
        maxi = len(titulos)
        # print(maxi)
        # print(izquierda+1)
        print(izquierda, " TITULO ", derecha)
        for i in range((izquierda+1), maxi):
            aux = titulos[i]
            titulos[i] = temporal
            temporal = aux
        titulos.append(temporal)


def insertarCodigo(newCodigo, index):
    global codigos
    izquierda = 0
    derecha = len(codigos) - 1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        elementoDelMedio = codigos[mitad][0]
        if elementoDelMedio == newCodigo:
            return mitad
        if newCodigo < elementoDelMedio:
            derecha = mitad - 1
        else:
            izquierda = mitad + 1
    if izquierda >= len(codigos) or len(codigos) == 0:
        codigos.append([newCodigo, index])
    else:
        temporal = codigos[izquierda]
        codigos[izquierda] = [newCodigo, index]
        print(izquierda, " CODIGO ", derecha)
        maxi = len(codigos)
        for i in range((izquierda), maxi):
            aux = codigos[i]
            codigos[i] = temporal
            temporal = aux
        codigos.append(temporal)
    print('codigos: ', codigos)


