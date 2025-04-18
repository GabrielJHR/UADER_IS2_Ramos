from __future__ import annotations
from abc import ABC, abstractmethod
from calculo_de_impuestos import CalculoImpuestosBuilder

# Producto abstracto
class Factura(ABC):
    def __init__(self, importe: float):
        self.importe = importe

    @abstractmethod
    def mostrar(self) -> None:
        pass

# Productos concretos
class FacturaIVAResponsable(Factura):
    def mostrar(self) -> None:
        print("Factura IVA Responsable")
        builder = CalculoImpuestosBuilder(self.importe)
        builder.calcular_iva()
        builder.calcular_iibb()
        builder.calcular_contribuciones()
        producto = builder.product
        
        print(f"Base no imponible: {self.importe:.2f}")
        producto.listar_impuestos()
        print("-----------------------")
        print(f"Total de impuestos: {producto.total_impuestos():.2f}")
        print(f"Importe total (con impuestos): {self.importe + producto.total_impuestos():.2f}")

class FacturaIVANoInscripto(Factura):
    def mostrar(self) -> None:
        print("Factura IVA No Inscripto")
        builder = CalculoImpuestosBuilder(self.importe)
        builder.calcular_iibb()
        builder.calcular_contribuciones()
        producto = builder.product
        
        print(f"Base no imponible: {self.importe:.2f}")
        producto.listar_impuestos()
        print("-----------------------")
        print(f"Total de impuestos: {producto.total_impuestos():.2f}")
        print(f"Importe total (con impuestos): {self.importe + producto.total_impuestos():.2f}")

class FacturaIVAExento(Factura):
    def mostrar(self) -> None:
        print("Factura IVA Exento")
        builder = CalculoImpuestosBuilder(self.importe)
        builder.calcular_contribuciones()
        producto = builder.product
        
        print(f"Base no imponible: {self.importe:.2f}")
        producto.listar_impuestos()
        print("-----------------------")
        print(f"Total de impuestos: {producto.total_impuestos():.2f}")
        print(f"Importe total (con impuestos): {self.importe + producto.total_impuestos():.2f}")

# Creador abstracto
class FacturaCreator(ABC):
    @abstractmethod
    def factory_method(self, importe: float) -> Factura:
        pass

# Creadores concretos
class FacturaIVAResponsableCreator(FacturaCreator):
    def factory_method(self, importe: float) -> Factura:
        return FacturaIVAResponsable(importe)

class FacturaIVANoInscriptoCreator(FacturaCreator):
    def factory_method(self, importe: float) -> Factura:
        return FacturaIVANoInscripto(importe)

class FacturaIVAExentoCreator(FacturaCreator):
    def factory_method(self, importe: float) -> Factura:
        return FacturaIVAExento(importe)

# Cliente
def client_code(creator: FacturaCreator, importe: float) -> None:
    factura = creator.factory_method(importe)
    factura.mostrar()

if __name__ == "__main__":
    print("App: Factura A - IVA Responsable.")
    client_code(FacturaIVAResponsableCreator(), 1000)
    
    print("")
    client_code(FacturaIVANoInscriptoCreator(), 1000)

    print("")
    client_code(FacturaIVAExentoCreator(), 1000)