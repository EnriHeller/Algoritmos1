from cuatro_en_linea import (crear_tablero, es_turno_de_x, insertar_simbolo) 

"print(crear_tablero(4,4))"

tablero_prueba = [

    [' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' '], 
    [' ', ' ', ' ', ' '], 
    ['X', ' ', ' ', ' ']

    ]
insertar_simbolo(tablero_prueba,0)

for fila in tablero_prueba:
    # Imprime cada elemento de la fila sin espacio entre ellos
    print(' '.join(fila))
    # Agrega un salto de línea después de imprimir la fila
    print()



