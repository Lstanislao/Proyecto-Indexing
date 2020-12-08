from funciones import*
from prettytable import PrettyTable
import csv

firstRowMovies = ['Logical','CodeNumber','MovieName','DailyPrice','Member']
firstRowCodes = ['Code','Index']
firstRowWords = ['Words','Index']
peliculas = [
]

titulos = [                                                                                                    
]

codigos = [
    ]

def leerPalabras():
    global titulos
    titulos = []
    with open ('wordsIndex.csv', 'r') as words_file:
        csv_reader = csv.reader(words_file)
        next(csv_reader)
        contador = 0
        for w in csv_reader:
            titulos.append(w)
            titulos[contador][1] = titulos[contador][1].strip('][').split(',')
            for i in range (len(titulos[contador][1])):
                titulos[contador][1][i] = int(titulos[contador][1][i])
            contador += 1

def leerCodigos():
    global codigos
    codigos = []
    with open ('codesIndex.csv', 'r') as codes_file:
        csv_reader = csv.reader(codes_file)
        next(csv_reader)
        contador = 0
        for c in csv_reader:
            codigos.append(c)
            for i in range(2):
                codigos[contador][i] = int(codigos[contador][i])
            contador+=1

def leerPeliculas():
    global peliculas
    peliculas = []
    with open ('movies.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for movie in csv_reader:
            peliculas.append(movie)

def pedirPelicula():
    global titulos
    global codigos
    leerCodigos()
    leerPalabras()

    valido = False
    while not valido:
        mostrarPeliculas()
        codigo = pedirEntero("\nType the code you want for the MOVIE: ", 5)
        if buscar(codigo, codigos) == -1:
            valido = True
        else:
            print("\nA movie of the list already has that code, type another.")
    valido = False
    titulo = ''
    while not valido:
        titulo = pedirString('\nType the name of the movie: ', 30)
        titulo = titulo.lower()
        palabras = titulo.split(" ")

        peliculaPedida = []
        for i in range(len(palabras)):
            peliculasTemp = []
            indice = buscar(palabras[i], titulos)
            if indice == -1:
                peliculaPedida = []
                break
            else:
                if i == 0:
                    for index in titulos[indice][1]:
                        peliculaPedida.append(index)
                else:
                    for index in titulos[indice][1]:
                        if peliculaPedida.count(index) > 0:
                            peliculasTemp.append(index)
                    peliculaPedida = peliculasTemp

        valido = len(peliculaPedida) == 0
        if not valido:
            print('\nA movie of the list already has that title.')
    alquiler = pedirEntero(
        '\nType de DAILY COST of the movie rental: ', 8)
    return ["", codigo, titulo, alquiler, -1]


def agregarPelicula():
    global peliculas
    leerPeliculas()

    peli = pedirPelicula()
    peliculas.append(peli)

    with open ('movies.csv', 'w',newline='') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)
        csv_writer.writerow(firstRowMovies)
        for p in peliculas:
            csv_writer.writerow(p)
    index = peliculas.index(peli)
    titulo = peli[2].lower()
    codigo = peli[1]
    agregarTitulo(titulo, index)
    insertarCodigo(codigo, index)


def agregarTitulo(titulo, index):
    global titulos
    leerPalabras()

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
    with open ('wordsIndex.csv', 'w',newline='') as new_words_file:
        csv_writer = csv.writer(new_words_file)
        csv_writer.writerow(firstRowWords)
        for t in titulos:
            csv_writer.writerow(t)


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
    leerCodigos()

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
    with open ('codesIndex.csv', 'w',newline='') as new_codes_file:
        csv_writer = csv.writer(new_codes_file)
        csv_writer.writerow(firstRowCodes)
        for c in codigos:
            csv_writer.writerow(c)


