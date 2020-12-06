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
                    print('El numero ingresado debe ser de logintud: ', maxi)
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
             Invalido
            ''')
    return entrada


def pedirPelicula():
    codigo = pedirEntero("Ingrese el codigo de la pelicula: ", 5)
    titulo = pedirString('Ingrese el nombre de la pelicula: ', 30)
    alquiler = pedirEntero(
        'Ingrese el costo diario del alquieler de la pelicula: ', 5)
    return [True, codigo, titulo, alquiler, -1]



