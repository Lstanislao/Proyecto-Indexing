from tables import*
from funciones import*
from prettytable import PrettyTable

seguir = 1
'''while seguir == 1:
    agregarPelicula()
    print(peliculas)
    seguir = int(input("seguir? "))
    #busqueda = int(input("codigo que desea buscar"))
    #print(buscar(busqueda, codigos))
    print(peliculas)


seguir = 1
while seguir == 1:
    eliminarPelicula(int(input("que vas a eliminar")))
    print(peliculas)
    print(codigos)
    print(titulos)
    print(peliculas)
    seguir = int(input("seguir? "))'''

print(peliculas)
packing()
print(codigos)
print(titulos)
print(peliculas)


menu = True
while menu:
    decision = input("Welcome to Blockbuster's System! \n\n  If you wanna ADD A NEW MOVIE, type 1\n\n  If you wanna DELETE A MOVIE, type 2\n\n  If you wanna CHECK IF A MOVIE IS RENTED, type 3\n\n  If you wanna RETURN A MOVIE, type 4\n\n  Type 5 to PACK\n\n")
