import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def iniciar_tutor():
    print("--- 🧠 AI English Tutor (Nivel A1-C1) ---")
    print("Escribe 'exit' para terminar.\n")

    contexto = (
        "Eres un tutor de inglés experto. Tu misión es ayudar al usuario a alcanzar el nivel C1. "
        "Si el usuario comete un error, corrígelo amablemente y explica la regla gramatical. "
        "Usa un tono motivador y, al final de cada respuesta, enseña una palabra o frase de nivel avanzado."
    )

    mensajes = [{"role": "system", "content": contexto}]

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == 'exit': break

        mensajes.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=mensajes
        )

        respuesta = response.choices[0].message.content
        print(f"\nTutor: {respuesta}\n")
        mensajes.append({"role": "assistant", "content": respuesta})

if __name__ == "__main__":
    iniciar_tutor()