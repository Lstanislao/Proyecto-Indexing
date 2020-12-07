from tables import*
from prettytable import PrettyTable
from time import sleep

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
    decision = input("Welcome to Blockbuster's System! \n\n  If you wanna ADD A NEW MOVIE, type 1\n\n  If you wanna DELETE A MOVIE, type 2\n\n  If you wanna CHECK IF A MOVIE IS RENTED, type 3\n\n  If you wanna RETURN A MOVIE, type 4\n\n If you wanna RENT A MOVIE, type 5\n\n  Type 6 to PACK\n\n  Type any other thing to EXIT\n\n")
    
    if decision == "1":
        agregarPelicula()
        print("\n\nMovie ADDED SUCCESSFULLY!\n\n")
    elif decision == "2":
        if eliminarPelicula():
            print("\n\nMovie DELETED SUCCESSFULLY!\n\n")
    elif decision == "3":
        busqueda = input("If you wanna search by CODE, type 1\nIf you wanna search by ONE OR TWO WORDS, type 2\n")
        if busqueda == "1":
            # checkCodePelicula()
            pass
        if busqueda == "2":
            # checkWordsPelicula()
            pass
        print("\n\nMovie CHECKED SUCCESSFULLY!\n\n")
    elif decision == "4":
        if rentarPelicula():
            print("\n\nMovie RETURNED SUCCESSFULLY!\n\n")
      
    elif decision == "5":
        # rentPelicula()
        print("\n\nMovie RENTED SUCCESSFULLY!\n\n")
    elif decision == "6":
        # pack()
        print("\n\nPACKING SUCCESSFUL!\n\n")
    else:
        menu = False
    sleep(6)

# seguir = 1
# while seguir == 1:
#     agregarPelicula()
#     print(peliculas)
#     seguir = int(input("seguir? "))
#     busqueda = int(input("codigo que desea buscar"))
#     print(buscar(busqueda, codigos))

# eliminarPelicula(11111)
# print(peliculas)
