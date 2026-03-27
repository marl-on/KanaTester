import os
import subprocess
import sys
from pathlib import Path

RECORD_FILE = Path(__file__).parent / "data" / "record.txt"


def record_options():
    print("\nHistorial: ")
    print("    1. Ver los últimos resultados.")
    print("    2. Ver todo el historial.")
    print("    3. Abrir el archivo del historial.")
    print("    4. Volver atrás")


def open_record_folder(path):
    if sys.platform == "win32":
        os.startfile(path)
    elif sys.platform == "darwin":  # Mac
        subprocess.Popen(["open", path])
    else:  # Linux
        subprocess.Popen(["xdg-open", path])


def show_record():
    while True:
        record_options()
        option = input("Escoja una opción para continuar:")

        if option == "1":
            try:
                print("\nÚltimas pruebas realizadas:")
                with open(RECORD_FILE, "r", encoding="UTF-8") as record:
                    attemps = record.readlines()
                    if attemps:
                        recent = attemps[-5] if len(attemps) >= 5 else attemps
                        for attemp in recent:
                            print("    " + attemp.strip())
                    else:
                        print("Todavía no se realizado una prueba.")
            except FileNotFoundError:
                print("\nTodavía no existe un historial de pruebas.")

        elif option == "2":
            try:
                print("\nHistorial de Pruebas:")
                with open(RECORD_FILE, "r", encoding="UTF-8") as record:
                    attemps = record.readlines()
                    if attemps:
                        for i, attemp in enumerate(attemps, start=1):
                            print(str(i) + ". " + attemp.strip())
                    else:
                        print("Todavía no se realizado una prueba.")
            except FileNotFoundError:
                print("\nTodavía no existe un historial de pruebas.")

        elif option == "3":
            open_record_folder(RECORD_FILE.parent)
        elif option == "4":
            break
        else:
            print("Opción inválida, por favor indique una de las opciones listadas.")
