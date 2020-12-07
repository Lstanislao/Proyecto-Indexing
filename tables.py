from funciones import *

peliculas = [
    ['*', 11111, 'El rey leon', 12456, -1], ['', 10000, 'rapidos y furiosos 2', 12456, -1], ['*', 55555, 'la bella y la bestia',
                                                                                             12564, -1], ['', 85203, 'la princesa y el sapo', 12651, -1], ['', 12378, 'furisos sapo y la bestia', 12564, -1]

]

titulos = [

    ['2', [1]], ['bella', [2]], ['bestia', [2, 4]], ['el', [0, 3]], ['furiosos', [1]], ['furisos', [4]], ['la', [2, 2, 3, 4]], ['leon',
                                                                                                                                [0]], ['princesa', [3]], ['rapidos', [1]], ['rey', [0]], ['sapo', [3, 4]], ['y', [1, 2, 3, 4]]
]

codigos = [
    [10000, 1], [11111, 0], [12378, 4], [55555, 2], [85203, 3]
]


def pedirPelicula():
    valido = False
    while not valido:
        codigo = pedirEntero("\nIngrese el codigo de la pelicula: ", 5)
        print(buscar(codigo, codigos))
        if buscar(codigo, codigos) == -1:
            valido = True
        else:
            print("\nYa existe una pelicula con ese codigo.")
    valido = False
    while not valido:
        titulo = pedirString('\nIngrese el nombre de la pelicula: ', 30)
        titulo = titulo.lower()
        palabras = titulo.split(" ")
        for palabra in palabras:
            if buscar(palabra, titulos) == -1:
                valido = True
        if not valido:
            print('\nYa existe una pelicula con este mismo titulo.')
    alquiler = pedirEntero(
        '\nIngrese el costo diario del alquiler de la pelicula: ', 8)
    return ["", codigo, titulo, alquiler, -1]


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
    palabras = list(set(palabras))
    for palabra in palabras:
        if palabra != "":
            posicion = buscar(palabra, titulos)
            if posicion == -1:
                insertarTitulo(palabra, index)
            else:
                indices = titulos[posicion][1]
                newIndices = []
                for indice in indices:
                    newIndices.append(indice)
                newIndices.append(index)
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
    izquierda = 0
    derecha = len(titulos) - 1
    while izquierda <= derecha:
        mitad = (izquierda + derecha) // 2
        elementoDelMedio = titulos[mitad][0]
        if newPalabra < elementoDelMedio:
            derecha = mitad - 1
        else:
            izquierda = mitad + 1
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


def eliminarPelicula():
    global codigos
    global peliculas
    codigo = pedirCodigo(
        "\nIngrese el codigo de la pelicula que desea eliminar: ")
    fila = buscar(codigo, codigos, True)
    if fila != -1:
        indicePelicula = codigos[fila][1]
        peliculas[indicePelicula][0] = "*"
        nombre = peliculas[indicePelicula][2].capitalize()
        print("\nLa pelicula '{}' se ha borrado.".format(nombre))
        return True
    else:
        print("\nNo hay una pelicula registrada con el codigo ingresado.")
        return False


def packing():
    global peliculas
    print(peliculas)
    print(codigos)
    print(titulos)
    i = 0
    while i < len(peliculas):
        pelicula = peliculas[i]
        print("PELICULA ", pelicula)
        if pelicula[0] == "*":
            if i == (len(peliculas)-1):
                i = i+1
            index = peliculas.index(pelicula)
            eliminarTitulo((pelicula[2].lower()), index)
            eliminarCodigo(pelicula[1])
            peliculas.remove(pelicula)
            compactar(index)
        else:
            i = i+1
    print(peliculas)
    print(codigos)
    print(titulos)


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
    '''
    Funcion que pide el numero de socio y el codigo de la pelicula a rentar. En caso de que la pelicula
    exista y no este alquilada, se alquila al socio. En caso contrario, se muestra un mensaje indicando
    que esta alquilada o que no existe.
    '''
    global peliculas
    global codigos

    info = pedirDatosRenta()
    indice = buscar(info[1], codigos, True)

    if indice != -1:
        indicePelicula = codigos[indice][1]
        nombre = peliculas[indicePelicula][2].capitalize()
        if peliculas[indicePelicula][4] == -1:
            peliculas[indicePelicula][4] = info[0]
            print(peliculas)
            print("\nHa rentado '{}'.".format(nombre))
            return True
        else:
            print("\nLa pelicula '{}' ya se encuentra alquilada.".format(nombre))
            return False
    else:
        print('\nNo hay una pelicula registrada con el codigo ingresado.')
        return False


