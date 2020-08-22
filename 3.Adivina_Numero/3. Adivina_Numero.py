#!/usr/bin/env python
#coding:utf-8
#################### #################### #################### #################### #################### #################### 
                                  #################### PROGRAMA DE ADIVINA UN NÚMERO #################### 
#################### #################### #################### #################### #################### #################### 

"""╔═══╗ ♪♪   
 ♫ ║███║ ♫ Created on Fri Jun 19 19:49:02 2020
   ║(●)║ ♫ @author: Norma Cala Martínez - Normisss11  
 ♪♪╚═══╝ ♫ email: normisss11@gmail.com 
"""

import Librerias_Adivina_Numero  as libadiv

print('\n\n\n        *****************************************************************')
print("        **** JUEGO DE ADIVINAR UN NÚMERO SEGÚN INTENTOS Y RANGOS ! ****")
print('        *****************************************************************')
 
gano = False
salir = False    
       

while(salir == False):        
    
    nombre = libadiv.getNombre()
    totalintentos = libadiv.getintentos()
    rango_ini,rango_fin, num_a_adivinar = libadiv.getnumero()
    libadiv.getsaludo(nombre,totalintentos,rango_ini,rango_fin)
     
    #print("*** ==> " + str(num_a_adivinar))
    
    intentos = 1
    
    while(intentos <= totalintentos):

        numero_usuario = libadiv.getingresaNumero()
        
        if numero_usuario == -2:        
            salir = True
            break                    
        
        if(libadiv.getacerto(num_a_adivinar,numero_usuario)== 0):
            print('\n    ¡Eres un ganador, Acertaste!')        
            print('\n       *****************************','\n       *****  ¡Felicitaciones! *****','\n       *****************************')  
            gano = True
            break
        
        elif(libadiv.getacerto(num_a_adivinar,numero_usuario)==1):        
            print('\n    * Ese número no es... intenta con un número más grande.\n     * Te quedan =>',totalintentos-intentos,'<= intentos.','\n     * Si deseas salir digita -2')
            intentos+=1        
                    
        else:        
            print('\n    * Ese número no es... intenta con un número más pequeño.\n    * Te quedan =>',totalintentos-intentos,'<= intentos.','\n     * Si deseas salir digita -2')        
            intentos+=1
                        
    if intentos > totalintentos:
        print('\n       *****************************','\n       ****  ¡GAME OVER! ****','\n       *****************************')    
                
    if salir == False:
        opcion = str(input("\n    ¿Deseas volver a jugar? (S/N)  "))            
        if(opcion == 'n'):        
            salir = True 
    else:
        salir = True
           
    if salir:
        print('\n       *****************************','\n       ****  ¡VUELVE PRONTO! ****','\n       *****************************')        
    


       
        
#Modifica este código para:
# *1 crear libreria con las funciones -- ya.
# *2 Solicitar al usuario los rangos en los cuales desea adivinar el número    
# *3 Que el usuario pueda ingresar el numero de intentos para adivinar
# 4 Visualizar el número de intentos restantes     
# *5 Ejecutar juego hasta que el usuario decida no seguir jugando.   