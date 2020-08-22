#!/usr/bin/env python
#coding:utf-8
               #################### LIBRERÍAS DEL PROGRAMA DE COMPRAS #################### 

"""╔═══╗ ♪♪   
 ♫ ║███║ ♫ Created on Fri Jul 01 18:49:02 2020
   ║(●)║ ♫ @author: Norma Cala Martínez - Normisss11  
 ♪♪╚═══╝ ♫ email: normisss11@gmail.com 
"""

# Almacen de funciones listas para ser llamadas en las librerias.

def iva(valor,iva = 0.16):
    valor = valor*iva
    return valor

def ica(valor, ica = 0.2):
    valor = valor*ica
    return valor

def getDescuento(edad):
    
            if(edad > 18 and edad <= 25):                
                return 0.10
            elif(edad > 25 and edad <= 40):
                return 0.15
            else:
                return 0.20
 
    
def getNombre():
    return input('  Ingrese nombre ==> ')

def getValorCompra():
        while True:            
            try:
                return float(input('  Valor compra ==> $ '))
            except Exception as error:
                print('  Datos erróneos',error)  

def getdescuentazo():
    while True:
        try:
            descuento = getDescuento(int(input('  Digite edad ==> ')))          
            return descuento
        except Exception as error:
             print('  Datos erróneos',error)        
    
    
    