def devolverPelicula():
    '''
    Funcion que pide el codigo de la pelicula a devolver. En caso de que la pelicula
    exista y este alquilada, se acepta la devolucion. En caso contrario, se muestra un mensaje indicando
    que no esta alquilada o que no existe.
    '''
    global peliculas
    global codigos

    codigo = pedirCodigo(
        "\nIngrese el codigo de la pelicula que desea devolver: ")
    indice = buscar(codigo, codigos, True)

    if indice != -1:
        indicePelicula = codigos[indice][1]
        nombre = peliculas[indicePelicula][2].capitalize()
        if peliculas[indicePelicula][4] != -1:
            peliculas[indicePelicula][4] = -1
            print(peliculas)
            print("\nHa devuelto '{}'.".format(nombre))
            return True
        else:
            print(
                "\nLa pelicula '{}' no esta alquilada y no puede ser devuelta.".format(nombre))
            return False
    else:
        print("\nNo hay una pelicula registrada con el codigo ingresado.")
        return False


def consultaPorCodigo():
    '''
    Funcion que pide el codigo de la pelicula y ve si existe. Si existe, muestra si esta alquilada o no. 
    Si no, muestra que no hay una pelicula con ese codigo.
    '''
    global peliculas
    global codigos

    codigo = pedirCodigo("\nIngrese el codigo de la pelicula que desea consultar: ")
    indice = buscar(codigo, codigos, True)
    
    print("\nRESULTADOS DE BUSQUEDA:\n")
    if indice != -1:
        indicePelicula = codigos[indice][1]
        nombre = peliculas[indicePelicula][2].capitalize()
        if peliculas[indicePelicula][4] != -1:
            print(peliculas)
            print("\nLa pelicula '{}' se encuentra alquilada.".format(nombre)) 
            return True     
        else:
            print("\nLa pelicula '{}' no esta alquilada.".format(nombre))     
            return False 
    else:
        print("\nNo hay una pelicula registrada con el codigo ingresado.")
        return False
        

def consultaPorPalabras():
    '''
    Funcion que pide una o dos palabras del titulo de la pelicula y ve si hay peliculas cuyo
    titulo las contenga. Si hay, muestra si estan alquiladas o no. Si no, muestra que no hay
    una pelicula con ese codigo.
    '''
    global peliculas
    global titulos

    palabras = pedirPalabras()
    peliculaPedida = []

    print("\nRESULTADOS DE BUSQUEDA:\n")
    for i in range(len(palabras)):
        peliculasTemp = []
        indice = buscar(palabras[i], titulos)
        if indice != -1:
            if i == 0:
                for index in titulos[indice][1]:
                    if peliculas[index][0] != "*":
                        peliculaPedida.append(index)
            else:
                for index in titulos[indice][1]:
                    if peliculaPedida.count(index):
                        peliculasTemp.append(index)
                peliculaPedida = peliculasTemp
        else:
            print("\nNo hay una pelicula registrada cuyo titulo contenga esa(s) palabra(s).")
            return False

    if len(peliculaPedida):
        for indicePelicula in peliculaPedida:
            nombre = peliculas[indicePelicula][2].capitalize()
            codigo = peliculas[indicePelicula][1]
            if peliculas[indicePelicula][4] != -1:
                print(peliculas)
                print("\n   La pelicula de titulo '{}' y codigo {} se encuentra alquilada.".format(nombre, codigo))      
            else:
                print("\n   La pelicula de titulo '{}' y codigo {} no esta alquilada.".format(nombre, codigo)) 
        return True
    else:
        print("\nNo hay una pelicula registrada cuyo titulo contenga esa(s) palabra(s).")
        return False
    



