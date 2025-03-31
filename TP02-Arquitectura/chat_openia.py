from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-4o-mini-2024-07-18",
    input="Escribe una reseña del señor de los anillos"
)

print(response.output_text)
