#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este script permite interactuar con la API de OpenAI para realizar consultas a ChatGPT.
Requisitos:
    - openai
    - pyreadline3
"""

import sys
from openai import OpenAI, APIError, APIConnectionError, RateLimitError
import pyreadline3


def initialize_client():
    """Inicializa el cliente de OpenAI, saliendo si ocurre un error."""
    try:
        return OpenAI()
    except APIError as e:
        print(f"Error de API de OpenAI al inicializar: {e}")
        sys.exit(1)


def initialize_readline():
    """Inicializa pyreadline3 para el manejo del historial de comandos.
    
    Retorna:
        Un objeto readline o None si la inicialización falla.
    """
    try:
        return pyreadline3.Readline()
    except Exception as e:
        print(f"Advertencia: No se pudo inicializar pyreadline3. El historial de comandos podría no funcionar: {e}")
        return None


# Inicialización del cliente y del historial de comandos.
client = initialize_client()
readline_obj = initialize_readline()

# Contexto inicial de la conversación con ChatGPT.
conversation_context = [
    {"role": "system", "content": "Eres un asistente útil y amigable."}
]


def add_to_history(command, rl_object):
    """Agrega un comando al historial, si es posible."""
    if rl_object is not None:
        try:
            rl_object.add_history(command)
        except Exception as e:
            print(f"Advertencia: No se pudo agregar al historial: {e}")


def chat_with_gpt(query, context):
    """Envía la consulta a la API de OpenAI y retorna la respuesta del asistente.
    
    Args:
        query (str): Consulta del usuario.
        context (list): Contexto de la conversación.
        
    Returns:
        str: Respuesta del asistente o un mensaje de error.
    """
    try:
        # Agregar la consulta del usuario al contexto
        context.append({"role": "user", "content": query})
        
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=context,
            temperature=1,
            max_tokens=16384,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        # Extraer y agregar la respuesta del asistente al contexto
        answer = response.choices[0].message.content
        context.append({"role": "assistant", "content": answer})
        return answer

    except (APIError, APIConnectionError, RateLimitError) as e:
        return f"Error de API de OpenAI: {e}"
    except Exception as e:
        return f"Error inesperado en chat_with_gpt: {e}"


def prompt_user():
    """Solicita la consulta del usuario y maneja la salida limpia en caso de errores."""
    try:
        user_input = input("You: ").strip()
        if not user_input:
            print("\nChatGPT: Bye!")
            sys.exit(0)
        return user_input
    except (KeyboardInterrupt, EOFError):
        print("\nChatGPT: Bye!")
        sys.exit(0)
    except Exception as e:
        print(f"Error inesperado al leer entrada: {e}")
        sys.exit(1)


def main_loop():
    """Bucle principal para interactuar continuamente con el usuario."""
    while True:
        user_query = prompt_user()
        add_to_history(user_query, readline_obj)
        response = chat_with_gpt(user_query, conversation_context)
        print(f"\nChatGPT: {response}\n")


if __name__ == "__main__":
    main_loop()
