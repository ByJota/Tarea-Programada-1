from os import system
from funciones import *

def menu():
    '''
    Funcion: Es un menu que muestra las funciones del programa de alquiles
    entradas:
    -edificio(matriz)
    salidas:
    - re direcciona a la funcion indicada por el usuario
    '''
    print("Menu de opciones:")
    print("")
    print("-1.Crear Expediente\n"+
              "-2.Crear Expediente\n"+
              "-3.Registrar Anotaciones\n"+
              "-4.Apartar animales de mi zoológico\n"+
              "-5.Exportar la base de datos\n"+
              "-6.Mostrar base de datos del zoológico"+
              "-7.Salir del menu\n") 
    print("")
    opcion=int(input("Opcion:"))
    if opcion==1:
        system("cls")
    elif opcion==2:
        system("cls")

    elif opcion==3:
        system("cls")

    elif opcion==4:
        system("cls")

    elif opcion==5:
        system("cls")

    elif opcion==6:
        system("cls")

    elif opcion==7:
        print("¿Seguro que quiere salir del Programa?\n"+
              "1.Si\n"+
              "2.No")
        respuesta=int(input("R/"))
        if respuesta==1:
            system("exit")
        else:
            system("cls")
            menu()
    else:
        print("opcion invalida. ")
    return

#Programa Principal 

print("Programa Zoologico".center(100,"="))
agregarAnimal()
