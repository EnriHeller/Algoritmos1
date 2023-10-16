def definir_palabras()->[str]:
    entrada = input("Ingrese las palabras para contar entre contactos: ")
    lista_palabras = entrada.lower().split()

    return lista_palabras

def es_mensaje_valido(linea: str)->bool:

    "Teniendo en cuenta que los mensajes validos enviados por un contacto siempre respetan la sintaxis: 'Contacto: Mensaje', un mensaje valido será aquel que tenga ': ' dentro."

    return ": " in linea

def obtener_informacion_del_mensaje(mensaje):
    contacto_y_mensaje = mensaje.split(" - ", 1)[1]
    contacto, mensaje = contacto_y_mensaje.split(":",1)

    return contacto,mensaje

def palabras_por_mensaje(palabras_a_filtrar:[str], mensaje:str) -> dict:
    resultado = {}

    for palabra in palabras_a_filtrar:
        lista_palabras = mensaje.split(" ")
        palabras_filtradas = list(filter(lambda p: p==palabra, lista_palabras))
        resultado[palabra] = resultado.get(palabra,0) + len(palabras_filtradas)

    return resultado

def definir_archivo():
    while True:
        try:
            archivo = input("Ingrese el archivo destino para guardar el reporte: ")
            return archivo
        except FileNotFoundError:
            print("Error al ingresar nombre del archivo. Intente nuevamente")


def contar_palabras_por_contacto(route):
    palabras = definir_palabras()
    archivo = input("Ingrese el archivo destino para guardar el reporte: ")

    resultado = {}

    with open(route) as chat:
        for linea in chat:
            
            if(not es_mensaje_valido(linea)): continue
            
            contacto, mensaje = obtener_informacion_del_mensaje(linea)

            palabras_encontradas = palabras_por_mensaje(palabras,mensaje.lower())

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

        print("Reporte generado!")


