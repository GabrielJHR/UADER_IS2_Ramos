import os
#*--------------------------------------------------------------------
#* Ejemplo de design pattern de tipo state
#*--------------------------------------------------------------------
"""State class: Base State class"""
class State:

    def scan(self):
        self.pos += 1
        total = len(self.stations) + len(self.memories)
        if self.pos == total:
            self.pos = 0
        if self.pos < len(self.stations):
            print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))
        else:
            mem_idx = self.pos - len(self.stations)
            mem_label, mem_freq = self.memories[mem_idx]
            print("Sintonizando... Memoria {}: {} {}".format(mem_label, mem_freq, self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        # Memorias: lista de tuplas (etiqueta, frecuencia)
        self.memories = [("M1", "1250"), ("M2", "1380"), ("M3", "1510"), ("M4", "1390")]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
class FmState(State):

    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.memories = [("M1", "89.1"), ("M2", "103.9"), ("M3", "99.5"), ("M4", "101.1")]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:

    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()

#*---------------------

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 7 + [radio.toggle_amfm] + [radio.scan] * 7
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()

