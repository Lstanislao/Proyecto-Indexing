def pedirEntero(message, maxi):
    valido = False
    while not valido:
        try:
            lenght = 0
            num = 0
            while (lenght > maxi or lenght == 0):
                num = int(input(message))
                lenght = len(str(num))
                if (lenght > maxi or lenght == 0):
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
        if entradaValidar.isalnum() == True and len(entrada) <= maxi:
            valido = True
        else:
            print('''
             Invalido. Se pueden ingresar como maximo 30 caracteres.
            ''')
    return entrada

def pedirPalabras():
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
    return pedirEntero(mensaje, 5)


def pedirDatosRenta():
    socio = pedirEntero("Ingrese su numero de socio: ", 5)
    pelicula = pedirCodigo(
        "Ingrese el codigo de la pelicula que desea rentar: ")
    return socio, pelicula
