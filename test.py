import random
from datetime import datetime
from pathlib import Path

from char import hiragana

# Crear la carpeta del historial si no existe
RECORD_FOLDER = Path(__file__).parent / "data"

# Si existe, ignorar la creación
RECORD_FOLDER.mkdir(exist_ok=True)

# Directorio del archivo de historial
RECORD_FILE = Path(__file__).parent / "data" / "record.txt"

# Obtener fecha
now = datetime.now()
date = now.date()

# print(f"Fecha: {fecha} Hora: {hora.hour}:{hora.minute}")


def start_test():
    # Obtener número de preguntas
    num = input("\nNúmero de carácteres a evaluar (Max:46): ")
    num = int(num)
    i = num

    # Definir variable de respuestas correctas
    correctAnswers = 0

    # Definir lista de prefuntas desde la tupla de Hiragana
    quiz = random.sample(list(hiragana), num)

    # Bucle de la prueba, repitiendo cada pregunta
    while i > 0:
        print("---------------")
        print(f"{i}/{num}:")

        # Obtener primera pregunta de la prueba(quiz)
        response = random.sample(quiz, 1)

        # Imprimir el Hiragana a adivinar
        print(f"    Hiragana: {response[0][1]}")

        # Obtener respuesta del usuario
        respuesta = input("    Respuesta: ")

        # Verificar respuesta
        if respuesta == response[0][0]:
            print("    Correcto")
            correctAnswers += 1
        else:
            print("    Incorrecto")
        quiz.remove(response[0])
        i -= 1

    # Resultado
    print("---------------")
    time = now.time()

    calification = round(((correctAnswers / num) * 100), 2)
    print(
        f"Resultado: {calification}% | Respuestas correctas: {correctAnswers} / {num}"
    )

    with open(RECORD_FILE, "a", encoding="utf-8") as record:
        record.write(
            str(date)
            + " - "
            + str(time.hour)
            + ":"
            + str(time.minute)
            + " | Resultados: "
            + str(calification)
            + "% "
            + "- Preguntas: "
            + str(num)
            + "\n"
        )
