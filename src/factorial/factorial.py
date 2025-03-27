#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial_OOP.py                                                       *
#* calcula el factorial de un rango de números utilizando OOP              *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

class Factorial:
    def __init__(self):
        pass

    def factorial(self, num): 
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

    def run(self, min, max):
        for num in range(min, max + 1):
            print("El factorial de", num, "es", self.factorial(num))

# Función para procesar el rango
def procesar_rango(rango):
    try:
        if rango.startswith('-'):
            hasta = int(rango[1:])
            desde = 1
        elif rango.endswith('-'):
            desde = int(rango[:-1])
            hasta = 60
        else:
            desde, hasta = map(int, rango.split('-'))
        return desde, hasta
    except ValueError:
        print("Formato de rango inválido. Debe ser '-hasta', 'desde-' o 'desde-hasta' (ej. 4-8).")
        sys.exit()

# Verificamos si se ha pasado un argumento
if len(sys.argv) <= 1:
    # Si no se ha pasado un argumento, solicitamos al usuario que ingrese el rango
    rango = input("Debe informar un rango ('-hasta', 'desde-' o 'desde-hasta'): ")
else:
    rango = sys.argv[1]

# Procesamos el rango
desde, hasta = procesar_rango(rango)

# Creamos una instancia de la clase Factorial y ejecutamos el cálculo
factorial_calculador = Factorial()
factorial_calculador.run(desde, hasta)
