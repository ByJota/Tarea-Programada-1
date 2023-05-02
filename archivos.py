#Elaborado por Josue Salazar ,Jenny King 
#Fecha de creacion 30/04/23 1:20pm
#Ultima modificacion 30/04/23 1:20pm
#version 3.10.6
#importacion de librerias
import pickle

def graba(nomArchGrabar,lista):
    #Función que graba un archivo en una lista 
    try:
        f=open(nomArchGrabar,"wb")
        #print("1.Voy a grabar el archivo: ", nomArchGrabar)
        pickle.dump(lista,f)
        #print("1.Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
    except TypeError:
        print('Error: Se esperaba un dato str y una lista/matriz/tupla/str')
    except:
        print('Error inesperado al guardar archivo:'+ nomArchGrabar)

def lee (nomArchLeer):
    #Función que lee un archivo en una lista 
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        #print("2. Voy a leer el archivo: ", nomArchLeer)
        lista = pickle.load(f)
        #print("2. Voy a cerrar el archivo: ", nomArchLeer)
        f.close()
    except TypeError:
        print('No se pudo leer adecuadamente')
    except FileNotFoundError:
        print("El archivo:", nomArchLeer,' aun no contiene nada, Utilice la opcion 1 para crear un zoologico primero')
        return False
    return lista

def leeInfo (nomArchLeer):
    #Función que lee un archivo en una lista 
    lista=[]
    try:
        f=open(nomArchLeer,"rb")
        #print("2. Voy a leer el archivo: ", nomArchLeer)
        lista = pickle.load(f)
        #print("2. Voy a cerrar el archivo: ", nomArchLeer)
        f.close()
    except TypeError:
        print('No se pudo leer adecuadamente')
    except FileNotFoundError:
        print("El archivo:", nomArchLeer,' aun no contiene nada, Utilice la opcion 2 para crear un Expediente con todos los animales del zoologico.')
        return False
    return lista

def grabaNoBinario(nomArchGrabar,lista):
    #Función que graba un archivo en una lista 
    try:
        f=open(nomArchGrabar,"w")
        #print("1.Voy a grabar el archivo: ", nomArchGrabar)
        f.write(lista)
        #print("1.Voy a cerrar el archivo: ", nomArchGrabar)
        f.close()
    except TypeError:
        print('Error: Se esperaba un dato str y una lista/matriz/tupla/str')
    except:
        print('Error inesperado al guardar archivo:'+ nomArchGrabar)