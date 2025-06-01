# -------------------------------------------------------------------------------------------------
# getJason.py
# Copyright UADERFCyT-IS2©2024 todos los derechos reservados.
#
# Descripción:
#   Automatiza pagos entre cuentas bancarias usando información de sitedata.json.
# -------------------------------------------------------------------------------------------------

import sys
from pagos import GestorPagos, CuentaBancaria
from lector_json import LectorJSON

VERSION = "1.2"

def crear_cuentas_desde_json(jsonfile, claves):
    """
    Crea una lista de cuentas bancarias a partir de un archivo JSON y claves específicas.
    """
    lector = LectorJSON()
    cuentas = []
    saldos = {"token1": 1000, "token2": 2000}
    for clave in claves:
        valor_token = lector.get_token(jsonfile, clave)
        if valor_token is not None:
            cuentas.append(CuentaBancaria(valor_token, saldos.get(clave, 0)))
    return cuentas

def main():
    """
    Función principal que ejecuta el script.
    Si se pasa el argumento "-v", muestra la versión del script y termina.
    Si no, crea cuentas bancarias desde el archivo JSON y realiza pagos.
    Luego lista los pagos realizados.
    """
    print("="*50)
    print(" Automatización de Pagos Bancarios ".center(50, "="))
    print("="*50)

    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print(f"getJason.py versión {VERSION}")
        sys.exit(0)

    print("Creando cuentas bancarias desde 'sitedata.json'...")
    claves = ["token1", "token2"]
    cuentas = crear_cuentas_desde_json("sitedata.json", claves)
    if not cuentas:
        print("No se pudieron crear cuentas. Verifique el archivo JSON.")
        sys.exit(1)

    gestor = GestorPagos(cuentas)
    print("Procesando pagos automáticos...\n")
    for pedido in range(1, 11):
        exito = gestor.realizar_pago(pedido, 500)
        if not exito:
            print(f"Pedido {pedido}: No se pudo realizar el pago por saldo insuficiente en todas las cuentas.")

    print("\n" + "-"*50)
    print("Listado de pagos realizados:")
    print("-"*50)
    gestor.listar_pagos()
    print("="*50)
    print(" Fin de la ejecución ".center(50, "="))
    print("="*50)

if __name__ == "__main__":
    """
    Punto de entrada del script.
    Si se ejecuta directamente, llama a la función main().
    """
    main()

    def listar_pagos(self):
        if not self.historial.pagos:
            print("No se han realizado pagos.")
            return
        print(f"{'Pedido':<10}{'Token':<10}{'Monto':<10}")
        print("-"*30)
        for pago in self.historial:
            print(f"{pago.numero_pedido:<10}{pago.token:<10}${pago.monto:<10}")
