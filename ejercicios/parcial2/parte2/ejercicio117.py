def decodificar_dato(dato):
    d_decodificado = ""

    for c in dato:
        if c != "<" and c != ">":
            d_decodificado = d_decodificado + c
    
    return d_decodificado

def decodificar_info(linea):
    datos = linea.split(";")
    info = map(decodificar_dato,datos)
    return info

def dist(p1_x, p1_y, p2_x,p2_y):
    return abs(p1_x - p2_x) + abs(p1_y - p2_y)

def pokemon_cercano(ruta, gimnasios):
    with open(ruta, "a") as archivo:
        for linea in archivo:
            pokemon, tipo, pos_x_p, pos_y_p = decodificar_info(linea)
            gim_cercano = ""
            distancia = 0
            for nombre_gim, posicion in gimnasios.items():
                pos_x_g, pos_y_g = posicion
                dist_calculada = dist(pos_x_p,pos_y_p,pos_x_g,pos_y_g)
                if distancia == 0 or dist_calculada < distancia:
                    distancia = dist_calculada
                    gim_cercano = nombre_gim
            archivo.write(f"<{pokemon};<{tipo}>;<{gim_cercano}>")
