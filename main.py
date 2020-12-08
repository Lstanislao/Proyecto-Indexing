from tables import*
from prettytable import PrettyTable
# from pyfiglet import Figlet
from time import sleep

import csv

menu = True
# f = Figlet(font='slant')
# print (f.renderText("BLOCKBUSTER'S"))
while menu:
    decision = input("\n\nWelcome to Blockbuster's System! \n\n  If you wanna ADD A NEW MOVIE, type 1\n\n  If you wanna DELETE A MOVIE, type 2\n\n  If you wanna CHECK IF A MOVIE IS RENTED, type 3\n\n  If you wanna RENT A MOVIE, type 4\n\n  If you wanna RETURN A MOVIE, type 5\n\n  Type 6 to SHOW ALL THE MOVIES\n\n  Type 7 to PACK\n\n  Type any other thing to EXIT\n\n")
    
    if decision == "1":
        agregarPelicula()
        print("\n\nMovie ADDED SUCCESSFULLY!\n\n")
    elif decision == "2":
        if eliminarPelicula():
            print("\n\nMovie DELETED SUCCESSFULLY!\n\n")
        else:
            pass
    elif decision == "3":
        busqueda = input("\n  If you wanna search by CODE, type 1\n\n  If you wanna search by ONE OR TWO WORDS, type 2\n\n")
        if busqueda == "1":
            if consultaPorCodigo():
                print("\n\nMovie CHECKED SUCCESSFULLY!\n\n")
            
        if busqueda == "2":
            if consultaPorPalabras():
                print("\n\nMovie CHECKED SUCCESSFULLY!\n\n")
                
    elif decision == "4":
        if rentarPelicula():
            print("\n\nRENT SUCCESSFUL!\n\n")

    elif decision == "5":
        if devolverPelicula():
            print("\n\nMovie RETURNED SUCCESSFULLY!\n\n")
        else: 
            pass
    elif decision == "6":
        mostrarPeliculas()
    elif decision == "7":
        packing()
        print("\n\nPACKING SUCCESSFUL!\n\n")
    else:
        menu = False
    sleep(6)
