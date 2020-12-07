from funciones import pedirPelicula, pedirDatosRenta

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
            print('posicion ', posicion)
            print(0 == False)
            if posicion == -1: #ARREGLAR: si el indice es 0, lo toma como falso
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

# @ recibe codigo o palabra y devuelve el index dode esta en su respectiva tabla y con este se puede sacr el indice dond eesta en peliculas


def buscar(buscado, arreglo, consulta=False):
    global peliculas
    izquierda = 0
    derecha = len(arreglo) - 1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        elementoDelMedio = arreglo[mitad][0]
        indice = arreglo[mitad][1]
        # print(indice)
        # print(peliculas[indice][0])
        if elementoDelMedio == buscado:
            if not consulta:
                return mitad
            elif peliculas[indice][0] != "*":
                return mitad
        if buscado < elementoDelMedio:
            derecha = mitad - 1
        else:
            izquierda = mitad + 1
    return -1


def insertarTitulo(newPalabra, index):
    global titulos
    # AQUI CREO QUE NO SE PUEDE HACER UN SOLO PROCEDDIMIENTO PARA INSERTAR TANTAO CODIGO COMO TITULO PORQUE NECESITAS MODIFICAR LA VARIABLE GLOBAL
    izquierda = 0
    derecha = len(titulos) - 1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        elementoDelMedio = titulos[mitad][0]

        if newPalabra < elementoDelMedio:
            derecha = mitad - 1
        else:
            izquierda = mitad + 1
    # INSERTAR Y ACOMODAR LOS INDICES
    if izquierda >= len(titulos) or len(titulos) == 0:
        titulos.append([newPalabra, [index]])
    else:
        temporal = titulos[izquierda]
        titulos[izquierda] = [newPalabra, [index]]
        maxi = len(titulos)
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
        if newCodigo < elementoDelMedio:
            derecha = mitad - 1
        else:
            izquierda = mitad + 1
    if izquierda >= len(codigos) or len(codigos) == 0:
        codigos.append([newCodigo, index])
    else:
        temporal = codigos[izquierda]
        codigos[izquierda] = [newCodigo, index]
        maxi = len(codigos)
        for i in range((izquierda+1), maxi):
            aux = codigos[i]
            codigos[i] = temporal
            temporal = aux
        codigos.append(temporal)
    print('codigos: ', codigos)


def eliminarPelicula(codigo):
    global codigos
    global peliculas
    fila = buscar(codigo, codigos)
    if fila != -1:
        peliculas[fila[1]][0] = "*"
    else:
        print('No se encontro la peli')
    


def packing():
    for pelicula in peliculas:
        if pelicula[0] == "*":
            eliminarTitulo = pelicula[2]
            eliminarCodigo = pelicula[1]


# def eliminarTitulo(titulo):
#    palabras = titulo.split(" ")
#    for palabras in titulo:
#      buscar(palabra,titulos)

def rentarPelicula():
    global peliculas
    global codigos

    info = pedirDatosRenta()
    indice = buscar(info[1], codigos, True)
    
    if indice != -1: #si el indice es 0 no sirve
        indicePelicula = codigos[indice][1]
        if peliculas[indicePelicula][4] == -1:
            peliculas[indicePelicula][4] = info[0]
            print(peliculas)
            print('ha rentado ', peliculas[indicePelicula][2])
    else:
        print('peli no esta registrada')
