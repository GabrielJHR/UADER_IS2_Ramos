from __future__ import annotations
from abc import ABC, abstractmethod


class Lamina:
    """
    Abstracción principal del patrón Bridge.
    Representa una lámina de acero y mantiene una referencia a un objeto de la
    jerarquía de implementación (TrenLaminador). Delegará la producción de la lámina
    al tren laminador correspondiente.
    """

    def __init__(self, tren_laminador: TrenLaminador) -> None:
        self.tren_laminador = tren_laminador

    def producir(self) -> str:
        return (f"\n=== Proceso de Producción de Lámina ===\n"
                f"Tren seleccionado: {self.tren_laminador.nombre_tren()}\n"
                f"Resultado: {self.tren_laminador.producir_lamina()}\n")


class TrenLaminador(ABC):
    """
    Implementación base del patrón Bridge.
    Define la interfaz que deben seguir todos los trenes laminadores concretos.
    Permite desacoplar la abstracción (Lamina) de la implementación concreta del tren.
    """

    @abstractmethod
    def producir_lamina(self) -> str:
        pass

    @abstractmethod
    def nombre_tren(self) -> str:
        """Devuelve el nombre descriptivo del tren laminador."""
        pass


"""
Implementaciones concretas de la interfaz TrenLaminador.
Cada clase representa un tren laminador específico que produce láminas de diferente longitud.
"""


class TrenLaminador5mts(TrenLaminador):
    def nombre_tren(self) -> str:
        return "Tren Laminador de 5 metros"

    def producir_lamina(self) -> str:
        return "Lámina de 5 metros producida exitosamente."


class TrenLaminador10mts(TrenLaminador):
    def nombre_tren(self) -> str:
        return "Tren Laminador de 10 metros"

    def producir_lamina(self) -> str:
        return "Lámina de 10 metros producida exitosamente."


def client_code(laminadora: Lamina) -> None:
    """
    Código cliente que utiliza la abstracción Lamina.
    El cliente solo interactúa con la abstracción, sin importar la implementación concreta del tren laminador.
    Esto permite combinar libremente diferentes tipos de láminas y trenes laminadores.
    """

    print(laminadora.producir())


if __name__ == "__main__":
    """
    Ejemplo de uso: el cliente puede crear láminas y asignarles diferentes trenes laminadores.
    """

    tren_laminador = TrenLaminador5mts()
    lamina = Lamina(tren_laminador)
    client_code(lamina)

    tren_laminador = TrenLaminador10mts()
    lamina = Lamina(tren_laminador)
    client_code(lamina)