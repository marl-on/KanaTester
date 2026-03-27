from menu import show_options
from record import show_record
from table import show_table
from test import start_test

# Opciones principales


def main():
    while True:
        show_options()
        option = input("Escoja una opción para continuar: ")

        if option == "1":
            start_test()
        elif option == "2":
            show_table()
        elif option == "3":
            show_record()
        elif option == "4":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, por favor indique una de las opciones listadas.")


if __name__ == "__main__":
    main()
