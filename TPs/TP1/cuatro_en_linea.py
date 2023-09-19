from typing import List


def validar_dimensiones_tablero(n_filas: int, n_columnas: int) -> None:

    assert type(n_filas) == int, "El numero de filas debe ser entero"
    assert n_filas >= 3, "El numero de filas debe ser mayor o igual a 3" 

    assert type(n_columnas) == int, "El numero de columnas debe ser entero"
    assert n_columnas >= 3, "El numero de columnas debe ser mayor o igual a 3" 


def crear_tablero(n_filas: int, n_columnas: int) -> List[List[str]]:
    """Crea un nuevo tablero de cuatro en línea, con dimensiones
    n_filas por n_columnas.
    Para todo el módulo `cuatro_en_linea`, las cadenas reconocidas para los
    valores de la lista de listas son las siguientes:
        - Celda vacía: ' '
        - Celda con símbolo X: 'X'
        - Celda con símbolo O: 'O'

    PRECONDICIONES:
        - n_filas y n_columnas son enteros positivos mayores a tres.

    POSTCONDICIONES:
        - la función devuelve un nuevo tablero lleno de casilleros vacíos
          que se puede utilizar para llamar al resto de las funciones del
          módulo.

    EJEMPLO:
        >>> crear_tablero(4, 5)
        [
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ']
        ]
    """

    validar_dimensiones_tablero(n_filas, n_columnas)

    tablero = []

    for fila in range(n_filas):
        fila_actual = []
        for col in range(n_columnas):
            fila_actual.append(' ')
        tablero.append(fila_actual)
    
    return tablero

def contar_casilleros_llenos(tablero: List[List[str]]) -> int:
    
    total = 0

    for fila in tablero:
        for col in fila:
            if col != " ": total += 1

    return total

def es_turno_de_x(tablero: List[List[str]]) -> bool:
    """Dado un tablero, devuelve True si el próximo turno es de X. Si, en caso
    contrario, es el turno de O, devuelve False.
    - Dado un tablero vacío, dicha función debería devolver `True`, pues el
      primer símbolo a insertar es X.
    - Luego de insertar el primer símbolo, esta función debería devolver `False`
      pues el próximo símbolo a insertar es O.
    - Luego de insertar el segundo símbolo, esta función debería devolver `True`
      pues el próximo símbolo a insertar es X.
    - ¿Qué debería devolver si hay tres símbolos en el tablero? ¿Y con cuatro
      símbolos?

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
        - los símbolos del tablero fueron insertados previamente insertados con
          la función `insertar_simbolo`"""
    
    total_casilleros_llenos = contar_casilleros_llenos(tablero)

    if(total_casilleros_llenos % 2 != 0): return False

    return True


def es_columna_valida(tablero: List[List[str]], columna: int) -> bool:
    if type(columna) != int:
        print("Ha ingresado una columna invalida: Intente nuevamente")
        return False

    if tablero[0][columna] != " ":
        print("La columna ingresada ya esta llena. Intente nuevamente")
        return False

    if not (columna in range(0,len(tablero[0]))):
        print("Columna fuera de rango. Intente nuevamente.")
        return False

    return True


def insertar_simbolo(tablero: List[List[str]], columna: int) -> bool:
    """Dado un tablero y un índice de columna, se intenta colocar el símbolo del
    turno actual en dicha columna.
    Un símbolo solo se puede colocar si el número de columna indicada por
    parámetro es válido, y si queda espacio en dicha columna.
    El número de la columna se encuentra indexado en 0, entonces `0` corresponde
    a la primer columna.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    POSTCONDICIONES:
        - si la función devolvió `True`, se modificó el contenido del parámetro
          `tablero`. Caso contrario, el parámetro `tablero` no se vio modificado
    """
    
    if(es_columna_valida(tablero, columna)):
        for fila in range(len(tablero)):
            
            "columna_seleccionada = tablero[fila][columna]"

            if(tablero[fila][columna] == " "):
                print("La fila es", tablero[fila])
                if(es_turno_de_x(tablero)):
                    tablero[fila][columna] = "X"
                    print("La fila modificada es", tablero[fila])

                    print(tablero)
                    return True
                else:
                    tablero[fila][columna] = "O"
                    print("La fila modificada es", tablero[fila])
                    return True
    
    return False
            



def tablero_completo(tablero: List[List[str]]) -> bool:
    """Dado un tablero, indica si se encuentra completo. Un tablero se considera
    completo cuando no hay más espacio para insertar un nuevo símbolo, en tal
    caso la función devuelve `True`.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`
    """


def obtener_ganador(tablero: List[List[str]]) -> str:
    """Dado un tablero, devuelve el símbolo que ganó el juego.
    El símbolo ganador estará dado por aquel que tenga un cuatro en línea. Es
    decir, por aquel símbolo que cuente con cuatro casilleros consecutivos
    alineados de forma horizontal, vertical, o diagonal.
    En el caso que el juego no tenga ganador, devuelve el símbolo vacío.
    En el caso que ambos símbolos cumplan con la condición de cuatro en línea,
    la función devuelve cualquiera de los dos.

    PRECONDICIONES:
        - el parámetro `tablero` fue inicializado con la función `crear_tablero`

    EJEMPLO: para el siguiente tablero, el ganador es 'X' por tener un cuatro en
    línea en diagonal
        [
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', ' ', ' ', ' '],
            [' ', ' ', 'O', 'X', ' ', ' ', ' '],
            [' ', ' ', 'X', 'O', 'X', ' ', ' '],
            [' ', 'O', 'O', 'X', 'X', 'X', 'O'],
        ]
    """