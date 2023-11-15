import random


class Flood:
    """
    Clase para administrar un tablero de N colores.
    """

    def __init__(self, alto, ancho):
        """
        Genera un nuevo Flood de un mismo color con las dimensiones dadas.

        Argumentos:
            alto, ancho (int): Tamaño de la grilla.
        """
        """El alto será la cantidad de filas y el ancho la cantidad de columnas. """
        self.alto = alto
        self.ancho = ancho
        self.rango_colores = [0]
        self.movimientos_posibles = [
                (1,0),
                (-1,0), 
                (0,1),
                (0,-1),
        ]

        tablero = []

        for i_fila in range(alto):
            tablero.append([])
            for i_columna in range(ancho):
                tablero[i_fila].append(0)
        
        self.tablero = tablero
        


    def mezclar_tablero(self, n_colores):
        """
        Asigna de forma completamente aleatoria hasta `n_colores` a lo largo de
        las casillas del tablero.

        Argumentos:
            n_colores (int): Cantidad maxima de colores a incluir en la grilla.
        """
        self.rango_colores = list(range(n_colores))
        for i_fila in range(self.alto):
            for i_columna in range(self.ancho):
                self.tablero[i_fila][i_columna] = random.choice(self.rango_colores)
        

    def obtener_color(self, fil, col):
        """
        Devuelve el color que se encuentra en las coordenadas solicitadas.

        Argumentos:
            fil, col (int): Posiciones de la fila y columna en la grilla.

        Devuelve:
            Color asignado.
        """
        return self.tablero[fil][col]


    def obtener_posibles_colores(self):
        """
        Devuelve una secuencia ordenada de todos los colores posibles del juego.
        La secuencia tendrá todos los colores posibles que fueron utilizados
        para generar el tablero, sin importar cuántos de estos colores queden
        actualmente en el tablero.

        Devuelve:
            iterable: secuencia ordenada de colores.
        """
        
        return self.rango_colores

    def dimensiones(self):
        """
        Dimensiones de la grilla (filas y columnas)

        Devuelve:
            (int, int): alto y ancho de la grilla en ese orden.
        """
        alto = len(self.tablero)
        ancho = len(self.tablero[0])
        return alto, ancho

    def es_posicion_valida(self, fila, columna):
        return fila in range(self.alto) and columna in range(self.ancho)

    def verificar_color_casillero(self, i_fila, i_col, primer_color, color_nuevo):

        color_actual = self.obtener_color(i_fila,i_col)

        if color_actual == color_nuevo or color_actual != primer_color:
            return
        
        self.tablero[i_fila][i_col] = color_nuevo

        for i,j in self.movimientos_posibles:
            nueva_fila, nueva_col = i_fila+i, i_col+j
            if self.es_posicion_valida(nueva_fila,nueva_col):
                self.verificar_color_casillero(nueva_fila, nueva_col, primer_color, color_nuevo)



    def cambiar_color(self, color_nuevo):
        """
        Asigna el nuevo color al Flood de la grilla. Es decir, a todas las
        coordenadas que formen un camino continuo del mismo color comenzando
        desde la coordenada origen en (0, 0) se les asignará `color_nuevo`

        Argumentos:
            color_nuevo: Valor del nuevo color a asignar al Flood.
        """
        primer_color = self.obtener_color(0,0)
        self.verificar_color_casillero(0, 0, primer_color, color_nuevo)


    def clonar(self):
        """
        Devuelve:
            Flood: Copia del Flood actual
        """
        atributos = self.__dict__
        copia = Flood(atributos["alto"], atributos["ancho"])
        copia.tablero = atributos["tablero"]
        copia.rango_colores = atributos["rango_colores"]
        return copia


    def esta_completado(self):
        """
        Indica si todas las coordenadas de grilla tienen el mismo color

        Devuelve:
            bool: True si toda la grilla tiene el mismo color
        """
        # Parte 4: Tu código acá...
        return False