

def pedirEntero(message, maxi):
    valido = False
    while not valido:
        try:
            lenght = 0
            num = 0
            while (lenght < maxi):
                num = int(input(message))
                lenght = len(str(num))
                if lenght < maxi:
                    print('El numero ingresado debe ser de logintud maxima: ', maxi)
            valido = True
        except ValueError:
            print('''
            Invalido, lo ingresado no es un numero
            ''')
    return num


def pedirString(messages, maxi):
    valido = False
    while not valido:
        entrada = input(messages)
        entradaValidar = entrada.replace(" ", '')
        if entradaValidar.isalnum() == True and len(entrada) <= 30:
            valido = True
        else:
            print('''
             Invalido. Se pueden ingresar como maximo 30 caracteres.
            ''')
    return entrada


'''def pedirPelicula():
    valido = False
    while not valido:
        codigo = pedirEntero("Ingrese el codigo de la pelicula: ", 5)
        if buscar(codigo, codigos, True) == -1:
            valido = True
        else:
            print("Ya existe uuna pelicula con ese codigo")
    valido = False
    while not valido:
        titulo = pedirString('Ingrese el nombre de la pelicula: ', 30)
        titulo = titulo.lower()
        palabras = titulo.split(" ")
        for palabra in palabras:
            print(buscar(palabra, titulos, True))
            if buscar(palabra, titulos, True) == -1:
                valido = True
        if not valido:
            print('Ya existe una pelicula con este mismo titulo')
    alquiler = pedirEntero(
        'Ingrese el costo diario del alquiler de la pelicula: ', 8)
    return ["", codigo, titulo, alquiler, -1]'''


def pedirDatosRenta():
    socio = pedirEntero("Ingrese su numero de socio: ", 5)
    pelicula = pedirEntero(
        "Ingrese el codigo de la pelicula que desea rentar: ", 5)
    return socio, pelicula
