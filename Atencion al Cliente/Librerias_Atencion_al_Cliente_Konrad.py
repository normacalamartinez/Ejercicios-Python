
               #################### LIBRERÍAS DEL PROGRAMA DE ATENCIÓN AL CLIENTE DE LA KONRAD LORENZ #################### 

"""
Created on Wed Jul  1 21:04:24 2020
@author: Norma Cala
"""


# Almacen de funciones listas para ser llamadas en las librerias.


### Declaración de funciones.
def getencabezado():
    print("""
         ____________________________________________________________________ 
           _  __                         _   _                                           
          | |/ /                        | | | |                                          
          | ' / ___  _ __  _ __ __ _  __| | | |     ___  _ __ ___ _ __  ____             
          |  < / _ \| '_ \| '__/ _` |/ _` | | |    / _ \| '__/ _ \ '_ \|_  /             
          | . \ (_) | | | | | | (_| | (_| | | |___| (_) | | |  __/ | | |/ /              
          |_|\_\___/|_| |_|_|  \__,_|\__,_| |______\___/|_|  \___|_| |_/___|       
         ____________________________________________________________________
    """)

def getalerta():
    print('\n     *** ALERTA: Datos erroneos u opción invalida. ***')
    
def getnombre():
    ingresa_nombre = input("   ¿Cúal es tu nombre y apellido?        ==> ")
    return ingresa_nombre

def getestatura():
    while True:            
        try:            
            ingresa_estatura = float(input("   ¿Cuánto mides?... Dímelo en metros.   ==> "))
            estatura_m = int(ingresa_estatura)
            estatura_cm = int( (ingresa_estatura - estatura_m)*100 )
            return estatura_cm
        except Exception as c:
            getalerta() 

def getedad():        
    while True:            
        try:
            ingresa_anio = int(input("   ¿Cuéntanos en qué año naciste?        ==> "))
            edad = 2020-ingresa_anio                
            return edad
        except Exception as e:
            getalerta()    
            
        
def getdireccion():
    ingresa_direccion = input("   ¿Cúal es tu dirección de residencia?  ==> ")
    return ingresa_direccion

def gettelefono():
    ingresa_telefono = input("   ¿Cúal es tu número de teléfono ?      ==> ")
    return ingresa_telefono
    
def getprograma():
    ingresa_programa = input("   ¿Nombre del programa en el que estás? ==> ")    
    return ingresa_programa
    
def getvisualizardatos(nombre,edad,estatura,direccion,telefono,programa):           
    print("\n\n       Muy bien,", nombre, ", revisa por favor tus datos.")
    print("       ----------------------------------------------")
    print("       --- Nombre:    ", nombre)
    print("       --- Edad:      ", edad, "años")
    print("       --- Estatura:  ", estatura, "centímetros")
    print("       --- Dirección: ", direccion)
    print("       --- Teléfono:  ", telefono)
    print("       --- Programa:  ", programa)
    print("       ----------------------------------------------")    
    
    
def getopcionmodificar():
    print("""          
           ================================
          |     SELECCIONE UNA OPCIÓN      |
          |                                |
          | 1. Modificar Nombre            |
          | 2. Modificar Año de nacimiento |
          | 3. Modificar Estatura          | 
          | 4. Modificar Dirección         |
          | 5. Modificar Teléfono          |
          | 6. Modificar Programa          |
          | 7. Mostrar Datos ingresados    |
          =================================
          """)          
    ingresa_opcion = int(input('   Digíte opción ==> '))
    return ingresa_opcion

def getresultadoactualizar():
    print("\n   ** EXCLENTE => Se encuentran actualizados los datos.!")
    