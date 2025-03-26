#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

# Definimos el límite inferior y superior del intervalo
lower = 1
upper = 500

# Imprimimos el encabezado para la lista de números primos
print("Números primos entre", lower, "y", upper, "son:")

# Iteramos a través de cada número en el intervalo especificado
for num in range(lower, upper + 1):
   # Todos los números primos son mayores que 1
   if num > 1:
       # Comprobamos si el número es primo
       for i in range(2, num):
           # Si el número es divisible por cualquier número menor que él, no es primo
           if (num % i) == 0:
               break
       else:
           # Si no se encontró ningún divisor, el número es primo y lo imprimimos
           print(num)