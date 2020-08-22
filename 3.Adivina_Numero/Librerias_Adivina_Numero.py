#!/usr/bin/env python
#coding:utf-8
                              #################### PROGRAMA DE ADIVINA UN NÚMERO #################### 

"""╔═══╗ ♪♪   
 ♫ ║███║ ♫ Created on Wed Jul  1 21:33:43 2020
   ║(●)║ ♫ @author: Norma Cala Martínez - Normisss11  
 ♪♪╚═══╝ ♫ email: normisss11@gmail.com 
"""

import random

def getnumero():
    while True:            
        try:    
            rango_ini = int(input('  Digita rango número inicial ==> '))
            rango_fin = int(input('  Digita rango número final   ==> '))            
            return (rango_ini,rango_fin,random.randint(rango_ini,rango_fin))            
        except Exception as error:
            print('    * Datos erroneos',error)

def getacerto(numero, numerousuario):
    if(numero == numerousuario):
        return 0
    elif(numero > numerousuario):
        return 1
    else:
        return -1

def getNombre():
     ingresa_nombre = input('  Digita nombre del jugador   ==> ')
     return ingresa_nombre

def getintentos():
    while True:
        try:            
            ingresa_intentos = int(input('  Digita número de intentos   ==> '))
            return ingresa_intentos
        except Exception as error:
            error


def getsaludo(nombre,intentos,rango_ini,rango_fin):            
    print("\n\n           REVISA TU CONFIGURACIÓN DE JUEGO")
    print("       ----------------------------------------------")
    print("       --- Nombre:         ", nombre)
    print("       --- Intentos:       ", intentos)
    print("       --- Rango inicial:  ", rango_ini)
    print("       --- Rango final:    ", rango_fin)
    print("       ----------------------------------------------")    
    print("\n                     EMPECEMOS A JUGAR!")    

    
def getingresaNumero():
    return int(input('  Digita número ==> '))