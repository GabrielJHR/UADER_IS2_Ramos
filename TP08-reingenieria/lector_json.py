import json
import os

class LectorJSON:
    """
    Clase Singleton para leer un archivo JSON y obtener el valor de una clave específica.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LectorJSON, cls).__new__(cls)
        return cls._instance

    def get_token(self, jsonfile, JSON_KEY='token1'):
        if not os.path.isfile(jsonfile):
            print(f"Error: El archivo '{jsonfile}' no existe.")
            return None
        try:
            with open(jsonfile, 'r', encoding="utf-8") as myfile:
                data = myfile.read()
            obj = json.loads(data)
        except json.JSONDecodeError:
            print(f"Error: El archivo '{jsonfile}' no es un JSON válido.")
            return None
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None

        if JSON_KEY not in obj:
            print(f"Error: La clave '{JSON_KEY}' no existe en el archivo JSON.")
            return None
        return str(obj[JSON_KEY])