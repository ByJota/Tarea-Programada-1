#Elaborado por Josue Salazar ,Jenny King 
#Fecha de creacion 29/04/23 1:20pm
#Ultima modificacion 29/04/23 1:20pm
#version 3.10.6
#C:\Users\jenki\OneDrive\Escritorio\texto.txt
#importacion de librerias
from os import system
from funciones import *
            
def menu():
    '''
    Funcion: Es un menu que muestra las funciones del sistema de zoológico
    entradas:
    -
    salidas:
    - re direcciona a la funcion indicada por el usuario
    '''
    while True: 
        try:
            print("Programa zoológico".center(100,"="))
            print("Menu de opciones:\n"+
                    "-1.Agregar animal\n"+
                    "-2.Crear Expediente\n"+
                    "-3.Registrar Anotaciones\n"+
                    "-4.Apartar animales de mi zoológico\n"+
                    "-5.Exportar la base de datos\n"+
                    "-6.Mostrar base de datos del zoológico\n"+
                    "-7.Salir del Programa\n") 
            opcion=int(input("Opción :"))
            if opcion==1:
                agregarAnimal()
                system("cls")
            elif opcion==2:
                crearExpediente(miZoo)
                system("cls")
            elif opcion==3:
                registrarAnotaciones(matriz)
                system("cls")
            elif opcion==4:
                system("cls")
                apartarAnimales(miZoo,matriz)
            elif opcion==5:
                system("cls")
                exportarDB(matriz)
            elif opcion==6:
                system("cls")
                crearTablaHTML(matriz)
                #mostrar base de datos
            elif opcion==7:
                print("¿Seguro que quiere salir del Programa?\n"+
                    "1.Si\n"+
                    "2.No")
                respuesta=int(input("R/"))
                if respuesta==1:
                    print('Gracias por usar el sistema.')
                    raise SystemExit
                else:
                    system("cls")
                    menu()
            else:
                print("Opción fuera del rango. Digite una entre 1 y 7. ")
        except ValueError:
            print("Debe digitar una opción del 1 al 7.")
            time.sleep(2)
            system("cls")
        except IndexError:
            print("El dato ingresado esta fuera de alcanze.")
            time.sleep(2)
            system("cls")
#Programa Principal 
menu()

