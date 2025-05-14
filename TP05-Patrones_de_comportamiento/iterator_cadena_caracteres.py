from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any

class StringIterator(Iterator):
    """
    Iterador concreto que recorre una cadena de caracteres en sentido directo o reverso.
    """
    def __init__(self, collection: StringCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = len(collection) - 1 if reverse else 0

    def __next__(self) -> Any:
        if self._reverse:
            if self._position < 0:
                raise StopIteration()
            value = self._collection[self._position]
            self._position -= 1
        else:
            if self._position >= len(self._collection):
                raise StopIteration()
            value = self._collection[self._position]
            self._position += 1
        return value

class StringCollection(Iterable):
    """
    Colección concreta que almacena una cadena de caracteres y permite obtener iteradores.
    """
    def __init__(self, cadena: str = "") -> None:
        self._cadena = cadena

    def __getitem__(self, index: int) -> str:
        return self._cadena[index]

    def __len__(self) -> int:
        return len(self._cadena)

    def __iter__(self) -> StringIterator:
        return StringIterator(self)

    def get_reverse_iterator(self) -> StringIterator:
        return StringIterator(self, True)

    def set_string(self, cadena: str) -> None:
        self._cadena = cadena

if __name__ == "__main__":
    cadena = "Prueba iterador"
    collection = StringCollection(cadena)

    print("Recorrido directo:")
    for char in collection:
        print(char, end=" ")
    print("\n")

    print("Recorrido reverso:")
    for char in collection.get_reverse_iterator():
        print(char, end=" ")
    print()