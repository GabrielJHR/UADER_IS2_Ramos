import json
import sys

# Control de branch para evitar conflictos con el código antiguo
NUEVO_CODIGO = False

class LectorJSON:
    """
    Clase Singleton para leer un archivo JSON y obtener el valor de una clave específica.
    """
    _instance = None

    def __new__(cls, jsonfile, jsonkey='token1'):
        if cls._instance is None:
            cls._instance = super(LectorJSON, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, jsonfile, jsonkey='token1'):
        if self._initialized:
            return
        self.jsonfile = jsonfile
        self.jsonkey = jsonkey
        self._initialized = True

    def get_token(self):
        """
        Lee el archivo JSON y devuelve el valor asociado a la clave especificada.
        """
        with open(self.jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        return str(obj[self.jsonkey])
    
if NUEVO_CODIGO:
    # Si se está ejecutando el nuevo código, se crea una instancia de LectorJSON
    if len(sys.argv) == 3:
        lector = LectorJSON(sys.argv[1], sys.argv[2])
    else:
        lector = LectorJSON(sys.argv[1])
    
    print("Nuevo código en ejecución")
    print(lector.get_token())
    sys.exit(0)
    


"""-------------------------------------------------- Programa original ----------------------------------------------------"""

"""
Recuperacion del codigo fuente de getJason.pyc

Este script lee un archivo JSON y muestra en pantalla el valor asociado a una clave específica (por defecto 'token1').
Se puede especificar la clave como segundo argumento al ejecutar el script.
Uso:
    python getJason.py archivo.json [clave]
"""
# Las librerias se importan al principio del archivo
# import json
# import sys
jsonfile = sys.argv[1]

# Modificacion para que tome dos argumentos y se pueda cambiar el token
if len(sys.argv) == 3:
    jsonkey = sys.argv[2]
else:
    jsonkey = "token1"

# Codigo antiguo
# jsonkey = "token1"

with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)
print(str(obj[jsonkey]))
