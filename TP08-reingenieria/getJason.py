# -------------------------------------------------------------------------------------------------
# getJason.py
# Copyright UADERFCyT-IS2©2024 todos los derechos reservados.
#
# Descripción:
#   Este script permite leer un archivo JSON y mostrar en pantalla el valor asociado a una clave
#   específica (por defecto 'token1'). Se puede especificar la clave como segundo argumento al
#   ejecutar el script.
#
# Uso:
#   python getJason.py archivo.json [clave]
#
# Notas:
#   - Incluye una versión refactorizada con control de errores y una clase Singleton.
#   - Si NUEVO_CODIGO es True, se ejecuta la versión mejorada.
# -------------------------------------------------------------------------------------------------

import json  # Importa el módulo para trabajar con archivos JSON
import sys   # Importa el módulo para acceder a argumentos de línea de comandos
import os    # Importa el módulo para operaciones del sistema operativo

VERSION = "1.1"  # Versión del programa

class LectorJSON:
    """
    Clase Singleton para leer un archivo JSON y obtener el valor de una clave específica.
    """
    _instance = None  # Variable de clase para almacenar la instancia única

    def __new__(cls):
        # Implementación del patrón Singleton
        if cls._instance is None:
            cls._instance = super(LectorJSON, cls).__new__(cls)
        return cls._instance

    def get_token(self, jsonfile, JSON_KEY='token1'):
        """
        Lee el archivo JSON y devuelve el valor asociado a la clave especificada.
        Maneja errores de archivo inexistente, formato inválido y clave no encontrada.
        """
        if not os.path.isfile(jsonfile):
            print(f"Error: El archivo '{jsonfile}' no existe.")
            return None
        try:
            with open(jsonfile, 'r', encoding="utf-8") as myfile:
                data = myfile.read()  # Lee el contenido del archivo
            obj = json.loads(data)   # Parsea el contenido como JSON
        except json.JSONDecodeError:
            print(f"Error: El archivo '{jsonfile}' no es un JSON válido.")
            return None
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None

        if JSON_KEY not in obj:
            print(f"Error: La clave '{JSON_KEY}' no existe en el archivo JSON.")
            return None
        return str(obj[JSON_KEY])  # Devuelve el valor de la clave como string

def main():
    # Si el argumento es "-v", mostrar la versión y salir
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        print(f"getJason.py versión {VERSION}")
        sys.exit(0)

    # Verifica la cantidad de argumentos recibidos
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Error: Número incorrecto de argumentos.")
        print("Uso: python getJason.py archivo.json [clave]")
        sys.exit(1)  # Termina con código de error

    jsonfile = sys.argv[1]  # Primer argumento: nombre del archivo JSON

    # Validación adicional: el archivo debe tener extensión .json
    if not jsonfile.lower().endswith('.json'):
        print("Error: El archivo debe tener extensión .json")
        sys.exit(1)

    JSON_KEY = sys.argv[2] if len(sys.argv) == 3 else "token1"  # Segundo argumento opcional: clave

    # Validación adicional: la clave no debe estar vacía
    if not JSON_KEY or not isinstance(JSON_KEY, str):
        print("Error: La clave debe ser un string no vacío.")
        sys.exit(1)

    lector = LectorJSON()  # Crea una instancia de LectorJSON
    token = lector.get_token(jsonfile, JSON_KEY)  # Obtiene el valor de la clave
    if token is not None:
        print(token)  # Imprime el valor si no hubo errores
    else:
        sys.exit(1)  # Si hubo error, termina con código de error
    
if __name__ == "__main__":
    main()  # Llama a la función principal al ejecutar el script