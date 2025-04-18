from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

class Builder(ABC):
    """
    Interfaz Builder para crear partes del producto (impuestos).
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def calcular_iva(self) -> None:
        pass

    @abstractmethod
    def calcular_iibb(self) -> None:
        pass

    @abstractmethod
    def calcular_contribuciones(self) -> None:
        pass

class CalculoImpuestosBuilder(Builder):
    """
    Builder concreto para calcular impuestos.
    """

    def __init__(self, base_imponible: float) -> None:
        self.base_imponible = base_imponible
        self.reset()

    def reset(self) -> None:
        self._product = CalculoImpuestosProduct(self.base_imponible)

    @property
    def product(self) -> 'CalculoImpuestosProduct':
        product = self._product
        self.reset()
        return product

    def calcular_iva(self) -> None:
        self._product.add_impuesto('IVA', self.base_imponible * 0.21)

    def calcular_iibb(self) -> None:
        self._product.add_impuesto('IIBB', self.base_imponible * 0.05)

    def calcular_contribuciones(self) -> None:
        self._product.add_impuesto('Contribuciones Municipales', self.base_imponible * 0.012)

class CalculoImpuestosProduct:
    """
    Producto final: contiene los impuestos calculados.
    """

    def __init__(self, base_imponible: float) -> None:
        self.base_imponible = base_imponible
        self.impuestos = {}

    def add_impuesto(self, nombre: str, valor: float) -> None:
        self.impuestos[nombre] = valor

    def total_impuestos(self) -> float:
        return sum(self.impuestos.values())

    def listar_impuestos(self) -> None:
        for nombre, valor in self.impuestos.items():
            print(f"{nombre}: {valor:.2f}")
