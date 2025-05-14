from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List
import random
import string

class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self, emitted_id: str) -> None:
        pass

class ConcreteSubject(Subject):
    def __init__(self) -> None:
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self, emitted_id: str) -> None:
        print(f"Subject: Emitting ID {emitted_id}")
        for observer in self._observers:
            observer.update(emitted_id)

    def emit_id(self, emitted_id: str) -> None:
        self.notify(emitted_id)

class Observer(ABC):
    @abstractmethod
    def update(self, emitted_id: str) -> None:
        pass

class ObserverAlpha(Observer):
    def __init__(self):
        self.my_id = "A1B2"
    def update(self, emitted_id: str) -> None:
        if emitted_id == self.my_id:
            print(f"ObserverAlpha: Mi ID {self.my_id} fue emitido!")

class ObserverBeta(Observer):
    def __init__(self):
        self.my_id = "C3D4"
    def update(self, emitted_id: str) -> None:
        if emitted_id == self.my_id:
            print(f"ObserverBeta: Mi ID {self.my_id} fue emitido!")

class ObserverGamma(Observer):
    def __init__(self):
        self.my_id = "E5F6"
    def update(self, emitted_id: str) -> None:
        if emitted_id == self.my_id:
            print(f"ObserverGamma: Mi ID {self.my_id} fue emitido!")

class ObserverDelta(Observer):
    def __init__(self):
        self.my_id = "G7H8"
    def update(self, emitted_id: str) -> None:
        if emitted_id == self.my_id:
            print(f"ObserverDelta: Mi ID {self.my_id} fue emitido!")

if __name__ == "__main__":
    subject = ConcreteSubject()
    observers = [ObserverAlpha(), ObserverBeta(), ObserverGamma(), ObserverDelta()]
    for obs in observers:
        subject.attach(obs)

    # IDs de los observers
    observer_ids = [obs.my_id for obs in observers]
    
    print("Emitiendo IDs:")
    ids_to_emit = observer_ids.copy()
    while len(ids_to_emit) < 8:
        random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        if random_id not in ids_to_emit:
            ids_to_emit.append(random_id)
    random.shuffle(ids_to_emit)

    for eid in ids_to_emit:
        subject.emit_id(eid)