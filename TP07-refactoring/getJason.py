import json
import sys
import os

# Control de branch para evitar conflictos con el código antiguo
NUEVO_CODIGO = True

class LectorJSON:
    """
    Clase Singleton para leer un archivo JSON y obtener el valor de una clave específica.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LectorJSON, cls).__new__(cls)
        return cls._instance

    def get_token(self, jsonfile, jsonkey='token1'):
        """
        Lee el archivo JSON y devuelve el valor asociado a la clave especificada.
        """
        if not os.path.isfile(jsonfile):
            print(f"Error: El archivo '{jsonfile}' no existe.")
            return None
        try:
            with open(jsonfile, 'r') as myfile:
                data = myfile.read()
            obj = json.loads(data)
        except json.JSONDecodeError:
            print(f"Error: El archivo '{jsonfile}' no es un JSON válido.")
            return None
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None

        if jsonkey not in obj:
            print(f"Error: La clave '{jsonkey}' no existe en el archivo JSON.")
            return None
        return str(obj[jsonkey])

if NUEVO_CODIGO:
    # Si se está ejecutando el nuevo código, se crea una instancia de LectorJSON
    print("Nuevo código en ejecución")
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Uso: python getJason.py archivo.json [clave]")
        sys.exit(0)

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2] if len(sys.argv) == 3 else "token1"

    lector = LectorJSON()
    token = lector.get_token(jsonfile, jsonkey)
    if token is not None:
        print(token)
        # Si hubo error, ya se mostró el mensaje y termina normalmente
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
