from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

"""
Este ejemplo implementa el patrón Builder para la construcción de aviones.
Un avión está compuesto por un cuerpo ("body"), dos alas, dos turbinas y un tren de aterrizaje.
El objetivo es separar la construcción de un objeto complejo (Avion) de su representación,
permitiendo construir diferentes configuraciones paso a paso.
"""

class Builder(ABC):
    """
    La interfaz Builder especifica los métodos para crear las diferentes partes
    que componen un avión.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_body(self) -> None:
        pass

    @abstractmethod
    def produce_ala(self) -> None:
        pass

    @abstractmethod
    def produce_tren_aterrizaje(self) -> None:
        pass

    @abstractmethod
    def produce_turbina(self) -> None:
        pass


class ConcreteBuilderAvion(Builder):
    """
    El ConcreteBuilderAvion implementa los pasos definidos en la interfaz Builder
    para construir un avión específico. Cada método agrega una parte al avión.
    """

    def __init__(self) -> None:
        """
        Al crear una nueva instancia del builder, se inicializa un avión vacío.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Avion()

    @property
    def product(self) -> Avion:
        """
        Devuelve el avión construido y reinicia el builder para permitir la construcción
        de un nuevo avión si es necesario.
        """
        product = self._product
        self.reset()
        return product

    def produce_body(self) -> None:
        self._product.add("Body")

    def produce_ala(self) -> None:
        self._product.add("Ala")

    def produce_tren_aterrizaje(self) -> None:
        self._product.add("Tren de aterrizaje")
    
    def produce_turbina(self) -> None:
        self._product.add("Turbina")


class Avion():
    """
    La clase Avion representa el producto final que se está construyendo.
    Permite agregar partes y mostrar la lista de componentes del avión.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Partes del avión: {', '.join(self.parts)}", end="")


class Director:
    """
    El Director define el orden en que se deben ejecutar los pasos de construcción
    para crear una configuración específica de avión.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        Permite asignar un builder concreto al director para construir el avión.
        """
        self._builder = builder

    """
    El Director puede definir diferentes métodos para construir distintas variantes de aviones.
    """

    def build_avion_basico(self) -> None:
        self.builder.produce_body()
        self.builder.produce_ala()
        self.builder.produce_ala()
        self.builder.produce_tren_aterrizaje()
        self.builder.produce_turbina()
        self.builder.produce_turbina()


if __name__ == "__main__":
    """
    Código cliente: crea un builder, lo asigna al director y construye un avión básico.
    Finalmente, muestra las partes del avión construido.
    """

    director = Director()
    builder = ConcreteBuilderAvion()
    director.builder = builder

    print("Construyendo un avión básico...")
    director.build_avion_basico()
    print("El avión básico fue construido, sus partes son:")
    builder.product.list_parts()