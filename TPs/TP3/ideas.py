def escanear_frontera_flood(self, fil_actual, col_actual, n_colores, escaneados):
        primer_color = self.obtener_color(0, 0)
        estoy_en_flood = self.tablero[fil_actual][col_actual] == primer_color

        if estoy_en_flood and (fil_actual, col_actual) not in escaneados:
            escaneados.append((fil_actual, col_actual))

            for i, j in self.movimientos_posibles:
                nueva_fil = fil_actual + i
                nueva_col = col_actual + j

                if self.es_posicion_valida(nueva_fil, nueva_col):
                    color_nuevo = self.obtener_color(nueva_fil, nueva_col)
                    es_color_distinto = color_nuevo != primer_color

                    if es_color_distinto:
                        n_colores[color_nuevo] = n_colores.get(color_nuevo, 0) + 1

                    self.escanear_frontera_flood(nueva_fil, nueva_col, n_colores, escaneados)

def obtener_frontera_flood(self):
            casilleros_escaneados = []
            n_colores = {}
            self.escanear_frontera_flood(0, 0, n_colores, casilleros_escaneados)
            return n_colores
        
def obtener_mejor_solucion(self):
            opciones = self.obtener_frontera_flood()
            color_seleccionado = None
            cantidad_maxima = 0

            for color, cantidad in opciones.items():
                if cantidad > cantidad_maxima:
                    color_seleccionado = color
            
            return color_seleccionado
