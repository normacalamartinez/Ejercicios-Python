
#################### #################### #################### #################### #################### #################### 
               #################### PROGRAMA DE ATENCIÓN AL CLIENTE DE LA KONRAD LORENZ #################### 
#################### #################### #################### #################### #################### #################### 
"""
Created on Fri Jun 19 17:49:02 2020
@author: Norma Cala
"""

### Llamado de funciones de otro archivo a través de librerías.
import Librerias_Atencion_al_Cliente_Konrad  as lib_ac



encabezado = lib_ac.getencabezado()

print("""            Hola!, es un gusto saludarte, Bienvenido a la Konrad Lorenz.
      Queremos que nos cuentes más de ti para personalizar tus servicios, por favor. \n""")


nombre = lib_ac.getnombre()
estatura = lib_ac.getestatura()
edad = lib_ac.getedad()
direccion = lib_ac.getdireccion()
telefono = lib_ac.gettelefono()
programa = lib_ac.getprograma()
lib_ac.getvisualizardatos(nombre,edad,estatura,direccion,telefono,programa)


### Usaremos una variable bool para indicar si el usuario desea continuar utilizando el programa o no
continuar = True

### Este ciclo se mantiene en ejecución hasta que el usuario desee salir
while continuar:
            
    # Solicitamos opción al usuario
    escribir_mensaje = str(input("\n\n    ¿Deseas modificar datos ingresados? (S/N)  ")) 

    # Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if escribir_mensaje == "S" or escribir_mensaje == "s" or escribir_mensaje == "":
    
            
        opcion = lib_ac.getopcionmodificar()            
        
        if(opcion == 1):
            print("\n   El nombre ingresado anteriormente es   => ", nombre)
            nombre = lib_ac.getnombre ()
            lib_ac.getresultadoactualizar()
                
        elif(opcion == 2):
            print("\n   Año/nacimento ingresado anteriormente  => ", edad)
            edad = lib_ac.getedad()
            lib_ac.getresultadoactualizar()
             
        elif(opcion == 3):
            print("\n   La estatura ingresada anteriormente es => ", estatura)
            estatura = lib_ac.getestatura()
            lib_ac.getresultadoactualizar()
             
        elif(opcion == 4):
            print("\n   La direccion ingresada anteriormente es => ", direccion)
            direccion = lib_ac.getdireccion()
            lib_ac.getresultadoactualizar()
             
        elif(opcion == 5):
            print("\n   El teléfono ingresado anteriormente es => ", telefono)
            lib_ac.gettelefono()
            lib_ac.getresultadoactualizar()
             
        elif(opcion == 6):
            print("\n   El programa ingresado anteriormente es => ", programa)
            programa = lib_ac.getprograma()
            lib_ac.getresultadoactualizar()
            
        elif(opcion == 7):
            lib_ac.getvisualizardatos(nombre,edad,estatura,direccion,telefono,programa)         
            
        else:
            lib_ac.getalerta()
            
        
    elif escribir_mensaje == "N" or escribir_mensaje == 'n':
        continuar = False
    # En caso que sea otra respuesta, vamos a decidir salir.Así, en la siguiente iteración el ciclo terminará
    else:
        lib_ac.getalerta()

#Mensaje de salida, una vez que el ciclo ha terminado.

print('\n\n\n        *****************************************************************')
print("        **** Gracias por usar el servicio de atención, Hasta pronto! ****")
print('        *****************************************************************')






