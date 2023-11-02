from contar_palabras_por_contacto import contar_palabras_por_contacto
from generar_mensajes import generar_mensaje

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
        ruta = input("Ingrese la ruta de su archivo: ")
        if es_ruta_valida(ruta): return ruta

def es_opcion_valida(seleccion:str, opciones:tuple)-> bool:
    """
    Dado que el menú espera que se escoja un índice para las opciones dispuestas, se define una opción valida como un número dentro del rango de opciones.
    """
    return seleccion.isdecimal() and int(seleccion) in range(1, len(opciones)+1)


def seleccionar_opcion():
    opciones = (
    "1. A partir de una serie de palabras, contar las veces que cada contacto dijo cada palabra, y guardar los resultados en un .csv",
    "2. A partir de un contacto, generar un mensaje pseudo-aleatorio", 
    "3. Salir del programa"
    )

    while True:
        print("Seleccione que le gustaría hacer: \n")

        for opcion in opciones:
            print(f"\t{opcion}") 

        opcion_seleccionada = input("\nOpción (1,2,3): ") 

        if es_opcion_valida(opcion_seleccionada, opciones): 
            return int(opcion_seleccionada)
        else: print("Opción Invalida. Intente nuevamente. \n")

def main():
    print("Bienvenid@!.")
    ruta = seleccionar_ruta()
    opcion = seleccionar_opcion()

    if opcion == 1:
        contar_palabras_por_contacto(ruta) 
        print("Reporte generado!")
    elif opcion == 2:
        print(f"\n{generar_mensaje(ruta)}")
    else:
        return

main()



