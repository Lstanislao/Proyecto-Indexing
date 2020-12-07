def pedirEntero(message, maxi):
    '''
    Funcion que pide un entero con el maximo de digitos indicado.
    '''
    valido = False
    while not valido:
        try:
            lenght = 0
            num = 0
            while (lenght > maxi or lenght == 0):
                num = int(input(message))
                lenght = len(str(num))
                if (lenght > maxi or lenght == 0):
                    print('El numero ingresado debe ser de longitud maxima: ', maxi)
            valido = True
        except ValueError:
            print('''
            Invalido, lo ingresado no es un numero
            ''')
    return num


def pedirString(messages, maxi):
    '''
    Funcion que pide un string con el maximo de caracteres indicado.
    '''

    valido = False
    while not valido:
        entrada = input(messages)
        entradaValidar = entrada.replace(" ", '')
        if entradaValidar.isalnum() == True and len(entrada) <= maxi:
            valido = True
        else:
            print('''
             Invalido. Se pueden ingresar como maximo 30 caracteres.
            ''')
    return entrada

def pedirPalabras():
    '''
    Funcion que pide un string de maximo 30 caracteres con solo una o dos palabras y devuelve un array
    con las palabras.
    '''
    valido = False
    listaPalabras = []
    while not valido:
        palabras = pedirString("\nIngrese una o dos palabras del titulo de la pelicula a consultar: ", 30)
        listaPalabras = palabras.lower().split(" ")
        if len(listaPalabras) == 1 or len(listaPalabras) == 2:
            valido = True
        else:
            print("\nInvalido. Solo se puede ingresar una o dos palabras.")
    return listaPalabras

def pedirCodigo(mensaje):
    '''
    Funcion que pide un numero de maximo 5 digitos.
    '''
    return pedirEntero(mensaje, 5)


def pedirDatosRenta():
    '''
    Funcion que pide 2 numeros de maximo 5 digitos cada uno y los devuelve.
    '''
    socio = pedirEntero("Ingrese su numero de socio: ", 5)
    pelicula = pedirCodigo(
        "Ingrese el codigo de la pelicula que desea rentar: ")
    return socio, pelicula
