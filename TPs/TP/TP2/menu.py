from contar_palabras_por_contacto import contar_palabras_por_contacto
from generate_messages import generate_messages 

def es_ruta_valida(ruta:str)-> bool:

    try:
        with open(ruta):
            print("Se ha ingresado a su ruta correctamente.")
            return True

    except FileNotFoundError:
            print("\nLa ruta ingresada es invalida. Intente nuevamente.\n")
            return False

def seleccionar_ruta():

    while True:
        """ ruta = input("Ingrese la ruta de su archivo: ") """
        ruta = "./chats-de-android/Chat de Android de Friends.txt"
        if es_ruta_valida(ruta): return ruta

def es_opcion_valida(seleccion:str, opciones:tuple)-> bool:

    return seleccion.isdecimal() and int(seleccion) in range(1, len(opciones)+1)


def seleccionar_opcion():


    option_titles = (
    "1. A partir de una serie de palabras, contar las veces que cada contacto dijo cada palabra, y guardar los resultados en un .csv",
    "2. A partir de un contacto, generar un mensaje pseudo-aleatorio", 
    "3. Salir del programa"
    )

    while True:
        print("Seleccione que le gustaría hacer: \n")

        for opt in option_titles:
            print(f"\t{opt}") 

        option_selected = input("\nOpción (1,2,3): ") 

        if es_opcion_valida(option_selected, option_titles): return int(option_selected)
        else: print("Opción Invalida. Intente nuevamente. \n")


def menu():

    print("Bienvenid@!.")
    ruta = seleccionar_ruta()
    option = seleccionar_opcion()

    if option == 1:
        contar_palabras_por_contacto(ruta) 
    elif option == 2:
        generate_messages(ruta)
    else:
        return



