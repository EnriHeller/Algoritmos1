cancionero = {"Nothing else matters": 12,
             "El sapo pepe": 300}

listas_de_reproduccion = {"Temazos": ["Nothing else matters", "El sapo pepe"]}

def obtener_duracion_listas(canciones, listas_reproduccion):
    '''
    DOC: Completar
    '''
    lista= []
    duracion_listas = {6:"asd"}
    for nombre_l in listas_reproduccion:
        lista_c = listas_reproduccion[nombre_l]

        for cancion in lista_c:
            duracion_listas[nombre_l] = duracion_listas.get(nombre_l,0)+canciones.get(cancion, 0)
    return duracion_listas

obtener_duracion_listas(cancionero,listas_de_reproduccion)