from funciones import pedirPelicula, pedirDatosRenta

peliculas = [
    ['*', 11111, 'El rey leon', 12456, -1], ['', 10000, 'rapidos y furiosos 2', 12456, -1], ['*', 55555, 'la bella y la bestia',
                                                                                             12564, -1], ['', 85203, 'la princesa y el sapo', 12651, -1], ['*', 12378, 'furisos sapo y la bestia', 12564, -1]

]

titulos = [

    ['2', [1]], ['bella', [2]], ['bestia', [2, 4]], ['el', [0, 3]], ['furiosos', [1]], ['furisos', [4]], ['la', [2, 2, 3, 4]], ['leon',
                                                                                                                                [0]], ['princesa', [3]], ['rapidos', [1]], ['rey', [0]], ['sapo', [3, 4]], ['y', [1, 2, 3, 4]]
]

codigos = [
    [10000, 1], [11111, 0], [12378, 4], [55555, 2], [85203, 3]
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
            if posicion == -1:  # ARREGLAR: si el indice es 0, lo toma como falso
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
    index = codigos[buscar(codigo, codigos)][1]
    print(index)
    peliculas[index][0] = "*"


def packing():
    global peliculas
    i = 0
    while i < len(peliculas):
        pelicula = peliculas[i]
        print("PELICULA ", pelicula)
        if pelicula[0] == "*":
            if i == (len(peliculas)-1):
                print("HOLA")
                i = i+1
            index = peliculas.index(pelicula)
            eliminarTitulo((pelicula[2].lower()), index)
            eliminarCodigo(pelicula[1])
            peliculas.remove(pelicula)
            compactar(index)
        else:
            i = i+1
    '''for pelicula in peliculas:
        print("PELICULA ", pelicula)
        if pelicula[0] == "*":
            index = peliculas.index(pelicula)
            eliminarTitulo((pelicula[2].lower()), index)
            eliminarCodigo(pelicula[1])
            peliculas.remove(pelicula)
            compactar(index)'''


def eliminarTitulo(titulo, index):
    global titulos
    palabras = titulo.split(" ")
    for palabra in palabras:
        aux = buscar(palabra, titulos)
        if len(titulos[aux][1]) > 1:
            newIndex = []
            for i in titulos[aux][1]:
                if i != index:
                    newIndex.append(i)
            titulos[aux][1] = newIndex
        else:
            titulos.pop(aux)


def eliminarCodigo(codigo):
    global codigos
    index = buscar(codigo, codigos)
    codigos.pop(index)


def compactar(index):
    global titulos
    global codigos
    for codigo in codigos:
        if codigo[1] > index:
            codigo[1] = codigo[1]-1
    for i in range(len(titulos)):
        for j in range(len(titulos[i][1])):
            if titulos[i][1][j] > index:
                titulos[i][1][j] = (titulos[i][1][j])-1


def rentarPelicula():
    global peliculas
    global codigos

    info = pedirDatosRenta()
    indice = buscar(info[1], codigos, True)

    if indice != -1:  # si el indice es 0 no sirve
        indicePelicula = codigos[indice][1]
        if peliculas[indicePelicula][4] == -1:
            peliculas[indicePelicula][4] = info[0]
            print(peliculas)
            print('ha rentado ', peliculas[indicePelicula][2])
    else:
        print('peli no esta registrada')
