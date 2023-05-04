#Elaborado por Josue Salazar ,Jenny King 
#Fecha de creacion 29/04/23 1:20pm
#Ultima modificacion 04/05/23 12:07pm
#version 3.10.6
#importacion de librerias
import os
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
            miZoo=lee(nombre)
            matriz=leeInfo(informacion)
            print("Programa zoológico".center(100,"="))
            print(
      "           |-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|\n"+
      "           |          ZOOLOGICO            |\n"+
      "           |-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-|\n"+
      "------------------------------------------------------------------- \n"+
      "|  Opciones del menu:                      |                      |\n"+
      "|                                          |                      |\n"
      "|  1.Agregar animales                      |     *-*-*-*-*-*-*    |\n"+
      "|  2.Crear Expedientes                     |     '  ABIERTO  '    |\n"+
      "|  3.Registrar Anotaciones                 |     *-*-*-*-*-*-*    |\n"+
      "|  4.Apartar animales de mi zoológico      |                      |\n"+
      "|  5.Exportar la base de datos             |                      |\n"+
      "|  6.Mostrar base de datos del zoológico   |      **********      |\n"+
      "|  7.Salir del programa                    |     *          *     |\n"+
      "|                                          |     *          *     |\n"+
      "| ---------------------------------------- |     *          *     |\n"+
      "|         |          |          |          |     *          *     |\n"+
      "-------------------------------------------------------------------\n"+
      "")
            opcion=int(input("Opción :"))
            if opcion==1:
                print("Cargando...")
                time.sleep(3)
                os.system("cls")
                agregarAnimal()
                os.system("cls")
            elif opcion==2:
                os.system("cls")
                crearExpediente(miZoo)
                os.system("cls")
            elif opcion==3:
                print("Cargando...")
                time.sleep(3)
                os.system("cls")
                registrarAnotaciones(matriz)
                os.system("cls")
            elif opcion==4:
                print("Cargando...")
                time.sleep(3)
                os.system("cls")
                apartarAnimales(miZoo,matriz)
                os.system("cls")
            elif opcion==5:
                print("Cargando...")
                time.sleep(3)
                os.system("cls")
                exportarDB(matriz)
                os.system("cls")
            elif opcion==6:
                print("Cargando...")
                time.sleep(3)
                os.system("cls")
                crearTablaHTML(matriz)
                input("Presione Enter para continuar:")
            elif opcion==7:
                print("¿Seguro que quiere salir del Programa?\n"+
                    "1.Si\n"+
                    "2.No")
                respuesta=int(input("R/"))
                if respuesta==1:
                    os.system("cls")
                    print('Gracias por usar el sistema.')
                    raise SystemExit
                else:
                    os.system("cls")
                    menu()
            else:
                print("Opción fuera del rango. Digite una entre 1 y 7. ")
                time.sleep(5)
                os.system("cls")
        except ValueError:
            print("Debe digitar una opción del 1 al 7.")
            time.sleep(5)
            os.system("cls")
        except IndexError:
            print("El dato ingresado esta fuera de alcanze.")
            time.sleep(5)
            os.system("cls")
#Programa Principal 
menu()

