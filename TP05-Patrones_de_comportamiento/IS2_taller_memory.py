import os
#*--------------------------------------------------------------------
#* Design pattern memento, ejemplo
#*-------------------------------------------------------------------
class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content

class FileWriterCaretaker:
    def __init__(self):
        self.mementos = []

    def save(self, writer):
        if len(self.mementos) == 4:
            self.mementos.pop(0)
        self.mementos.append(writer.save())

    def undo(self, writer, idx=0):
        if not self.mementos:
            print("No hay estados guardados.")
            return
        if idx < 0 or idx >= len(self.mementos):
            print("Índice fuera de rango.")
            return
        writer.undo(self.mementos[-(idx+1)])

if __name__ == '__main__':

    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional III")
    writer.write("Material adicional de la clase de patrones III\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional IV (no se guarda para probar límite)")
    writer.write("Material adicional de la clase de patrones IV\n")
    print(writer.content + "\n\n")

    print("Recuperando el estado inmediato anterior (0)")
    caretaker.undo(writer, 0)
    print(writer.content + "\n\n")

    print("Recuperando el segundo estado anterior (1)")
    caretaker.undo(writer, 1)
    print(writer.content + "\n\n")

    print("Recuperando el tercer estado anterior (2)")
    caretaker.undo(writer, 2)
    print(writer.content + "\n\n")

    print("Recuperando el cuarto estado anterior (3)")
    caretaker.undo(writer, 3)
    print(writer.content + "\n\n")

