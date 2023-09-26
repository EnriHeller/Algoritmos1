import cuatro_en_linea



def main():

    def definir_dimensiones_tablero():
        while True:
            n_filas = input("Ingrese el ancho de juego entre 4 y 10: ")

            if not n_filas.isdecimal():
                print("Caracter invalido para fila ingresada. Intente nuevamente.")
                continue
            else:
                n_filas = int(n_filas)


            if n_filas < 4 or n_filas>10:
                print("Fila ingresada fuera de rango. intente nuevamente.")
                continue

            break
        
        while True:
            m_col = input("Ingrese el alto del juego entre 4 y 10: ")

            if not m_col.isdecimal():
                print("Caracter invalido para columna ingresada. Intente nuevamente.")
                continue
            else:
                m_col = int(m_col)


            if m_col < 4 or m_col>10:
                print("Columna ingresada fuera de rango. intente nuevamente.")
                continue

            break
        return n_filas, m_col
    
    n_filas, m_col = definir_dimensiones_tablero()
    tablero = cuatro_en_linea.crear_tablero(n_filas, m_col)

    
    def columnas_enumeradas():
        columnas_int = list(range(m_col))
        return list(map(str, columnas_int))
    
    def separacion_horizontal():
        separaciones = []
        for col in range(m_col):
            separaciones.append("_")
        return separaciones

    def imprimir_fila(fila):
        fila_formateada = " | ".join(fila)
        print(fila_formateada.ljust(6," "))

    def imprimir_tablero():
        print()
        
        imprimir_fila(columnas_enumeradas())
        for fila in tablero:
            imprimir_fila(separacion_horizontal())
            imprimir_fila(fila)
        
        print()

    def imprimir_turno():
        simbolo = " "
        if cuatro_en_linea.es_turno_de_x(tablero):
            simbolo = "X"
        else:
            simbolo = "O"
        print(f"\033[1m-Es turno de {simbolo}-\033[0m")

    def solicitar_columna():
        print(f"Ingrese una columna entre 0 y {str(len(tablero) - 1)}. 's' para salir.")
        columna = input("Entrada: ")

        if(columna == "s"):
            return "salir"
        
        if not columna.isdecimal():
            print("Ha ingresado una columna invalida: Intente nuevamente")
            return False

        cuatro_en_linea.insertar_simbolo(tablero, int(columna))

    while True:
        imprimir_tablero()
        imprimir_turno()
        nueva_entrada = solicitar_columna()
        if(nueva_entrada == "salir"):
            break
        ganador = cuatro_en_linea.obtener_ganador(tablero)
        if(ganador != " "):
            imprimir_tablero()
            print(f"\033[1m-Felicituaciones {ganador}!. Ganaste.-\033[0m")
            print("-Fin del juego-")
            break

main()
