#!/usr/bin/env python
#coding:utf-8
#################### #################### #################### #################### #################### #################### 
                                  #################### PROGRAMA DE COMPRAS #################### 
#################### #################### #################### #################### #################### #################### 

"""╔═══╗ ♪♪   
 ♫ ║███║ ♫ Created on Fri Jun 19 17:49:02 2020
   ║(●)║ ♫ @author: Norma Cala Martínez - Normisss11  
 ♪♪╚═══╝ ♫ email: normisss11@gmail.com 
"""

## Importa para poder acceder al plano donde estan las funciones.

import funLib  as af
#from funLi import iva as f_iva # Otra forma de llamar las funciones.

print('\n\n\n        *****************************************************************')
print("        ***  Experiencia de compra, gracias por utilizar el servicio! ***")
print('        *****************************************************************')


#Para realizar el llamado de las funciones que tenemos en el plano de funLib
nombre = af.getNombre()
valor  = af.getValorCompra()           

print('\n\n  Descuento:   ',af.getdescuentazo()*valor)
print('  Iva:         ',af.iva(valor))   # ,af.iva(valor,0.1)) tambien le podemos poner asi. 
print('  Valor compra:',valor)

valor_a_pagar =valor-valor*af.getdescuentazo() + af.iva(valor)  # + af.iva(valor,0.1)

print("\n\n *** RESUMEN TOTAL ***\n ",nombre, 'el valor a pagar es de: $', valor_a_pagar )




