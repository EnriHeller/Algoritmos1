import utils 

def contar_palabras_por_contacto(ruta:str):
    """
    Solicita una secuencia de palabras dentro de una cadena, separadas por espacio. Las mismas se buscan dentro de un archivo de chat de Whatsapp para Android (ruta). Se cuenta la cantidad de veces que cada contacto repite cada palabra y se guarda un reporte de ello, en el archivo destino que se indique.
    """
    
    palabras = utils.definir_palabras()
    archivo = utils.definir_archivo_reporte()

    resultado = {}

    with open(ruta) as chat:
        for linea in chat:
            
            if(not utils.es_mensaje_valido(linea)): continue
            
            contacto, mensaje = utils.obtener_informacion_de_linea(linea)

            palabras_encontradas = utils.palabras_por_mensaje(palabras,mensaje.lower())

            if contacto not in resultado:
                resultado[contacto] = {}

            for palabra, cantidad in palabras_encontradas.items():
                resultado[contacto][palabra] = resultado[contacto].get(palabra, 0) + cantidad

    with open(archivo,"a") as reporte:

        encabezado = "contacto, palabra, frecuencia\n"
        reporte.write(encabezado)
        
        for contacto, palabra in resultado.items():
            for clave, cantidad in palabra.items():
                reporte.write(f"{contacto}, {clave}, {cantidad}\n")

        


