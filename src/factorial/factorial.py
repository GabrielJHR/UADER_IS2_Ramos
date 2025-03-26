#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("El factorial de un número negativo no existe")
        return 0
    elif num == 0: 
        return 1
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

# Verificamos si se ha pasado un argumento
if len(sys.argv) <= 1:
    # Si no se ha pasado un argumento, solicitamos al usuario que ingrese un número
    num = int(input("Debe informar un número: "))
else:
    num = int(sys.argv[1])

# Imprimimos el resultado del factorial
print("El factorial de", num, "es", factorial(num))

