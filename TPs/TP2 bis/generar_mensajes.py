import utils

def generar_mensaje(ruta):

    contactos = utils.obtener_contactos(ruta)

    contacto_seleccionado = utils.seleccionar_contacto(contactos)

    mensajes = utils.filtrar_mensajes_de_contacto(ruta, contacto_seleccionado)

    inicios_de_mensaje = utils.obtener_cantidad_de_inicios(mensajes) 
    primer_palabra = utils.obtener_palabra_probable(inicios_de_mensaje)

    palabras_mensaje = [primer_palabra]

    while True:
        ultima_palabra = palabras_mensaje[-1]

        if(ultima_palabra[-1]=="."):
            return " ".join(palabras_mensaje)

        palabras_siguientes = utils.obtener_palabras_siguientes(ultima_palabra, mensajes)

        if palabras_siguientes != {}:
            nueva_palabra = utils.obtener_palabra_probable(palabras_siguientes)
            palabras_mensaje.append(nueva_palabra)
        else:
            palabras_mensaje[-1] = palabras_mensaje[-1] + "."