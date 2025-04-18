# -*- coding: utf-8 -*-
"""Este script permite interactuar con la API de OpenAI para realizar consultas a ChatGPT.
Se utiliza la biblioteca OpenAI para realizar las solicitudes a la API y pyreadline3 para
manejar el historial de comandos en la terminal.
Se requiere tener instalada la biblioteca OpenAI y pyreadline3 para su correcto funcionamiento."""

import sys # Importar sys para usar sys.exit()
from openai import OpenAI, APIError, APIConnectionError, RateLimitError
import pyreadline3


# Importar la biblioteca OpenAI y pyreadline3 para el manejo de la entrada del usuario
# y el historial de comandos en la terminal.
try:
    client = OpenAI()
except APIError as e:
    print(f"Error de API de OpenAI al inicializar: {e}")
    sys.exit(1) # Salir si no se puede inicializar el cliente

# Configuración de la API de OpenAI
context = [
    {"role": "system", "content": "Eres un asistente útil y amigable."}
]

# Inicializar pyreadline para el manejo del historial de comandos
rl = pyreadline3.Readline()

# Función para agregar un comando al historial
# de comandos en la terminal
def add_to_history(command):
    """Agrega un comando al historial de comandos."""
    rl.add_history(command)

# Función para manejar la conversación con ChatGPT
# y enviar la consulta del usuario a la API
def chat_with_gpt(user_query):
    """Maneja la conversación con ChatGPT y envía la consulta a la API."""
    try:
        # Agregar la consulta del usuario al contexto
        context.append({"role": "user", "content": user_query})

        # Realizar la solicitud a la API de ChatGPT
        response = client.chat.completions.create(
            model="gpt-4.1-mini-2025-04-14",
            messages=context,
            temperature=1,
            max_tokens=16384,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Agregar la respuesta de ChatGPT al contexto
        context.append({"role": "assistant", "content": response.choices[0].message.content})

        # Devolver la respuesta de ChatGPT
        return response.choices[0].message.content
    # Capturar excepciones específicas de la API de OpenAI
    except (APIError, APIConnectionError, RateLimitError) as e:
        return f"Error de API de OpenAI: {e}"
    # Capturar otras excepciones generales
    except Exception as e: # Captura genérica como último recurso
        return f"Error inesperado en chat_with_gpt: {e}"

def main():
    """Función principal para interactuar con el usuario y ChatGPT."""
    try:
        # Leer la entrada del usuario con soporte para historial de comandos
        user_query = input("You: ")

        # Si el usuario no ingresa nada, salir del programa
        if user_query != "":
            add_to_history(user_query)
            response = chat_with_gpt(user_query)
            print('')
            print(f"ChatGPT: {response}")
            print('')
            print('')
        else:
            print('')
            print("ChatGPT: Bye!")
            sys.exit()
    # Capturar interrupción del teclado (Ctrl+C)
    except KeyboardInterrupt:
        print("\nChatGPT: Interrupción detectada. Bye!")
        sys.exit(0) # Usar sys.exit()
    # Capturar fin de archivo (Ctrl+D en Linux/macOS, Ctrl+Z+Enter en Windows)
    except EOFError:
        print("\nChatGPT: Bye!")
        sys.exit(0) # Usar sys.exit()
    # Capturar otras excepciones generales durante la ejecución de main
    except Exception as e: # Captura genérica como último recurso
        print(f"Error inesperado en main: {e}")
        sys.exit(1) # Salir con código de error

if __name__ == "__main__":
    while True:
        main()
