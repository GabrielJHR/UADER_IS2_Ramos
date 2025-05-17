from abc import ABC, abstractmethod

class Ping(ABC):

    """
    Interfaz Ping que declara operaciones comunes para realizar pings,
    tanto controlados como libres, a una dirección IP.
    """

    @abstractmethod

    def execute(self, ip: str) -> None:
        pass


    def execute_free(self, ip: str) -> None:
        pass


class RealPing(Ping):
    """
    Implementación concreta de Ping que realiza la lógica real de los pings.
    """

    def execute(self, ip: str) -> None:

        if ip.startswith("192."):
            print(f"RealPing: ejecutando ping real a la direccion {ip}")

        else:
            print(f"No se puede ejecutar ping real a la direccion {ip}")



    def execute_free(self, ip: str) -> None:
        print(f"RealPing: ejecutando ping libre a la direccion {ip}")





class ProxyPing(Ping):

    """
    Proxy para la clase RealPing. Controla el acceso y modifica la IP en el caso de que sea 192.168.0.254 la cambia por la ip de google.
    """

    def __init__(self, real_subject: RealPing) -> None:
        self._real_subject = real_subject


    def execute(self, ip: str) -> None:
        """
        El proxy puede realizar acciones adicionales antes de delegar la ejecución al objeto real.
        """

        if ip == "192.168.0.254":
            print("Proxy: cambiando la ip a 8.8.8.8")
            ip = "8.8.8.8"

        
        if ip.startswith("192."):
            self._real_subject.execute(ip)
        else:
            self._real_subject.execute_free(ip)


def client_code(subject: Ping) -> None:
    """
    El cliente debe trabajar con todos los objetos (ambos sujetos y proxies) a través de la interfaz Ping 
    para soportar tanto los sujetos reales como los proxies. En la vida real, sin embargo, 
    los clientes generalmente trabajan con sus sujetos reales directamente. 
    En este caso, para implementar el patrón de manera más fácil, puedes extender tu proxy de la clase del sujeto real.

    """

    subject.execute("192.168.0.254")


if __name__ == "__main__":

    print("Client: Ejecutando el codigo del cliente con un real subject:")
    real_subject = RealPing()
    client_code(real_subject)

    print("")


    print("Client: Ejecutando el codigo del cliente con un proxy:")
    proxy = ProxyPing(real_subject)
    client_code(proxy)