"""
Este módulo proporciona una clase para calcular diferentes tipos de impuestos
sobre una base imponible.
"""

class CalculoImpuestos:
    """
    Clase para calcular impuestos como IVA, IIBB y contribuciones municipales.
    """
    def __init__(self, base_imponible):
        """
        Inicializa la clase con la base imponible.
        """
        self.base_imponible = base_imponible

    def calcular_iva(self):
        """
        Calcula el IVA sobre la base imponible.
        """
        return self.base_imponible * 0.21

    def calcular_iibb(self):
        """
        Calcula el impuesto sobre los ingresos brutos (IIBB).
        """
        return self.base_imponible * 0.05

    def calcular_contribuciones_municipales(self):
        """
        Calcula las contribuciones municipales sobre la base imponible.
        """
        return self.base_imponible * 0.012

    def calcular_total_impuestos(self):
        """
        Calcula el total de todos los impuestos.
        """
        return (self.calcular_iva() +
                self.calcular_iibb() +
                self.calcular_contribuciones_municipales())
