"""
Este módulo proporciona una implementación de un Singleton para calcular factoriales.
"""

class FactorialSingleton:
    """
    Clase Singleton para calcular el factorial de un número.
    """
    _instance = None

    def __new__(cls):
        """
        Crea una única instancia de la clase.
        """
        if cls._instance is None:
            cls._instance = super(FactorialSingleton, cls).__new__(cls)
        return cls._instance

    def calcular_factorial(self, n):
        """
        Calcula el factorial de un número no negativo.

        :param n: Número entero no negativo
        :return: Factorial de n
        :raises ValueError: Si n es negativo
        """
        if n < 0:
            raise ValueError("El número debe ser no negativo")
        if n in {0, 1}:
            return 1
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial


# Este código crea una instancia del Singleton, calcula los factoriales de 5 y 4,
# e imprime los resultados junto con los IDs de los objetos para demostrar que
# se está utilizando la misma instancia (mismo ID) para ambos cálculos
singleton = FactorialSingleton()

resultado = singleton.calcular_factorial(5)
print("Factorial de 5:")
print(f"El id del objeto es: {id(singleton)}")
print(f"El factorial de 5 es: {resultado}")

print("--------------------------------")

resultado = singleton.calcular_factorial(4)
print("Factorial de 4:")
print(f"El id del objeto es: {id(singleton)}")
print(f"El resultado es: {resultado}")
