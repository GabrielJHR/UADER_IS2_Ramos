from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request: int) -> Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler: Optional[Handler] = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def handle(self, request: int) -> Optional[str]:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class ParHandler(AbstractHandler):
    def handle(self, request: int) -> Optional[str]:
        if request % 2 == 0:
            return f"ParHandler: Consumí el número par {request}"
        else:
            return super().handle(request)

def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

class PrimoHandler(AbstractHandler):
    def handle(self, request: int) -> Optional[str]:
        if es_primo(request):
            return f"PrimoHandler: Consumí el número primo {request}"
        else:
            return super().handle(request)

def client_code(handler: Handler) -> None:
    for numero in range(1, 101):
        resultado = handler.handle(numero)
        if resultado:
            print(resultado)
        else:
            print(f"Ningún handler consumió el número {numero}")

if __name__ == "__main__":
    par_handler = ParHandler()
    primo_handler = PrimoHandler()
    par_handler.set_next(primo_handler)

    print("Cadena: ParHandler > PrimoHandler\n")
    client_code(par_handler)