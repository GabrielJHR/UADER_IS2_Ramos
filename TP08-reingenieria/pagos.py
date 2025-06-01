class Pago:
    def __init__(self, numero_pedido, token, monto):
        """
        Inicializa un objeto Pago con el número de pedido, token de la cuenta y monto del pago.
        :param numero_pedido: Número del pedido asociado al pago.
        :param token: Token de la cuenta bancaria que realiza el pago.
        :param monto: Monto del pago a realizar.
        """
        self.monto = monto
        self.numero_pedido = numero_pedido
        self.token = token

    def __str__(self):
        return f"Pago de {self.monto} para el pedido {self.numero_pedido} con token {self.token}"

    def __repr__(self):
        return f"Pago(monto={self.monto}, numero_pedido={self.numero_pedido}, token={self.token})"

class HistorialDePagos:
    """
    Clase para gestionar el historial de pagos realizados.
    Permite agregar pagos y recorrerlos como un iterable.
    :param pagos: Lista de objetos Pago que representan los pagos realizados.
    :param indice: Índice para iterar sobre los pagos.
    :raises ValueError: Si se intenta agregar un objeto que no es de tipo Pago.
    """
    def __init__(self):
        self.pagos = []
        self.indice = 0

    def agregar_pago(self, pago):
        """
        Agrega un objeto Pago al historial de pagos.
        :param pago: Objeto Pago a agregar al historial.
        :raises ValueError: Si el objeto no es de tipo Pago.
        """
        if isinstance(pago, Pago):
            self.pagos.append(pago)
        else:
            raise ValueError("El pago debe ser un objeto de tipo Pago.")

    def __iter__(self):
        self.indice = 0
        return self

    def __next__(self):
        """
        Devuelve el siguiente pago en el historial.
        :return: El siguiente objeto Pago en el historial.
        :raises StopIteration: Si no hay más pagos en el historial.
        """
        if self.indice < len(self.pagos):
            pago = self.pagos[self.indice]
            self.indice += 1
            return pago
        else:
            raise StopIteration

class CuentaBancaria:
    """
    Clase para representar una cuenta bancaria con un token y un saldo.
    Permite verificar si se puede realizar un pago y realizarlo si es posible.
    :param token: Token de la cuenta bancaria.
    :param saldo: Saldo disponible en la cuenta bancaria (por defecto es 0).
    """
    def __init__(self, token, saldo=0):
        self.token = token
        self.saldo = saldo

    def puede_pagar(self, monto):
        """
        Verifica si la cuenta tiene suficiente saldo para realizar un pago.
        :param monto: Monto del pago a realizar.
        :return: True si el saldo es suficiente, False en caso contrario.
        """
        return self.saldo >= monto

    def realizar_pago(self, monto):
        """
        Realiza un pago si hay suficiente saldo en la cuenta.
        :param monto: Monto del pago a realizar.
        :return: True si el pago se realizó con éxito, False si no hay suficiente saldo."""
        if self.puede_pagar(monto):
            self.saldo -= monto
            return True
        else:
            print("Error: Saldo insuficiente.")
            return False

    def get_token(self):
        """
        Devuelve el token de la cuenta bancaria.
        :return: Token de la cuenta bancaria.
        """
        return self.token

    def get_saldo(self):
        """
        Devuelve el saldo actual de la cuenta bancaria.
        :return: Saldo de la cuenta bancaria.
        """
        return self.saldo

class GestorPagos:
    """
    Clase para gestionar los pagos automáticos utilizando múltiples cuentas bancarias.
    Permite realizar pagos en un orden cíclico entre las cuentas y mantener un historial de pagos.
    :param cuentas: Lista de objetos CuentaBancaria que representan las cuentas disponibles para realizar pagos.
    :param historial: Objeto HistorialDePagos que almacena los pagos realizados.
    :param turno: Índice de la cuenta que se utilizará para el próximo pago.
    """
    def __init__(self, cuentas):
        self.cuentas = cuentas
        self.historial = HistorialDePagos()
        self.turno = 0

    def realizar_pago(self, numero_pedido, monto):
        cuentas_len = len(self.cuentas)
        intentos = 0
        idx = self.turno
        while intentos < cuentas_len:
            cuenta = self.cuentas[idx]
            if cuenta.puede_pagar(monto):
                cuenta.realizar_pago(monto)
                pago = Pago(numero_pedido, cuenta.get_token(), monto)
                self.historial.agregar_pago(pago)
                print(f"Pago realizado: Pedido {numero_pedido}, Token {cuenta.get_token()}, Monto ${monto}")
                self.turno = (idx + 1) % cuentas_len
                return True
            idx = (idx + 1) % cuentas_len
            intentos += 1
        print(f"No se pudo realizar el pago del pedido {numero_pedido}: saldo insuficiente en todas las cuentas.")
        return False

    def listar_pagos(self):
        """
        Lista todos los pagos realizados en el historial.
        Si no hay pagos, informa al usuario.
        """
        print("Listado de pagos realizados:")
        for pago in self.historial:
            print(pago)
