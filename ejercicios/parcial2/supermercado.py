pedido_e = [
    { "nombre_producto1": 6,  "nombre_producto_n":2},
    { "nombre_producto1": 3,  "nombre_producto_n":4},
    ]


def generar_texto(dict):
    texto_final = ""
    for k,v in dict.items():
        texto_final = texto_final + f"{k};{v}\n"
    return texto_final
def resumir_pedidos(pedidos, nombre_archivo_dest):
    '''
    DOC: Completar
    '''
    pedidos_totales= {}
    for pedido in pedidos:

        for nombre, cantidad in pedido.items():

            pedidos_totales[nombre] = pedidos_totales.get(nombre,0)+cantidad



    with open(nombre_archivo_dest,"w") as resumen:
        texto = generar_texto(pedidos_totales)
        resumen.write(texto)

resumir_pedidos(pedido_e,"prueba")



