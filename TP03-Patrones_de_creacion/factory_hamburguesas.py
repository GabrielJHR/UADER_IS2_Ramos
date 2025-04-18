from __future__ import annotations
from abc import ABC, abstractmethod

# Producto abstracto
class Hamburguesa(ABC):
    @abstractmethod
    def entregar(self) -> str:
        pass

# Productos concretos
class HamburguesaMostrador(Hamburguesa):
    def entregar(self) -> str:
        return "Hamburguesa entregada en mostrador."

class HamburguesaRetiro(Hamburguesa):
    def entregar(self) -> str:
        return "Hamburguesa retirada por el cliente."

class HamburguesaDelivery(Hamburguesa):
    def entregar(self) -> str:
        return "Hamburguesa enviada por delivery."

# Creador abstracto
class HamburguesaCreator(ABC):
    @abstractmethod
    def crear_hamburguesa(self) -> Hamburguesa:
        pass

    def entregar_hamburguesa(self) -> str:
        hamburguesa = self.crear_hamburguesa()
        return hamburguesa.entregar()

# Creadores concretos
class MostradorCreator(HamburguesaCreator):
    def crear_hamburguesa(self) -> Hamburguesa:
        return HamburguesaMostrador()

class RetiroCreator(HamburguesaCreator):
    def crear_hamburguesa(self) -> Hamburguesa:
        return HamburguesaRetiro()

class DeliveryCreator(HamburguesaCreator):
    def crear_hamburguesa(self) -> Hamburguesa:
        return HamburguesaDelivery()

# Cliente
def client_code(creator: HamburguesaCreator):
    print(creator.entregar_hamburguesa())

if __name__ == "__main__":
    print("App: Hamburguesa por mostrador.")
    client_code(MostradorCreator())
    print("App: Hamburguesa retirada por cliente.")
    client_code(RetiroCreator())
    print("App: Hamburguesa por delivery.")
    client_code(DeliveryCreator())