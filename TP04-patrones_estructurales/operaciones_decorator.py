class Numero:
    """
    Componente base que almacena un valor numérico y permite imprimirlo.
    """
    def __init__(self, valor: float):
        self._valor = valor

    def operacion(self) -> float:
        return self._valor

    def __str__(self):
        return f"Valor actual: {self.operacion()}"

class DecoradorNumero(Numero):
    """
    Decorador base para operaciones sobre Numero.
    """
    def __init__(self, componente: Numero):
        self._componente = componente

    def operacion(self) -> float:
        return self._componente.operacion()

class SumarDos(DecoradorNumero):
    def operacion(self) -> float:
        return self._componente.operacion() + 2

class MultiplicarPorDos(DecoradorNumero):
    def operacion(self) -> float:
        return self._componente.operacion() * 2

class DividirPorTres(DecoradorNumero):
    def operacion(self) -> float:
        return self._componente.operacion() / 3

if __name__ == "__main__":
    numero = Numero(9)
    print("Sin decoradores:")
    print(numero)

    print("\nSumar 2:")
    suma = SumarDos(numero)
    print(f"Valor: {suma.operacion()}")

    print("\nMultiplicar por 2:")
    mult = MultiplicarPorDos(numero)
    print(f"Valor: {mult.operacion()}")

    print("\nDividir por 3:")
    div = DividirPorTres(numero)
    print(f"Valor: {div.operacion()}")

    print("\nOperaciones anidadas (Sumar 2, luego multiplicar por 2, luego dividir por 3):")
    anidado = DividirPorTres(MultiplicarPorDos(SumarDos(numero)))
    print(f"Valor: {anidado.operacion()}")