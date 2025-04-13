# -*- coding: utf-8 -*-
# Este script permite interactuar con la API de OpenAI para realizar consultas a ChatGPT.
# Se utiliza la biblioteca OpenAI para realizar las solicitudes a la API y pyreadline3 para manejar el historial de comandos en la terminal.   
# Se requiere tener instalada la biblioteca OpenAI y pyreadline3 para su correcto funcionamiento.

from openai import OpenAI
import pyreadline3

# Importar la biblioteca OpenAI y pyreadline3 para el manejo de la entrada del usuario
# y el historial de comandos en la terminal.
client = OpenAI()

# Configuración de la API de OpenAI
context = [
    {"role": "system", "content": "Eres un asistente útil y amigable."}
]

# Inicializar pyreadline para el manejo del historial de comandos
rl = pyreadline3.Readline()

# Función para agregar un comando al historial
# de comandos en la terminal
def add_to_history(command):
    rl.add_history(command)

# Función para manejar la conversación con ChatGPT
# y enviar la consulta del usuario a la API
def chat_with_gpt(user_query):
    try:
        # Agregar la consulta del usuario al contexto
        context.append({"role": "user", "content": user_query})

        # Realizar la solicitud a la API de ChatGPT
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
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
    except Exception as e:
        return f"Error: {e}"

def main():
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
            exit()
    except Exception as e:
        print(f"Error: {e}")
        exit()

if __name__ == "__main__":
    while True:
        main()