def eliminarPelicula():
    global codigos
    global peliculas
    mostrarPeliculas()
    leerPeliculas()
    leerCodigos()
    codigo = pedirCodigo(
        "\nIngrese el codigo de la pelicula que desea eliminar: ")
    fila = buscar(codigo, codigos, True)
    
    if fila != -1:
        indicePelicula = codigos[fila][1]
        if peliculas[indicePelicula][4] == '-1':
            peliculas[indicePelicula][0] = "*"
            nombre = peliculas[indicePelicula][2].capitalize()
            with open ('movies.csv', 'w',newline='') as new_csv_file:
                csv_writer = csv.writer(new_csv_file)
                csv_writer.writerow(firstRowMovies)
                for p in peliculas:
                    csv_writer.writerow(p)
            print("\nThe movie '{}' has been deleted.".format(nombre))
            return True
        else:
            print("YOU CANT DELETE A MOVIE THAT IS RENTED")
            return False
    else:
        print("\nNO MOVIE WITH THAT CODE IN THE SYSTEM")
        return False


def packing():
    global peliculas
    leerPeliculas()
    i = 0
    while i < len(peliculas):
        pelicula = peliculas[i]
        if pelicula[0] == "*":
            if i == (len(peliculas)-1):
                i = i+1
            index = peliculas.index(pelicula)
            eliminarTitulo((pelicula[2].lower()), index)
            eliminarCodigo(pelicula[1])
            peliculas.remove(pelicula)
            with open ('movies.csv', 'w',newline='') as new_csv_file:
                csv_writer = csv.writer(new_csv_file)
                csv_writer.writerow(firstRowMovies)
                for p in peliculas:
                    csv_writer.writerow(p)
            compactar(index)
        else:
            i = i+1
    mostrarPeliculas()


def eliminarTitulo(titulo, index):
    global titulos
    leerPalabras()

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
    with open ('wordsIndex.csv', 'w',newline='') as new_words_file:
        csv_writer = csv.writer(new_words_file)
        csv_writer.writerow(firstRowWords)
        for t in titulos:
            csv_writer.writerow(t)

def eliminarCodigo(codigo):
    global codigos
    leerCodigos()
    index = buscar(int(codigo), codigos)
    codigos.pop(index)
    with open ('codesIndex.csv', 'w',newline='') as new_codes_file:
        csv_writer = csv.writer(new_codes_file)
        csv_writer.writerow(firstRowCodes)
        for c in codigos:
            csv_writer.writerow(c)


def compactar(index):
    global titulos
    global codigos
    leerPalabras()
    leerCodigos()

    for codigo in codigos:
        if codigo[1] > index:
            codigo[1] = codigo[1]-1
    for i in range(len(titulos)):
        for j in range(len(titulos[i][1])):
            if titulos[i][1][j] > index:
                titulos[i][1][j] = (titulos[i][1][j])-1
    with open ('codesIndex.csv', 'w',newline='') as new_codes_file:
        csv_writer = csv.writer(new_codes_file)
        csv_writer.writerow(firstRowCodes)
        for c in codigos:
            csv_writer.writerow(c)
    with open ('wordsIndex.csv', 'w',newline='') as new_words_file:
        csv_writer = csv.writer(new_words_file)
        csv_writer.writerow(firstRowWords)
        for t in titulos:
            csv_writer.writerow(t)


def rentarPelicula():
    '''
    Funcion que pide el numero de socio y el codigo de la pelicula a rentar. En caso de que la pelicula
    exista y no este alquilada, se alquila al socio. En caso contrario, se muestra un mensaje indicando
    que esta alquilada o que no existe.
    '''
    global peliculas
    leerPeliculas()
    global codigos
    leerCodigos()
    mostrarPeliculas()
    info = pedirDatosRenta()
    indice = buscar(info[1], codigos, True)

    if indice != -1:
        indicePelicula = codigos[indice][1]
        nombre = peliculas[indicePelicula][2].capitalize()
        if int(peliculas[indicePelicula][4]) == -1:
            peliculas[indicePelicula][4] = info[0]
            with open ('movies.csv', 'w',newline='') as new_csv_file:
                csv_writer = csv.writer(new_csv_file)
                csv_writer.writerow(firstRowMovies)
                for p in peliculas:
                    csv_writer.writerow(p)
            print("\nYou have rented '{}'.".format(nombre))
            return True
        else:
            print("\nThe movie '{}' is already rented.".format(nombre))
            return False
    else:
        print('\nNO MOVIE WITH THAT CODE.')
        return False


