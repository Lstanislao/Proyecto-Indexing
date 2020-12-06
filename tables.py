from funciones import pedirPelicula

peliculas = [
    ['*', 12345, "la triste historia de los que estudian sistema ", 10, 12345],
    ['', 65478, "rapidos y furiosos", 10, -1],
    ['', 36589, "rapidos y furiosos 5", 10, -1],
]

titulos = [
    ["hola", [6, 77]],
    ["chao", [0]],
    ["hasta pronto", [99]],
    ["hasta luego", [1]],
    ["zzzzz", [6]]
]

codigos = [

]


def agregarPelicula():
    global peliculas
    peli = pedirPelicula()
    peliculas.append(peli)
    index = peliculas.index(peli)
    titulo = peli[2].lower
    agregarTitulo(titulo, index)


def agregarTitulo(titulo, index):
    ordenarTitulos()  # Quitar
    global titulos
    print(titulos)
    palabras = titulo.split(" ")
    for palabra in palabras:
        if palabra != "":
            posicion = buscarTitulo(palabra)
            if posicion == False:
                titulos.append([palabra, [index]])
            else:
                indices = titulos[posicion][1]
                newIndices = []
                for indice in indices:
                    newIndices.append(indice)
                newIndices.append(index)
                titulos[posicion][1] = newIndices
    print(titulos)


def ordenarTitulos():
    global titulos
    titulos = sorted(titulos, key=lambda fila: fila[0])


def ordenarPeliculas():
    global peliculas
    peliculas = sorted(peliculas, key=lambda fila: fila[1])


def buscarTitulo(buscado):
    global titulos
    izquierda = 0
    derecha = len(titulos) - 1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        elementoDelMedio = titulos[mitad][0]
        if elementoDelMedio == buscado:
            return mitad
        if buscado < elementoDelMedio:
            derecha = mitad - 1
        else:
            izquierda = mitad + 1
    return False


def buscarCodigo(arreglo, buscado):
    izquierda = 0
    derecha = len(arreglo) - 1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        elementoDelMedio = arreglo[mitad][1]
        if elementoDelMedio == buscado:
            return mitad
        if buscado < elementoDelMedio:
            derecha = mitad - 1
        else:
            izquierda = mitad + 1
    return False
