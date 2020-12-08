from funciones import*
<<<<<<< HEAD
=======
from prettytable import PrettyTable
>>>>>>> gebrayel
import csv

firstRowMovies = ['Logical','CodeNumber','MovieName','DailyPrice','Member']
firstRowCodes = ['Code','Index']
firstRowWords = ['Words','Index']
peliculas = [
<<<<<<< HEAD
    ['*', 11111, 'El rey leon', 12456, -1], ['', 10000, 'rapidos y furiosos 2', 12456, -1], ['*', 55555, 'la bella y la bestia', 12564, -1], ['', 85203, 'la princesa y el sapo', 12651, -1], ['*', 12378, 'furisos sapo y la bestia', 12564, -1]

]

titulos = [

    ['2', [1]], ['bella', [2]], ['bestia', [2, 4]], ['el', [0, 3]], ['furiosos', [1]], ['furisos', [4]], ['la', [2, 2, 3, 4]], ['leon', [0]], ['princesa', [3]], ['rapidos', [1]], ['rey', [0]], ['sapo', [3, 4]], ['y', [1, 2, 3, 4]]
=======
]

titulos = [                                                                                                    
>>>>>>> gebrayel
]

codigos = [
    ]


def pedirPelicula():
    valido = False
    while not valido:
        codigo = pedirEntero("Ingrese el codigo de la pelicula: ", 5)
        print(buscar(codigo, codigos))
        if buscar(codigo, codigos) == -1:
            valido = True
        else:
            print("Ya existe uuna pelicula con ese codigo")
    valido = False
    while not valido:
        titulo = pedirString('Ingrese el nombre de la pelicula: ', 30)
        titulo = titulo.lower()
        palabras = titulo.split(" ")
        for palabra in palabras:
            if buscar(palabra, titulos) == -1:
                valido = True
        if not valido:
            print('Ya existe una pelicula con este mismo titulo')
    alquiler = pedirEntero(
        'Ingrese el costo diario del alquiler de la pelicula: ', 8)
    return ["", codigo, titulo, alquiler, -1]


def agregarPelicula():
    global peliculas
    peliculas = []
    peli = pedirPelicula()
    with open ('movies.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for movie in csv_reader:
            peliculas.append(movie)
        peliculas.append(peli)
        print(peliculas)

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
    titulos = []
    with open ('wordsIndex.csv', 'r') as words_file:
        csv_reader = csv.reader(words_file)
        next(csv_reader)
        contador = 0
        for w in csv_reader:
            titulos.append(w)
            titulos[contador][1] = titulos[contador][1].strip('][').split(',')
            for i in range (len(titulos[contador][1])):
                print(titulos[contador][1][i] )
                titulos[contador][1][i] = int(titulos[contador][1][i])
            contador += 1

    print('titulos 1')
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
    for title in titulos:
        print(title[1])
    with open ('wordsIndex.csv', 'w',newline='') as new_words_file:
        csv_writer = csv.writer(new_words_file)
        csv_writer.writerow(firstRowWords)
        for t in titulos:
            csv_writer.writerow(t)
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
    print('codigos: ', codigos)


def eliminarPelicula():
    global codigos
    global peliculas
    codigos = []
    peliculas = []
    with open ('movies.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for movie in csv_reader:
            peliculas.append(movie)
    with open ('codesIndex.csv', 'r') as codes_file:
        csv_reader = csv.reader(codes_file)
        next(csv_reader)
        contador = 0
        for c in csv_reader:
            codigos.append(c)
            for i in range(2):
                codigos[contador][i] = int(codigos[contador][i])
            contador+=1
    print(codigos)
    print('arriba')
    codigo = pedirCodigo(
        "\nIngrese el codigo de la pelicula que desea eliminar: ")
    fila = buscar(codigo, codigos, True)
    
    if fila != -1:
        indicePelicula = codigos[fila][1]
        if peliculas[indicePelicula][4] == '-1':
            peliculas[indicePelicula][0] = "*"
            with open ('movies.csv', 'w',newline='') as new_csv_file:
                csv_writer = csv.writer(new_csv_file)
                csv_writer.writerow(firstRowMovies)
                for p in peliculas:
                    csv_writer.writerow(p)
            return True
        else:
            print("YOUR CANT DELETE A MOVIE THAT IS RENTED")
            return False
    else:
        print("\nNO MOVIE WITH THAT CODE IN THE SYSTEM")
        return False


def packing():
    global peliculas
    peliculas = []
    with open ('movies.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for movie in csv_reader:
            peliculas.append(movie)
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
            with open ('movies.csv', 'w',newline='') as new_csv_file:
                csv_writer = csv.writer(new_csv_file)
                csv_writer.writerow(firstRowMovies)
                for p in peliculas:
                    csv_writer.writerow(p)
            compactar(index)
        else:
            i = i+1


def eliminarTitulo(titulo, index):
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
                print(titulos[contador][1][i] )
                titulos[contador][1][i] = int(titulos[contador][1][i])
            contador += 1
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
    index = buscar(int(codigo), codigos)
    codigos.pop(index)
    with open ('codesIndex.csv', 'w',newline='') as new_codes_file:
        csv_writer = csv.writer(new_codes_file)
        csv_writer.writerow(firstRowCodes)
        for c in codigos:
            csv_writer.writerow(c)


def compactar(index):
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
                print(titulos[contador][1][i] )
                titulos[contador][1][i] = int(titulos[contador][1][i])
            contador += 1
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
    global peliculas
    peliculas = []
    with open ('movies.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for movie in csv_reader:
            peliculas.append(movie)
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
            print(peliculas)
            print("Ha rentado '{}'.".format(nombre))
            return True
        else:
            print("La pelicula '{}' ya se encuentra alquilada.".format(nombre))
            return False
    else:
        print('No hay una pelicula registrada con el codigo ingresado.')
        return False


def devolverPelicula():
    global peliculas
    peliculas = []
    with open ('movies.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for movie in csv_reader:
            peliculas.append(movie)
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
    global peliculas
    peliculas = []
    with open ('movies.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for movie in csv_reader:
            peliculas.append(movie)
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

    codigo = pedirCodigo("\nIngrese el codigo de la pelicula que desea consultar: ")
    indice = buscar(codigo, codigos, True)
    
    print("\nRESULTADOS DE BUSQUEDA:\n")
    if indice != -1:
        indicePelicula = codigos[indice][1]
        nombre = peliculas[indicePelicula][2].capitalize()
        if peliculas[indicePelicula][4] != '-1':
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
    global peliculas
    peliculas = []
    with open ('movies.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for movie in csv_reader:
            peliculas.append(movie)
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
                print(titulos[contador][1][i] )
                titulos[contador][1][i] = int(titulos[contador][1][i])
            contador += 1

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
            if peliculas[indicePelicula][4] != '-1':
                print(peliculas)
                print("\n   La pelicula de titulo '{}' y codigo {} se encuentra alquilada.".format(nombre, codigo))      
            else:
                print("\n   La pelicula de titulo '{}' y codigo {} no esta alquilada.".format(nombre, codigo)) 
        return True
    else:
        print("\nNo hay una pelicula registrada cuyo titulo contenga esa(s) palabra(s).")
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