def devolverPelicula():
    '''
    Funcion que pide el codigo de la pelicula a devolver. En caso de que la pelicula
    exista y este alquilada, se acepta la devolucion. En caso contrario, se muestra un mensaje indicando
    que no esta alquilada o que no existe.
    '''
    global peliculas
    leerPeliculas()
    global codigos
    leerCodigos()
    mostrarPeliculas()
    codigo = pedirCodigo(
        "\nIngrese el codigo de la pelicula que desea devolver: ")
    indice = buscar(codigo, codigos, True)

    if indice != -1:
        indicePelicula = codigos[indice][1]
        nombre = peliculas[indicePelicula][2].capitalize()
        if peliculas[indicePelicula][4] != '-1':
            peliculas[indicePelicula][4] = -1
            with open ('movies.csv', 'w',newline='') as new_csv_file:
                csv_writer = csv.writer(new_csv_file)
                csv_writer.writerow(firstRowMovies)
                for p in peliculas:
                    csv_writer.writerow(p)
            print("\nHa devuelto '{}'.".format(nombre))
            return True
        else:
            print(
                "\nThe movie '{}' is not rented and cant be returned.".format(nombre))
            return False
    else:
        print("\nNO MOVIE WITH THAT CODE.")
        return False


def consultaPorCodigo():
    '''
    Funcion que pide el codigo de la pelicula y ve si existe. Si existe, muestra si esta alquilada o no. 
    Si no, muestra que no hay una pelicula con ese codigo.
    '''
    global peliculas
    leerPeliculas()
    global codigos
    leerCodigos()

    codigo = pedirCodigo("\nType the code of the movie you wanna CHECK: ")
    indice = buscar(codigo, codigos, True)
    
    print("\nSEARCH RESULTS:\n")
    if indice != -1:
        indicePelicula = codigos[indice][1]
        nombre = peliculas[indicePelicula][2].capitalize()
        if peliculas[indicePelicula][4] != '-1':
            print("\nThe movie '{}' is rented.".format(nombre)) 
            return True     
        else:
            print("\nThe movie '{}' is not rented.".format(nombre))     
            return False 
    else:
        print("\nNO MOVIE WITH THAT CODE.")
        return False
        

def consultaPorPalabras():
    '''
    Funcion que pide una o dos palabras del titulo de la pelicula y ve si hay peliculas cuyo
    titulo las contenga. Si hay, muestra si estan alquiladas o no. Si no, muestra que no hay
    una pelicula con ese codigo.
    '''
    global peliculas
    global titulos
    global peliculas
    
    leerPeliculas()
    
    leerPalabras()

    palabras = pedirPalabras()
    peliculaPedida = []

    print("\nSEARCH RESULTS:\n")
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
            print("\nNO MOVIE WITH THAT/THOSE WORD/WORDS.")
            return False

    if len(peliculaPedida):
        for indicePelicula in peliculaPedida:
            nombre = peliculas[indicePelicula][2].capitalize()
            codigo = peliculas[indicePelicula][1]
            if peliculas[indicePelicula][4] != '-1':
                print("\n   The movie with the title '{}' and the code {} is rented.".format(nombre, codigo))      
            else:
                print("\n   The movie with the title '{}' and the code {} is not rented.".format(nombre, codigo)) 
        return True
    else:
        print("\nNO MOVIE WITH THAT/THOSE WORD/WORDS.")
        return False
    
def mostrarPeliculas():
    x = PrettyTable()

    peliculas = []
    with open ('movies.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for movie in csv_reader:
            peliculas.append(movie)
    x.field_names= peliculas[0]
    for i in range (1,len(peliculas)):
        x.add_row(peliculas[i])
    print(x)
    print('\nIF LOGICAL HAVE A "*", THE MOVIE WAS LOGICALLY REMOVED\nIF MEMBER NUMBER IS "-1", THE MOVIE IS NOT RENTED RIGTH NOW')



