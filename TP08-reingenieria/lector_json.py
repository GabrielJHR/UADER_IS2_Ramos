"""LectorJSON: Clase Singleton para leer un archivo JSON y obtener el 
valor de una clave específica."""

import json
import os

class LectorJSON:
    """
    Clase Singleton para leer un archivo JSON y obtener el valor de una clave específica.
    """
    _instance = None

    def __new__(cls):
        """
        Método para asegurar que solo se crea una instancia de LectorJSON (Singleton).
        """
        if cls._instance is None:
            cls._instance = super(LectorJSON, cls).__new__(cls)
        return cls._instance

    def get_token(self, jsonfile, json_key='token1'):
        """
        Obtiene el valor de una clave específica de un archivo JSON.
        """
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

        if json_key not in obj:
            print(f"Error: La clave '{json_key}' no existe en el archivo JSON.")
            return None
        return str(obj[json_key])
